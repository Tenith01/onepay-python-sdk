"""Refunds resource — initiate full or partial refunds."""

from __future__ import annotations

from typing import Any, Dict, Optional

from onepay._auth import build_auth_header
from onepay._config import OnePayConfig
from onepay._http import AsyncHttpClient, SyncHttpClient
from onepay.models.refund import RefundResponse


class RefundResource:
    """Sync refund operations."""

    def __init__(self, http: SyncHttpClient, config: OnePayConfig) -> None:
        self._http = http
        self._config = config

    def create(
        self,
        *,
        onepay_transaction_id: str,
        refund_reason: str,
        is_partially: bool = False,
        amount: Optional[float] = None,
        refund_note: Optional[str] = None,
    ) -> RefundResponse:
        """Initiate a refund for a successfully paid transaction.

        Args:
            onepay_transaction_id: The OnePay transaction ID to refund.
            refund_reason: One of ``DUPLICATED``, ``FRAUDULENT``,
                ``OUT_OF_ORDER``, ``REQUESTED_BY_CUSTOMER``, ``OTHER``.
            is_partially: ``True`` for partial refund, ``False`` for full.
            amount: Required for partial refunds.
            refund_note: Optional free-text note.

        Returns:
            :class:`RefundResponse` with refund details.

        Raises:
            ValueError: If ``is_partially`` is True but ``amount`` is not provided.
        """
        if is_partially and amount is None:
            raise ValueError("amount is required for partial refunds (is_partially=True)")

        payload: Dict[str, Any] = {
            "app_id": self._config.get_app_id_or_raise(),
            "onepay_transaction_id": onepay_transaction_id,
            "refund_reason": refund_reason,
            "is_partially": is_partially,
        }
        if amount is not None:
            payload["amount"] = amount
        if refund_note is not None:
            payload["refund_note"] = refund_note

        headers = build_auth_header(self._config.get_app_token_or_raise())

        response = self._http.request(
            "POST",
            "/v3/transaction/refund/",
            json=payload,
            headers=headers,
        )
        return RefundResponse.model_validate(response)


class AsyncRefundResource:
    """Async refund operations."""

    def __init__(self, http: AsyncHttpClient, config: OnePayConfig) -> None:
        self._http = http
        self._config = config

    async def create(
        self,
        *,
        onepay_transaction_id: str,
        refund_reason: str,
        is_partially: bool = False,
        amount: Optional[float] = None,
        refund_note: Optional[str] = None,
    ) -> RefundResponse:
        """Async version of :meth:`RefundResource.create`."""
        if is_partially and amount is None:
            raise ValueError("amount is required for partial refunds (is_partially=True)")

        payload: Dict[str, Any] = {
            "app_id": self._config.get_app_id_or_raise(),
            "onepay_transaction_id": onepay_transaction_id,
            "refund_reason": refund_reason,
            "is_partially": is_partially,
        }
        if amount is not None:
            payload["amount"] = amount
        if refund_note is not None:
            payload["refund_note"] = refund_note

        headers = build_auth_header(self._config.get_app_token_or_raise())

        response = await self._http.request(
            "POST",
            "/v3/transaction/refund/",
            json=payload,
            headers=headers,
        )
        return RefundResponse.model_validate(response)
