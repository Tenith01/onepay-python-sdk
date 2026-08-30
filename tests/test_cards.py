"""Tests for cards resource."""

from __future__ import annotations

import httpx
import pytest
import respx

from onepay import OnePay
from onepay.models.card import (
    CardData,
    ChargeTokenResponse,
    DeleteCardResponse,
    GetCardResponse,
)


@pytest.fixture
def mock_card_list_response():
    return {
        "status": 200,
        "message": "Cards fetched successfully",
        "data": [
            {
                "token_id": "tok_12345678",
                "masked_pan": "411111XXXXXX1111",
                "card_brand": "Visa",
                "is_active": True
            }
        ],
    }

@pytest.fixture
def mock_card_get_response():
    return {
        "status": 200,
        "message": "Card fetched successfully",
        "data": {
            "token_id": "tok_12345678",
            "masked_pan": "411111XXXXXX1111",
            "card_brand": "Visa",
            "is_active": True
        },
    }

@pytest.fixture
def mock_card_delete_response():
    return {
        "status": 200,
        "message": "Card deleted successfully",
        "data": {
            "token_id": "tok_12345678"
        },
    }

@pytest.fixture
def mock_card_charge_response():
    return {
        "status": 200,
        "message": "Charge successful",
        "data": {
            "ipg_transaction_id": "TXN_999",
            "status": "SUCCESS"
        },
    }


class TestCardResource:
    @respx.mock
    def test_list_cards(self, client, mock_card_list_response):
        respx.get("https://api.onepay.lk/v3/customers/cus_123/cards/?app_id=test_app_id_12345").mock(
            return_value=httpx.Response(200, json=mock_card_list_response)
        )

        result = client.cards.list(customer_id="cus_123")
        assert len(result) == 1
        assert isinstance(result[0], CardData)
        assert result[0].token_id == "tok_12345678"

    @respx.mock
    def test_get_card(self, client, mock_card_get_response):
        respx.get("https://api.onepay.lk/v3/customers/cus_123/cards/tok_12345678/?app_id=test_app_id_12345").mock(
            return_value=httpx.Response(200, json=mock_card_get_response)
        )

        result = client.cards.get(customer_id="cus_123", token_id="tok_12345678")
        assert isinstance(result, GetCardResponse)
        assert result.data.token_id == "tok_12345678"

    @respx.mock
    def test_delete_card(self, client, mock_card_delete_response):
        respx.delete("https://api.onepay.lk/v3/customers/cus_123/cards/tok_12345678/?app_id=test_app_id_12345").mock(
            return_value=httpx.Response(200, json=mock_card_delete_response)
        )

        result = client.cards.delete(customer_id="cus_123", token_id="tok_12345678")
        assert isinstance(result, DeleteCardResponse)
        assert result.data.token_id == "tok_12345678"

    @respx.mock
    def test_charge_card(self, client, mock_card_charge_response):
        respx.post("https://api.onepay.lk/v3/customers/cus_123/payments/").mock(
            return_value=httpx.Response(200, json=mock_card_charge_response)
        )

        result = client.cards.charge(
            customer_id="cus_123",
            token_id="tok_12345678",
            amount=1000.00,
            currency="LKR",
            reference="REF-001"
        )
        assert isinstance(result, ChargeTokenResponse)
        assert result.data.ipg_transaction_id == "TXN_999"
