"""Customers resource — manage customer profiles for Card on File."""

from __future__ import annotations

import builtins  # noqa: TCH003
from typing import TYPE_CHECKING, Any

from onepay._auth import build_auth_header
from onepay.models.customer import (
    CreateCustomerResponse,
    CustomerData,
    CustomerTransactionData,
    GetCustomerResponse,
    ListCustomersResponse,
    ListCustomerTransactionsResponse,
)

if TYPE_CHECKING:
    from onepay._config import OnePayConfig
    from onepay._http import AsyncHttpClient, SyncHttpClient


class CustomerResource:
    """Sync customer operations."""

    def __init__(self, http: SyncHttpClient, config: OnePayConfig) -> None:
        self._http = http
        self._config = config

    def create(
        self,
        *,
        first_name: str,
        last_name: str,
        email: str,
        phone_number: str,
        address: str,
        redirect_url: str,
    ) -> CreateCustomerResponse:
        """Create a new customer and get a card-entry redirect URL.

        Args:
            first_name: Customer's first name.
            last_name: Customer's last name.
            email: Customer's email address.
            phone_number: Phone with country code (e.g., ``"+94771234567"``).
            address: Customer's billing or physical address.
            redirect_url: URL to redirect after card entry.

        Returns:
            :class:`CreateCustomerResponse` with ``customer_id`` and ``redirect_url``.
        """
        payload: dict[str, Any] = {
            "app_id": self._config.get_app_id_or_raise(),
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone_number": phone_number,
            "address": address,
            "redirect_url": redirect_url,
        }

        headers = build_auth_header(self._config.get_access_token_or_raise())
        response = self._http.request("POST", "/v3/customers/", json=payload, headers=headers)
        return CreateCustomerResponse.model_validate(response)

    def request_token(self, *, customer_id: str, redirect_url: str) -> CreateCustomerResponse:
        """Request a new card token for an existing customer.

        Args:
            customer_id: Existing customer ID (e.g., ``"cus_907fa39a"``).
            redirect_url: URL to redirect after card entry.

        Returns:
            :class:`CreateCustomerResponse` with a new card-entry ``redirect_url``.
        """
        payload: dict[str, Any] = {
            "app_id": self._config.get_app_id_or_raise(),
            "customer_id": customer_id,
            "redirect_url": redirect_url,
        }

        headers = build_auth_header(self._config.get_access_token_or_raise())
        response = self._http.request("POST", "/v3/customers/", json=payload, headers=headers)
        return CreateCustomerResponse.model_validate(response)

    def list(self) -> list[CustomerData]:
        """List all customers.

        Returns:
            List of :class:`CustomerData` objects.
        """
        headers = build_auth_header(self._config.get_access_token_or_raise())
        response = self._http.request("GET", "/v3/customers/", headers=headers)
        parsed = ListCustomersResponse.model_validate(response)
        return parsed.data or []

    def get(self, *, customer_id: str) -> GetCustomerResponse:
        """Get detailed customer info including cards and transactions.

        Args:
            customer_id: Unique customer identifier.

        Returns:
            :class:`GetCustomerResponse` with full customer details.
        """
        app_id = self._config.get_app_id_or_raise()
        headers = build_auth_header(self._config.get_access_token_or_raise())

        response = self._http.request(
            "GET",
            f"/v3/customers/{customer_id}/",
            params={"app_id": app_id},
            headers=headers,
        )
        return GetCustomerResponse.model_validate(response)

    def list_transactions(self, *, customer_id: str) -> builtins.list[CustomerTransactionData]:
        """Get a customer's full billing history.

        Args:
            customer_id: Unique customer identifier.

        Returns:
            List of :class:`CustomerTransactionData` objects.
        """
        app_id = self._config.get_app_id_or_raise()
        headers = build_auth_header(self._config.get_access_token_or_raise())

        response = self._http.request(
            "GET",
            f"/v3/customers/{customer_id}/transactions/",
            params={"app_id": app_id},
            headers=headers,
        )
        parsed = ListCustomerTransactionsResponse.model_validate(response)
        return parsed.data or []


class AsyncCustomerResource:
    """Async customer operations."""

    def __init__(self, http: AsyncHttpClient, config: OnePayConfig) -> None:
        self._http = http
        self._config = config

    async def create(
        self,
        *,
        first_name: str,
        last_name: str,
        email: str,
        phone_number: str,
        address: str,
        redirect_url: str,
    ) -> CreateCustomerResponse:
        """Async version of :meth:`CustomerResource.create`."""
        payload: dict[str, Any] = {
            "app_id": self._config.get_app_id_or_raise(),
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone_number": phone_number,
            "address": address,
            "redirect_url": redirect_url,
        }

        headers = build_auth_header(self._config.get_access_token_or_raise())
        response = await self._http.request("POST", "/v3/customers/", json=payload, headers=headers)
        return CreateCustomerResponse.model_validate(response)

    async def request_token(self, *, customer_id: str, redirect_url: str) -> CreateCustomerResponse:
        """Async version of :meth:`CustomerResource.request_token`."""
        payload: dict[str, Any] = {
            "app_id": self._config.get_app_id_or_raise(),
            "customer_id": customer_id,
            "redirect_url": redirect_url,
        }

        headers = build_auth_header(self._config.get_access_token_or_raise())
        response = await self._http.request("POST", "/v3/customers/", json=payload, headers=headers)
        return CreateCustomerResponse.model_validate(response)

    async def list(self) -> builtins.list[CustomerData]:
        """Async version of :meth:`CustomerResource.list`."""
        headers = build_auth_header(self._config.get_access_token_or_raise())
        response = await self._http.request("GET", "/v3/customers/", headers=headers)
        parsed = ListCustomersResponse.model_validate(response)
        return parsed.data or []

    async def get(self, *, customer_id: str) -> GetCustomerResponse:
        """Async version of :meth:`CustomerResource.get`."""
        app_id = self._config.get_app_id_or_raise()
        headers = build_auth_header(self._config.get_access_token_or_raise())

        response = await self._http.request(
            "GET",
            f"/v3/customers/{customer_id}/",
            params={"app_id": app_id},
            headers=headers,
        )
        return GetCustomerResponse.model_validate(response)

    async def list_transactions(
        self, *, customer_id: str
    ) -> builtins.list[CustomerTransactionData]:
        """Async version of :meth:`CustomerResource.list_transactions`."""
        app_id = self._config.get_app_id_or_raise()
        headers = build_auth_header(self._config.get_access_token_or_raise())

        response = await self._http.request(
            "GET",
            f"/v3/customers/{customer_id}/transactions/",
            params={"app_id": app_id},
            headers=headers,
        )
        parsed = ListCustomerTransactionsResponse.model_validate(response)
        return parsed.data or []
