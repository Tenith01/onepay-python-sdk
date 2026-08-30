"""Tests for checkout resource."""

from __future__ import annotations

import httpx
import pytest
import respx

from onepay import OnePay
from onepay.models.checkout import CheckoutResponse


class TestCheckoutResource:
    """Tests for the checkout.create() method."""

    @respx.mock
    def test_create_checkout_success(self, client, mock_checkout_response):
        """Successful checkout should return redirect URL and transaction ID."""
        respx.post("https://api.onepay.lk/v3/checkout/link/").mock(
            return_value=httpx.Response(200, json=mock_checkout_response)
        )

        result = client.checkout.create(
            amount=1000.00,
            currency="LKR",
            reference="ORDER-123",
            customer_first_name="John",
            customer_last_name="Doe",
            customer_phone_number="+94771234567",
            customer_email="john@example.com",
            transaction_redirect_url="https://store.lk/thank-you",
        )

        assert isinstance(result, CheckoutResponse)
        assert result.redirect_url == "https://gateway.onepay.lk/pay/abc123"
        assert result.ipg_transaction_id == "WQBV118E584C83CBA50C6"

    @respx.mock
    def test_create_checkout_includes_hash_in_payload(self, client):
        """The request payload should include the auto-generated hash."""
        route = respx.post("https://api.onepay.lk/v3/checkout/link/").mock(
            return_value=httpx.Response(200, json={
                "status": 200,
                "data": {
                    "gateway": {"redirect_url": "https://gateway.onepay.lk/pay/x"},
                    "ipg_transaction_id": "TXN1",
                },
            })
        )

        client.checkout.create(
            amount=500.00,
            currency="LKR",
            reference="REF-1",
            customer_first_name="A",
            customer_last_name="B",
            customer_phone_number="+94770000000",
            customer_email="a@b.com",
            transaction_redirect_url="https://example.com",
        )

        # Verify the request was sent with a hash
        request = route.calls.last.request
        body = request.content.decode()
        assert '"hash"' in body
        assert '"app_id"' in body

    @respx.mock
    def test_create_checkout_with_optional_fields(self, client, mock_checkout_response):
        """Optional fields like additional_data and items should be included."""
        respx.post("https://api.onepay.lk/v3/checkout/link/").mock(
            return_value=httpx.Response(200, json=mock_checkout_response)
        )

        result = client.checkout.create(
            amount=1000.00,
            currency="LKR",
            reference="ORDER-456",
            customer_first_name="Jane",
            customer_last_name="Doe",
            customer_phone_number="+94770000000",
            customer_email="jane@example.com",
            transaction_redirect_url="https://store.lk/thank-you",
            additional_data="extra_info",
            items=["item_1", "item_2"],
        )

        assert result.redirect_url is not None

    def test_create_checkout_missing_app_id(self):
        """Should raise ValueError when app_id is not configured."""
        client = OnePay(hash_salt="salt", app_token="token")
        with pytest.raises(ValueError, match="app_id"):
            client.checkout.create(
                amount=100.00,
                currency="LKR",
                reference="REF",
                customer_first_name="A",
                customer_last_name="B",
                customer_phone_number="+94770000000",
                customer_email="a@b.com",
                transaction_redirect_url="https://example.com",
            )
