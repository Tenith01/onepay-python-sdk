"""Tests for cards resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import httpx
import pytest
import respx
from onepay.models.card import (
    CardData,
    ChargeCardResponse,
    DeleteCardResponse,
    GetCardResponse,
)

if TYPE_CHECKING:
    from onepay import OnePay


@pytest.fixture
def mock_card_list_response() -> dict[str, Any]:
    return {
        "status": 200,
        "message": "Cards fetched successfully",
        "data": [
            {
                "token_id": "tok_12345678",
                "masked_number": "411111XXXXXX1111",
                "card_type": "Visa",
                "is_active": True,
            }
        ],
    }


@pytest.fixture
def mock_card_get_response() -> dict[str, Any]:
    return {
        "status": 200,
        "message": "Card fetched successfully",
        "data": {
            "token_id": "tok_12345678",
            "masked_number": "411111XXXXXX1111",
            "card_type": "Visa",
            "is_active": True,
        },
    }


@pytest.fixture
def mock_card_delete_response() -> dict[str, Any]:
    return {"status": 200, "message": "Card deleted successfully"}


@pytest.fixture
def mock_card_charge_response() -> dict[str, Any]:
    return {
        "status": 200,
        "message": "Charge successful",
        "data": {"transaction_id": "TXN_999", "status": True},
    }


class TestCardResource:
    @respx.mock
    def test_list_cards(self, client: OnePay, mock_card_list_response: dict[str, Any]) -> None:
        respx.get(
            "https://api.onepay.lk/v3/customers/cus_123/cards/?app_id=test_app_id_12345"
        ).mock(return_value=httpx.Response(200, json=mock_card_list_response))

        result = client.cards.list(customer_id="cus_123")
        assert len(result) == 1
        assert isinstance(result[0], CardData)
        assert result[0].token_id == "tok_12345678"

    @respx.mock
    def test_get_card(self, client: OnePay, mock_card_get_response: dict[str, Any]) -> None:
        respx.get(
            "https://api.onepay.lk/v3/customers/cus_123/cards/tok_12345678/?app_id=test_app_id_12345"
        ).mock(return_value=httpx.Response(200, json=mock_card_get_response))

        result = client.cards.get(customer_id="cus_123", token_id="tok_12345678")
        assert isinstance(result, GetCardResponse)
        assert result.data is not None
        assert result.data.token_id == "tok_12345678"

    @respx.mock
    def test_delete_card(self, client: OnePay, mock_card_delete_response: dict[str, Any]) -> None:
        respx.delete(
            "https://api.onepay.lk/v3/customers/cus_123/cards/tok_12345678/?app_id=test_app_id_12345"
        ).mock(return_value=httpx.Response(200, json=mock_card_delete_response))

        result = client.cards.delete(customer_id="cus_123", token_id="tok_12345678")
        assert isinstance(result, DeleteCardResponse)
        assert result.message == "Card deleted successfully"

    @respx.mock
    def test_charge_card(self, client: OnePay, mock_card_charge_response: dict[str, Any]) -> None:
        respx.post("https://api.onepay.lk/v3/customers/cus_123/payments/").mock(
            return_value=httpx.Response(200, json=mock_card_charge_response)
        )

        result = client.cards.charge(
            customer_id="cus_123", token_id="tok_12345678", amount="1000.00", currency="LKR"
        )
        assert isinstance(result, ChargeCardResponse)
        assert result.data is not None
        assert result.data.transaction_id == "TXN_999"
