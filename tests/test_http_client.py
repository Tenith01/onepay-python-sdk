"""Tests for HTTP client error handling."""

from __future__ import annotations

import httpx
import pytest
import respx

from onepay.exceptions import (
    AuthenticationError,
    InvalidRequestError,
    RateLimitError,
)


class TestHttpClientErrors:
    """Tests for error parsing and exception raising."""

    @respx.mock
    def test_401_raises_authentication_error(self, client):
        """HTTP 401 should raise AuthenticationError."""
        respx.post("https://api.onepay.lk/v3/checkout/link/").mock(
            return_value=httpx.Response(401, json={
                "message": "Invalid authorization"
            })
        )

        with pytest.raises(AuthenticationError) as exc_info:
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

        assert exc_info.value.status_code == 401

    @respx.mock
    def test_400_raises_invalid_request_error(self, client):
        """HTTP 400 should raise InvalidRequestError."""
        respx.post("https://api.onepay.lk/v3/checkout/link/").mock(
            return_value=httpx.Response(400, json={
                "message": "Invalid request body"
            })
        )

        with pytest.raises(InvalidRequestError) as exc_info:
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

        assert exc_info.value.status_code == 400

    @respx.mock
    def test_429_raises_rate_limit_error(self, client):
        """HTTP 429 should raise RateLimitError."""
        respx.post("https://api.onepay.lk/v3/checkout/link/").mock(
            return_value=httpx.Response(429, json={
                "message": "Too many requests"
            })
        )

        with pytest.raises(RateLimitError) as exc_info:
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

        assert exc_info.value.status_code == 429
