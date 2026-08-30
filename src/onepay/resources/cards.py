"""Cards resource — manage saved card tokens and charge them."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from onepay._auth import build_auth_header
from onepay._config import OnePayConfig
from onepay._http import AsyncHttpClient, SyncHttpClient
from onepay.models.card import (
    CardData,
    ChargeCardResponse,
    DeleteCardResponse,
    GetCardResponse,
    ListCardsResponse,
)


class CardResource:
    """Sync card/token operations."""

    def __init__(self, http: SyncHttpClient, config: OnePayConfig) -> None:
        self._http = http
        self._config = config

    def list(self, *, customer_id: str) -> List[CardData]:
        """List all saved cards for a customer.

        Args:
            customer_id: Unique customer identifier.

        Returns:
            List of :class:`CardData` objects.
        """
        app_id = self._config.get_app_id_or_raise()
        headers = build_auth_header(self._config.get_access_token_or_raise())

        response = self._http.request(
            "GET",
            f"/v3/customers/{customer_id}/cards/",
            params={"app_id": app_id},
            headers=headers,
        )
        parsed = ListCardsResponse.model_validate(response)
        return parsed.data or []

    def get(self, *, customer_id: str, token_id: str) -> GetCardResponse:
        """Get details for a specific saved card.

        Args:
            customer_id: Unique customer identifier.
            token_id: Secure card token (e.g., ``"tok_12345678"``).

        Returns:
            :class:`GetCardResponse` with card details.
        """
        app_id = self._config.get_app_id_or_raise()
        headers = build_auth_header(self._config.get_access_token_or_raise())

        response = self._http.request(
            "GET",
            f"/v3/customers/{customer_id}/cards/{token_id}/",
            params={"app_id": app_id},
            headers=headers,
        )
        return GetCardResponse.model_validate(response)

    def delete(self, *, customer_id: str, token_id: str) -> DeleteCardResponse:
        """Soft-delete a saved card. Irreversible.

        Args:
            customer_id: Unique customer identifier.
            token_id: Secure card token to delete.

        Returns:
            :class:`DeleteCardResponse`.
        """
        app_id = self._config.get_app_id_or_raise()
        headers = build_auth_header(self._config.get_access_token_or_raise())

        response = self._http.request(
            "DELETE",
            f"/v3/customers/{customer_id}/cards/{token_id}/",
            params={"app_id": app_id},
            headers=headers,
        )
        return DeleteCardResponse.model_validate(response)

    def charge(
        self,
        *,
        customer_id: str,
        token_id: str,
        amount: str,
        currency: str,
    ) -> ChargeCardResponse:
        """Charge a saved card token.

        No customer interaction required — entirely server-triggered.

        Args:
            customer_id: Unique customer identifier.
            token_id: The saved card token to charge.
            amount: Amount as string (e.g., ``"1000.00"``).
            currency: Currency code (e.g., ``"LKR"``).

        Returns:
            :class:`ChargeCardResponse` with transaction details.
        """
        payload: Dict[str, Any] = {
            "app_id": self._config.get_app_id_or_raise(),
            "token_id": token_id,
            "amount": amount,
            "currency": currency,
        }

        headers = build_auth_header(self._config.get_access_token_or_raise())

        response = self._http.request(
            "POST",
            f"/v3/customers/{customer_id}/payments/",
            json=payload,
            headers=headers,
        )
        return ChargeCardResponse.model_validate(response)


class AsyncCardResource:
    """Async card/token operations."""

    def __init__(self, http: AsyncHttpClient, config: OnePayConfig) -> None:
        self._http = http
        self._config = config

    async def list(self, *, customer_id: str) -> List[CardData]:
        """Async version of :meth:`CardResource.list`."""
        app_id = self._config.get_app_id_or_raise()
        headers = build_auth_header(self._config.get_access_token_or_raise())

        response = await self._http.request(
            "GET",
            f"/v3/customers/{customer_id}/cards/",
            params={"app_id": app_id},
            headers=headers,
        )
        parsed = ListCardsResponse.model_validate(response)
        return parsed.data or []

    async def get(self, *, customer_id: str, token_id: str) -> GetCardResponse:
        """Async version of :meth:`CardResource.get`."""
        app_id = self._config.get_app_id_or_raise()
        headers = build_auth_header(self._config.get_access_token_or_raise())

        response = await self._http.request(
            "GET",
            f"/v3/customers/{customer_id}/cards/{token_id}/",
            params={"app_id": app_id},
            headers=headers,
        )
        return GetCardResponse.model_validate(response)

    async def delete(
        self, *, customer_id: str, token_id: str
    ) -> DeleteCardResponse:
        """Async version of :meth:`CardResource.delete`."""
        app_id = self._config.get_app_id_or_raise()
        headers = build_auth_header(self._config.get_access_token_or_raise())

        response = await self._http.request(
            "DELETE",
            f"/v3/customers/{customer_id}/cards/{token_id}/",
            params={"app_id": app_id},
            headers=headers,
        )
        return DeleteCardResponse.model_validate(response)

    async def charge(
        self,
        *,
        customer_id: str,
        token_id: str,
        amount: str,
        currency: str,
    ) -> ChargeCardResponse:
        """Async version of :meth:`CardResource.charge`."""
        payload: Dict[str, Any] = {
            "app_id": self._config.get_app_id_or_raise(),
            "token_id": token_id,
            "amount": amount,
            "currency": currency,
        }

        headers = build_auth_header(self._config.get_access_token_or_raise())

        response = await self._http.request(
            "POST",
            f"/v3/customers/{customer_id}/payments/",
            json=payload,
            headers=headers,
        )
        return ChargeCardResponse.model_validate(response)
