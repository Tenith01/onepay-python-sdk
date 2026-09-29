"""Transaction resource — verify payment status."""

from __future__ import annotations

from typing import TYPE_CHECKING

from onepay._auth import build_auth_header
from onepay.models.transaction import TransactionStatusResponse

if TYPE_CHECKING:
    from onepay._config import OnePayConfig
    from onepay._http import AsyncHttpClient, SyncHttpClient


class TransactionResource:
    """Sync transaction operations."""

    def __init__(self, http: SyncHttpClient, config: OnePayConfig) -> None:
        self._http = http
        self._config = config

    def get_status(self, *, onepay_transaction_id: str) -> TransactionStatusResponse:
        """Verify the outcome of a payment transaction.

        Always verify server-side — do not rely solely on redirect URL parameters.

        Args:
            onepay_transaction_id: The transaction ID from checkout creation
                (``ipg_transaction_id``).

        Returns:
            :class:`TransactionStatusResponse` with payment status and details.
        """
        app_id = self._config.get_app_id_or_raise()

        payload: dict[str, str] = {
            "app_id": app_id,
            "onepay_transaction_id": onepay_transaction_id,
        }

        response = self._http.request(
            "POST",
            "/v3/transaction/status/",
            json=payload,
            headers=build_auth_header(self._config.get_app_token_or_raise()),
        )

        result: TransactionStatusResponse = TransactionStatusResponse.model_validate(response)
        return result


class AsyncTransactionResource:
    """Async transaction operations."""

    def __init__(self, http: AsyncHttpClient, config: OnePayConfig) -> None:
        self._http = http
        self._config = config

    async def get_status(self, *, onepay_transaction_id: str) -> TransactionStatusResponse:
        """Async version of :meth:`TransactionResource.get_status`."""
        app_id = self._config.get_app_id_or_raise()

        payload: dict[str, str] = {
            "app_id": app_id,
            "onepay_transaction_id": onepay_transaction_id,
        }

        response = await self._http.request(
            "POST",
            "/v3/transaction/status/",
            json=payload,
            headers=build_auth_header(self._config.get_app_token_or_raise()),
        )

        result: TransactionStatusResponse = TransactionStatusResponse.model_validate(response)
        return result
