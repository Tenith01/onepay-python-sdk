"""Tests for items resource."""

from __future__ import annotations

import respx
import httpx


class TestItemResource:
    """Tests for item CRUD operations."""

    @respx.mock
    def test_create_item(self, client, mock_create_item_response):
        """Item creation should return the new item_id."""
        respx.post("https://api.onepay.lk/v3/item/").mock(
            return_value=httpx.Response(200, json=mock_create_item_response)
        )

        result = client.items.create(
            name="Widget",
            description="A nice widget",
            price=1400.99,
            currency="LKR",
        )

        assert result.item_id == "item_abc123"

    @respx.mock
    def test_list_items(self, client, mock_list_items_response):
        """Item listing should return a list of ItemData."""
        respx.get("https://api.onepay.lk/v3/item/").mock(
            return_value=httpx.Response(200, json=mock_list_items_response)
        )

        items = client.items.list()

        assert len(items) == 1
        assert items[0].item_id == "item_abc123"
        assert items[0].name == "Widget"

    @respx.mock
    def test_update_item(self, client):
        """Item update should succeed."""
        respx.put("https://api.onepay.lk/v3/item/item_abc123/").mock(
            return_value=httpx.Response(200, json={
                "status": 200,
                "message": "Item updated",
                "data": {"item_id": "item_abc123"},
            })
        )

        result = client.items.update(item_id="item_abc123", name="Updated Widget")
        assert result.status == 200

    @respx.mock
    def test_delete_item(self, client):
        """Item deletion should succeed."""
        respx.delete("https://api.onepay.lk/v3/item/item_abc123/").mock(
            return_value=httpx.Response(200, json={
                "status": 200,
                "message": "Item deleted",
            })
        )

        result = client.items.delete(item_id="item_abc123")
        assert result.status == 200
