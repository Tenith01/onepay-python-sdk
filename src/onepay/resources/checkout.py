"""Checkout resource — create payment sessions."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from onepay._auth import build_auth_header, generate_hash
from onepay.models.checkout import CheckoutResponse

if TYPE_CHECKING:
    from decimal import Decimal

    from onepay._config import OnePayConfig
    from onepay._http import AsyncHttpClient, SyncHttpClient


class CheckoutResource:
    """Sync checkout operations."""

    def __init__(self, http: SyncHttpClient, config: OnePayConfig) -> None:
        self._http = http
        self._config = config

    def create(
        self,
        *,
        amount: float | Decimal | str,
        currency: str,
        reference: str,
        customer_first_name: str,
        customer_last_name: str,
        customer_phone_number: str,
        customer_email: str,
        transaction_redirect_url: str,
        additional_data: str | None = None,
        items: list[str] | None = None,
    ) -> CheckoutResponse:
        """Create a checkout transaction and get a redirect URL.

        Args:
            amount: Transaction amount (e.g., ``1000.00``).
            currency: Three-letter ISO currency code (e.g., ``"LKR"``).
            reference: Your internal order or reference ID.
            customer_first_name: Customer's first name.
            customer_last_name: Customer's last name.
            customer_phone_number: Phone in E.164 format (e.g., ``"+94771234567"``).
            customer_email: Customer's email address.
            transaction_redirect_url: URL to redirect customer after payment.
            additional_data: Optional metadata to associate with the transaction.
            items: Optional list of item IDs from the Items API.

        Returns:
            :class:`CheckoutResponse` with ``redirect_url`` and ``ipg_transaction_id``.
        """
        app_id = self._config.get_app_id_or_raise()
        hash_salt = self._config.get_hash_salt_or_raise()

        # Format amount to 2 decimal places
        amount_str = f"{float(amount):.2f}"

        # Generate SHA-256 hash
        hash_value = generate_hash(app_id, currency, amount_str, hash_salt)

        payload: dict[str, Any] = {
            "app_id": app_id,
            "amount": float(amount_str),
            "currency": currency,
            "hash": hash_value,
            "reference": reference,
            "customer_first_name": customer_first_name,
            "customer_last_name": customer_last_name,
            "customer_phone_number": customer_phone_number,
            "customer_email": customer_email,
            "transaction_redirect_url": transaction_redirect_url,
        }

        if additional_data is not None:
            payload["additionalData"] = additional_data
        if items is not None:
            payload["items"] = items

        headers = build_auth_header(self._config.get_app_token_or_raise())

        response = self._http.request(
            "POST",
            "/v3/checkout/link/",
            json=payload,
            headers=headers,
        )

        return CheckoutResponse.model_validate(response)


class AsyncCheckoutResource:
    """Async checkout operations."""

    def __init__(self, http: AsyncHttpClient, config: OnePayConfig) -> None:
        self._http = http
        self._config = config

    async def create(
        self,
        *,
        amount: float | Decimal | str,
        currency: str,
        reference: str,
        customer_first_name: str,
        customer_last_name: str,
        customer_phone_number: str,
        customer_email: str,
        transaction_redirect_url: str,
        additional_data: str | None = None,
        items: list[str] | None = None,
    ) -> CheckoutResponse:
        """Async version of :meth:`CheckoutResource.create`."""
        app_id = self._config.get_app_id_or_raise()
        hash_salt = self._config.get_hash_salt_or_raise()

        amount_str = f"{float(amount):.2f}"
        hash_value = generate_hash(app_id, currency, amount_str, hash_salt)

        payload: dict[str, Any] = {
            "app_id": app_id,
            "amount": float(amount_str),
            "currency": currency,
            "hash": hash_value,
            "reference": reference,
            "customer_first_name": customer_first_name,
            "customer_last_name": customer_last_name,
            "customer_phone_number": customer_phone_number,
            "customer_email": customer_email,
            "transaction_redirect_url": transaction_redirect_url,
        }

        if additional_data is not None:
            payload["additionalData"] = additional_data
        if items is not None:
            payload["items"] = items

        headers = build_auth_header(self._config.get_app_token_or_raise())

        response = await self._http.request(
            "POST",
            "/v3/checkout/link/",
            json=payload,
            headers=headers,
        )

        return CheckoutResponse.model_validate(response)
