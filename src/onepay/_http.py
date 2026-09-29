"""HTTP client layer for the OnePay SDK.

Provides both synchronous and asynchronous HTTP clients with automatic
retry logic, error parsing, and structured logging.
"""

from __future__ import annotations

import logging
import random
import time
from typing import TYPE_CHECKING, Any, TypeVar

import httpx

from onepay._version import __version__
from onepay.exceptions import (
    APIError,
    AuthenticationError,
    InvalidRequestError,
    NetworkError,
    OnePayError,
    RateLimitError,
)

if TYPE_CHECKING:
    from onepay._config import OnePayConfig

logger = logging.getLogger("onepay")

T = TypeVar("T")

_USER_AGENT = f"onepay-python/{__version__}"


def _parse_error_response(
    status_code: int,
    response_data: dict[str, Any],
    headers: httpx.Headers | dict[str, str] | None = None,
) -> APIError:
    """Parse an HTTP error response into the appropriate exception type."""
    message = response_data.get("message", "") or response_data.get("error", "")
    if not message:
        message = str(response_data)

    # Detect specific 400 error types from the message
    msg_lower = message.lower() if isinstance(message, str) else ""

    if status_code == 401:
        return AuthenticationError(message=message, raw_response=response_data)

    if status_code == 429:
        err = RateLimitError(message=message, raw_response=response_data)
        if headers and "Retry-After" in headers:
            try:
                err.retry_after = float(headers["Retry-After"])
            except ValueError:
                pass
        return err

    if status_code == 400:
        if "invalid app" in msg_lower:
            from onepay.exceptions import InvalidAppIdError

            return InvalidAppIdError(message=message, raw_response=response_data)
        if "invalid amount" in msg_lower:
            from onepay.exceptions import InvalidAmountError

            return InvalidAmountError(message=message, raw_response=response_data)
        if "currency" in msg_lower and ("not available" in msg_lower or "invalid" in msg_lower):
            from onepay.exceptions import InvalidCurrencyError

            return InvalidCurrencyError(message=message, raw_response=response_data)
        if "refund" in msg_lower:
            from onepay.exceptions import RefundNotAllowedError

            return RefundNotAllowedError(message=message, raw_response=response_data)
        return InvalidRequestError(message=message, raw_response=response_data)

    return APIError(message=message, status_code=status_code, raw_response=response_data)


def _should_retry(status_code: int) -> bool:
    """Determine if a request should be retried based on status code."""
    return status_code == 429 or status_code >= 500


def _backoff_delay(attempt: int, base: float = 0.5, max_delay: float = 30.0) -> float:
    """Calculate exponential backoff delay with jitter."""
    delay = min(base * (2**attempt), max_delay)
    jitter = random.uniform(0, delay * 0.5)  # noqa: S311
    return float(delay + jitter)


class SyncHttpClient:
    """Synchronous HTTP client backed by ``httpx.Client``."""

    def __init__(self, config: OnePayConfig) -> None:
        self._config = config
        self._client = httpx.Client(
            base_url=config.base_url,
            timeout=httpx.Timeout(config.timeout),
            headers={"User-Agent": _USER_AGENT},
        )

    def request(
        self,
        method: str,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        """Execute an HTTP request with retry logic.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE).
            path: API endpoint path (e.g., ``/v3/checkout/link/``).
            json: JSON body for the request.
            params: Query parameters.
            headers: Additional headers.

        Returns:
            Parsed JSON response as a dictionary.

        Raises:
            APIError: On API error responses.
            NetworkError: On connection or timeout failures.
        """
        last_error: Exception | None = None

        for attempt in range(self._config.max_retries + 1):
            try:
                if self._config.debug:
                    logger.debug(
                        "OnePay API request: %s %s (attempt %d/%d)",
                        method,
                        path,
                        attempt + 1,
                        self._config.max_retries + 1,
                    )

                response = self._client.request(
                    method=method,
                    url=path,
                    json=json,
                    params=params,
                    headers=headers,
                )

                if self._config.debug:
                    logger.debug(
                        "OnePay API response: %d %s",
                        response.status_code,
                        path,
                    )

                # Parse response
                try:
                    response_data = response.json()
                except Exception:
                    response_data = {"message": response.text}

                # Success
                if response.is_success:
                    return response_data  # type: ignore[no-any-return]

                # Check if we should retry
                if _should_retry(response.status_code) and attempt < self._config.max_retries:
                    delay = _backoff_delay(attempt)
                    if response.status_code == 429 and "Retry-After" in response.headers:
                        try:
                            delay = float(response.headers["Retry-After"])
                        except ValueError:
                            pass
                    if self._config.debug:
                        logger.debug(
                            "Retrying in %.2fs after HTTP %d",
                            delay,
                            response.status_code,
                        )
                    time.sleep(delay)
                    last_error = _parse_error_response(
                        response.status_code, response_data, response.headers
                    )
                    continue

                # Non-retryable error
                raise _parse_error_response(response.status_code, response_data, response.headers)

            except OnePayError:
                raise
            except httpx.TimeoutException as exc:
                last_error = NetworkError(
                    message=f"Request timed out: {method} {path}",
                    original_error=exc,
                )
                if attempt < self._config.max_retries:
                    delay = _backoff_delay(attempt)
                    time.sleep(delay)
                    continue
                raise last_error from exc
            except httpx.HTTPError as exc:
                last_error = NetworkError(
                    message=f"Network error: {exc}",
                    original_error=exc,
                )
                if attempt < self._config.max_retries:
                    delay = _backoff_delay(attempt)
                    time.sleep(delay)
                    continue
                raise last_error from exc

        # Should not reach here, but just in case
        if last_error:
            raise last_error
        raise NetworkError(message="Request failed after all retries.")

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()


class AsyncHttpClient:
    """Asynchronous HTTP client backed by ``httpx.AsyncClient``."""

    def __init__(self, config: OnePayConfig) -> None:
        self._config = config
        self._client = httpx.AsyncClient(
            base_url=config.base_url,
            timeout=httpx.Timeout(config.timeout),
            headers={"User-Agent": _USER_AGENT},
        )

    async def request(
        self,
        method: str,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        """Execute an async HTTP request with retry logic.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE).
            path: API endpoint path (e.g., ``/v3/checkout/link/``).
            json: JSON body for the request.
            params: Query parameters.
            headers: Additional headers.

        Returns:
            Parsed JSON response as a dictionary.

        Raises:
            APIError: On API error responses.
            NetworkError: On connection or timeout failures.
        """
        import asyncio

        last_error: Exception | None = None

        for attempt in range(self._config.max_retries + 1):
            try:
                if self._config.debug:
                    logger.debug(
                        "OnePay API request: %s %s (attempt %d/%d)",
                        method,
                        path,
                        attempt + 1,
                        self._config.max_retries + 1,
                    )

                response = await self._client.request(
                    method=method,
                    url=path,
                    json=json,
                    params=params,
                    headers=headers,
                )

                if self._config.debug:
                    logger.debug(
                        "OnePay API response: %d %s",
                        response.status_code,
                        path,
                    )

                try:
                    response_data = response.json()
                except Exception:
                    response_data = {"message": response.text}

                if response.is_success:
                    return response_data  # type: ignore[no-any-return]

                if _should_retry(response.status_code) and attempt < self._config.max_retries:
                    delay = _backoff_delay(attempt)
                    if response.status_code == 429 and "Retry-After" in response.headers:
                        try:
                            delay = float(response.headers["Retry-After"])
                        except ValueError:
                            pass
                    if self._config.debug:
                        logger.debug(
                            "Retrying in %.2fs after HTTP %d",
                            delay,
                            response.status_code,
                        )
                    await asyncio.sleep(delay)
                    last_error = _parse_error_response(
                        response.status_code, response_data, response.headers
                    )
                    continue

                raise _parse_error_response(response.status_code, response_data, response.headers)

            except OnePayError:
                raise
            except httpx.TimeoutException as exc:
                last_error = NetworkError(
                    message=f"Request timed out: {method} {path}",
                    original_error=exc,
                )
                if attempt < self._config.max_retries:
                    delay = _backoff_delay(attempt)
                    await asyncio.sleep(delay)
                    continue
                raise last_error from exc
            except httpx.HTTPError as exc:
                last_error = NetworkError(
                    message=f"Network error: {exc}",
                    original_error=exc,
                )
                if attempt < self._config.max_retries:
                    delay = _backoff_delay(attempt)
                    await asyncio.sleep(delay)
                    continue
                raise last_error from exc

        if last_error:
            raise last_error
        raise NetworkError(message="Request failed after all retries.")

    async def close(self) -> None:
        """Close the underlying async HTTP client."""
        await self._client.aclose()
