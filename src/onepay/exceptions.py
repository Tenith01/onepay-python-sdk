"""Exception hierarchy for the OnePay Python SDK.

All exceptions inherit from :class:`OnePayError`, making it easy to catch
any SDK-related error with a single ``except OnePayError`` clause.
"""

from __future__ import annotations

from typing import Any


class OnePayError(Exception):
    """Base exception for all OnePay SDK errors."""

    def __init__(self, message: str = "An error occurred with the OnePay API") -> None:
        self.message = message
        super().__init__(self.message)


class APIError(OnePayError):
    """Raised when the OnePay API returns an error response.

    Attributes:
        status_code: HTTP status code from the response.
        message: Human-readable error message.
        raw_response: The full parsed JSON response body, if available.
    """

    def __init__(
        self,
        message: str,
        status_code: int,
        raw_response: dict[str, Any] | None = None,
    ) -> None:
        self.status_code = status_code
        self.raw_response = raw_response or {}
        super().__init__(message)

    def __str__(self) -> str:
        return f"[HTTP {self.status_code}] {self.message}"


class AuthenticationError(APIError):
    """Raised on HTTP 401 — missing or invalid credentials / hash."""

    def __init__(
        self,
        message: str = "Authentication failed. Check your credentials.",
        raw_response: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message=message, status_code=401, raw_response=raw_response)


class InvalidRequestError(APIError):
    """Raised on HTTP 400 — bad parameters in the request.

    Subclasses provide more specific error types.
    """

    def __init__(
        self,
        message: str = "Invalid request parameters.",
        raw_response: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message=message, status_code=400, raw_response=raw_response)


class InvalidAppIdError(InvalidRequestError):
    """Raised when the app_id is invalid or not recognized."""

    def __init__(
        self,
        message: str = "Invalid app ID.",
        raw_response: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message=message, raw_response=raw_response)


class InvalidAmountError(InvalidRequestError):
    """Raised when the amount value is invalid."""

    def __init__(
        self,
        message: str = "Invalid amount.",
        raw_response: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message=message, raw_response=raw_response)


class InvalidCurrencyError(InvalidRequestError):
    """Raised when the currency is not supported or invalid."""

    def __init__(
        self,
        message: str = "Currency type not available for the app.",
        raw_response: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message=message, raw_response=raw_response)


class RefundNotAllowedError(InvalidRequestError):
    """Raised when a refund cannot be processed (e.g., already refunded, test transaction)."""

    def __init__(
        self,
        message: str = "Refund not allowed for this transaction.",
        raw_response: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message=message, raw_response=raw_response)


class RateLimitError(APIError):
    """Raised on HTTP 429 — too many requests.

    Attributes:
        retry_after: Suggested number of seconds to wait before retrying.
    """

    def __init__(
        self,
        message: str = "Rate limit exceeded. Please retry after a short wait.",
        retry_after: float | None = None,
        raw_response: dict[str, Any] | None = None,
    ) -> None:
        self.retry_after = retry_after
        super().__init__(message=message, status_code=429, raw_response=raw_response)


class NetworkError(OnePayError):
    """Raised on connection failures, DNS errors, or timeouts."""

    def __init__(
        self,
        message: str = "A network error occurred while communicating with OnePay.",
        original_error: Exception | None = None,
    ) -> None:
        self.original_error = original_error
        super().__init__(message)
