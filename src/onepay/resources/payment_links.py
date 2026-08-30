"""Payment links resource — CRUD for shareable payment URLs."""

from __future__ import annotations

from typing import Any, Dict, Optional

from onepay._auth import build_auth_header
from onepay._config import OnePayConfig
from onepay._http import AsyncHttpClient, SyncHttpClient
from onepay.models.payment_link import (
    CreatePaymentLinkResponse,
    DeletePaymentLinkResponse,
    GetPaymentLinkResponse,
    UpdatePaymentLinkResponse,
)


class PaymentLinkResource:
    """Sync payment link operations."""

    def __init__(self, http: SyncHttpClient, config: OnePayConfig) -> None:
        self._http = http
        self._config = config

    def create(
        self,
        *,
        amount: str,
        currency: str,
        reference_number: str,
        customer_first_name: str,
        customer_last_name: str,
        customer_email: str,
        customer_phone_number: str,
        description: Optional[str] = None,
        expiration_date: Optional[str] = None,
        allow_partial_payment: bool = False,
        minimum_partial_amount: Optional[str] = None,
    ) -> CreatePaymentLinkResponse:
        """Create a new payment link.

        Args:
            amount: Payment amount as a string.
            currency: Currency code.
            reference_number: Your internal reference.
            customer_first_name: Customer's first name.
            customer_last_name: Customer's last name.
            customer_email: Customer's email.
            customer_phone_number: Customer's phone number.
            description: Optional description.
            expiration_date: Optional expiry in YYYY-MM-DD format.
            allow_partial_payment: Allow partial payments.
            minimum_partial_amount: Minimum partial amount.

        Returns:
            :class:`CreatePaymentLinkResponse` with link details.
        """
        app_id = self._config.get_app_id_or_raise()
        api_key = self._config.get_api_key_or_raise()

        payload: Dict[str, Any] = {
            "amount": amount,
            "currency": currency,
            "reference_number": reference_number,
            "customer_first_name": customer_first_name,
            "customer_last_name": customer_last_name,
            "customer_email": customer_email,
            "customer_phone_number": customer_phone_number,
            "allow_partial_payment": allow_partial_payment,
        }
        if description is not None:
            payload["description"] = description
        if expiration_date is not None:
            payload["expiration_date"] = expiration_date
        if minimum_partial_amount is not None:
            payload["minimum_partial_amount"] = minimum_partial_amount

        headers = build_auth_header(api_key)
        response = self._http.request(
            "POST",
            "/v3/payment-link/",
            json=payload,
            params={"app_id": app_id},
            headers=headers,
        )
        return CreatePaymentLinkResponse.model_validate(response)

    def get(self, *, link_id: str) -> GetPaymentLinkResponse:
        """Retrieve details of a payment link.

        Args:
            link_id: The 8-character payment link ID.

        Returns:
            :class:`GetPaymentLinkResponse` with full link details.
        """
        app_id = self._config.get_app_id_or_raise()
        api_key = self._config.get_api_key_or_raise()
        headers = build_auth_header(api_key)

        response = self._http.request(
            "GET",
            f"/v3/payment-link/{link_id}/",
            params={"app_id": app_id},
            headers=headers,
        )
        return GetPaymentLinkResponse.model_validate(response)

    def update(self, *, link_id: str, description: str) -> UpdatePaymentLinkResponse:
        """Update a payment link's description.

        Only the description field can be modified after creation.

        Args:
            link_id: The 8-character payment link ID.
            description: New description.

        Returns:
            :class:`UpdatePaymentLinkResponse`.
        """
        app_id = self._config.get_app_id_or_raise()
        api_key = self._config.get_api_key_or_raise()

        payload: Dict[str, Any] = {
            "app_id": app_id,
            "description": description,
        }
        headers = build_auth_header(api_key)

        response = self._http.request(
            "PUT",
            f"/v3/payment-link/{link_id}/",
            json=payload,
            headers=headers,
        )
        return UpdatePaymentLinkResponse.model_validate(response)

    def delete(self, *, link_id: str) -> DeletePaymentLinkResponse:
        """Soft-delete a payment link.

        Cannot delete links with completed payments.

        Args:
            link_id: The 8-character payment link ID.

        Returns:
            :class:`DeletePaymentLinkResponse`.
        """
        app_id = self._config.get_app_id_or_raise()
        api_key = self._config.get_api_key_or_raise()
        headers = build_auth_header(api_key)

        response = self._http.request(
            "DELETE",
            f"/v3/payment-link/{link_id}/",
            params={"app_id": app_id},
            headers=headers,
        )
        return DeletePaymentLinkResponse.model_validate(response)


class AsyncPaymentLinkResource:
    """Async payment link operations."""

    def __init__(self, http: AsyncHttpClient, config: OnePayConfig) -> None:
        self._http = http
        self._config = config

    async def create(
        self,
        *,
        amount: str,
        currency: str,
        reference_number: str,
        customer_first_name: str,
        customer_last_name: str,
        customer_email: str,
        customer_phone_number: str,
        description: Optional[str] = None,
        expiration_date: Optional[str] = None,
        allow_partial_payment: bool = False,
        minimum_partial_amount: Optional[str] = None,
    ) -> CreatePaymentLinkResponse:
        """Async version of :meth:`PaymentLinkResource.create`."""
        app_id = self._config.get_app_id_or_raise()
        api_key = self._config.get_api_key_or_raise()

        payload: Dict[str, Any] = {
            "amount": amount,
            "currency": currency,
            "reference_number": reference_number,
            "customer_first_name": customer_first_name,
            "customer_last_name": customer_last_name,
            "customer_email": customer_email,
            "customer_phone_number": customer_phone_number,
            "allow_partial_payment": allow_partial_payment,
        }
        if description is not None:
            payload["description"] = description
        if expiration_date is not None:
            payload["expiration_date"] = expiration_date
        if minimum_partial_amount is not None:
            payload["minimum_partial_amount"] = minimum_partial_amount

        headers = build_auth_header(api_key)
        response = await self._http.request(
            "POST",
            "/v3/payment-link/",
            json=payload,
            params={"app_id": app_id},
            headers=headers,
        )
        return CreatePaymentLinkResponse.model_validate(response)

    async def get(self, *, link_id: str) -> GetPaymentLinkResponse:
        """Async version of :meth:`PaymentLinkResource.get`."""
        app_id = self._config.get_app_id_or_raise()
        api_key = self._config.get_api_key_or_raise()
        headers = build_auth_header(api_key)

        response = await self._http.request(
            "GET",
            f"/v3/payment-link/{link_id}/",
            params={"app_id": app_id},
            headers=headers,
        )
        return GetPaymentLinkResponse.model_validate(response)

    async def update(
        self, *, link_id: str, description: str
    ) -> UpdatePaymentLinkResponse:
        """Async version of :meth:`PaymentLinkResource.update`."""
        app_id = self._config.get_app_id_or_raise()
        api_key = self._config.get_api_key_or_raise()

        payload: Dict[str, Any] = {
            "app_id": app_id,
            "description": description,
        }
        headers = build_auth_header(api_key)

        response = await self._http.request(
            "PUT",
            f"/v3/payment-link/{link_id}/",
            json=payload,
            headers=headers,
        )
        return UpdatePaymentLinkResponse.model_validate(response)

    async def delete(self, *, link_id: str) -> DeletePaymentLinkResponse:
        """Async version of :meth:`PaymentLinkResource.delete`."""
        app_id = self._config.get_app_id_or_raise()
        api_key = self._config.get_api_key_or_raise()
        headers = build_auth_header(api_key)

        response = await self._http.request(
            "DELETE",
            f"/v3/payment-link/{link_id}/",
            params={"app_id": app_id},
            headers=headers,
        )
        return DeletePaymentLinkResponse.model_validate(response)
