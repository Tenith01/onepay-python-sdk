"""Items resource — CRUD for line items."""

from __future__ import annotations

import builtins  # noqa: TCH003
from typing import TYPE_CHECKING, Any

from onepay._auth import build_auth_header
from onepay.models.item import (
    CreateItemResponse,
    DeleteItemResponse,
    ItemData,
    ListItemsResponse,
    UpdateItemResponse,
)

if TYPE_CHECKING:
    from onepay._config import OnePayConfig
    from onepay._http import AsyncHttpClient, SyncHttpClient


class ItemResource:
    """Sync item operations."""

    def __init__(self, http: SyncHttpClient, config: OnePayConfig) -> None:
        self._http = http
        self._config = config

    def create(
        self,
        *,
        name: str,
        description: str,
        price: float,
        currency: str,
        image_url: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> CreateItemResponse:
        """Create a new item.

        Args:
            name: Product or service name.
            description: Short description of the item.
            price: Unit price (e.g., ``1400.99``).
            currency: Currency code (e.g., ``"LKR"``).
            image_url: Optional public URL of a product image.
            metadata: Optional key-value pairs for internal cataloguing.

        Returns:
            :class:`CreateItemResponse` with the new ``item_id``.
        """
        payload: dict[str, Any] = {
            "app_id": self._config.get_app_id_or_raise(),
            "name": name,
            "description": description,
            "price": price,
            "currency": currency,
        }
        if image_url is not None:
            payload["image_url"] = image_url
        if metadata is not None:
            payload["metadata"] = metadata

        headers = build_auth_header(self._config.get_app_token_or_raise())
        response = self._http.request("POST", "/v3/item/", json=payload, headers=headers)
        return CreateItemResponse.model_validate(response)

    def list(self) -> list[ItemData]:
        """List all items under your App ID.

        Returns:
            List of :class:`ItemData` objects.
        """
        app_id = self._config.get_app_id_or_raise()
        headers = build_auth_header(self._config.get_app_token_or_raise())
        response = self._http.request(
            "GET", "/v3/item/", params={"app_id": app_id}, headers=headers
        )
        parsed = ListItemsResponse.model_validate(response)
        return parsed.data or []

    def update(
        self,
        *,
        item_id: str,
        name: str | None = None,
        price: float | None = None,
        description: str | None = None,
        image_url: str | None = None,
        metadata: builtins.list[dict[str, Any]] | None = None,
    ) -> UpdateItemResponse:
        """Update an existing item. Only provided fields are changed.

        Args:
            item_id: The item to update.
            name: Updated name.
            price: Updated price.
            description: Updated description.
            image_url: Updated image URL.
            metadata: Updated metadata (replaces existing).

        Returns:
            :class:`UpdateItemResponse`.
        """
        payload: dict[str, Any] = {
            "app_id": self._config.get_app_id_or_raise(),
        }
        if name is not None:
            payload["name"] = name
        if price is not None:
            payload["price"] = price
        if description is not None:
            payload["description"] = description
        if image_url is not None:
            payload["image_url"] = image_url
        if metadata is not None:
            payload["metadata"] = metadata

        headers = build_auth_header(self._config.get_app_token_or_raise())
        response = self._http.request("PUT", f"/v3/item/{item_id}/", json=payload, headers=headers)
        return UpdateItemResponse.model_validate(response)

    def delete(self, *, item_id: str) -> DeleteItemResponse:
        """Permanently delete an item.

        Items attached to completed transactions cannot be deleted.

        Args:
            item_id: The item to delete.

        Returns:
            :class:`DeleteItemResponse`.
        """
        app_id = self._config.get_app_id_or_raise()
        headers = build_auth_header(self._config.get_app_token_or_raise())
        response = self._http.request(
            "DELETE",
            f"/v3/item/{item_id}/",
            params={"app_id": app_id},
            headers=headers,
        )
        return DeleteItemResponse.model_validate(response)


class AsyncItemResource:
    """Async item operations."""

    def __init__(self, http: AsyncHttpClient, config: OnePayConfig) -> None:
        self._http = http
        self._config = config

    async def create(
        self,
        *,
        name: str,
        description: str,
        price: float,
        currency: str,
        image_url: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> CreateItemResponse:
        """Async version of :meth:`ItemResource.create`."""
        payload: dict[str, Any] = {
            "app_id": self._config.get_app_id_or_raise(),
            "name": name,
            "description": description,
            "price": price,
            "currency": currency,
        }
        if image_url is not None:
            payload["image_url"] = image_url
        if metadata is not None:
            payload["metadata"] = metadata

        headers = build_auth_header(self._config.get_app_token_or_raise())
        response = await self._http.request("POST", "/v3/item/", json=payload, headers=headers)
        return CreateItemResponse.model_validate(response)

    async def list(self) -> list[ItemData]:
        """Async version of :meth:`ItemResource.list`."""
        app_id = self._config.get_app_id_or_raise()
        headers = build_auth_header(self._config.get_app_token_or_raise())
        response = await self._http.request(
            "GET", "/v3/item/", params={"app_id": app_id}, headers=headers
        )
        parsed = ListItemsResponse.model_validate(response)
        return parsed.data or []

    async def update(
        self,
        *,
        item_id: str,
        name: str | None = None,
        price: float | None = None,
        description: str | None = None,
        image_url: str | None = None,
        metadata: builtins.list[dict[str, Any]] | None = None,
    ) -> UpdateItemResponse:
        """Async version of :meth:`ItemResource.update`."""
        payload: dict[str, Any] = {
            "app_id": self._config.get_app_id_or_raise(),
        }
        if name is not None:
            payload["name"] = name
        if price is not None:
            payload["price"] = price
        if description is not None:
            payload["description"] = description
        if image_url is not None:
            payload["image_url"] = image_url
        if metadata is not None:
            payload["metadata"] = metadata

        headers = build_auth_header(self._config.get_app_token_or_raise())
        response = await self._http.request(
            "PUT", f"/v3/item/{item_id}/", json=payload, headers=headers
        )
        return UpdateItemResponse.model_validate(response)

    async def delete(self, *, item_id: str) -> DeleteItemResponse:
        """Async version of :meth:`ItemResource.delete`."""
        app_id = self._config.get_app_id_or_raise()
        headers = build_auth_header(self._config.get_app_token_or_raise())
        response = await self._http.request(
            "DELETE",
            f"/v3/item/{item_id}/",
            params={"app_id": app_id},
            headers=headers,
        )
        return DeleteItemResponse.model_validate(response)
