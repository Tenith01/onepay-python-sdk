"""Tests for payment links resource."""

from __future__ import annotations

import httpx
import pytest
import respx

from onepay.models.payment_link import (
    CreatePaymentLinkResponse,
    DeletePaymentLinkResponse,
    GetPaymentLinkResponse,
    UpdatePaymentLinkResponse,
)


@pytest.fixture
def mock_payment_link_create_response():
    return {
        "status": 200,
        "message": "Payment link created successfully",
        "data": {
            "link_id": "8IT20WK7",
            "link_url": "https://gateway.onepay.lk/payment-link/8IT20WK7"
        },
    }

@pytest.fixture
def mock_payment_link_get_response():
    return {
        "status": 200,
        "message": "Payment link fetched successfully",
        "data": {
            "link_id": "8IT20WK7",
            "amount": "5000.00",
            "currency": "LKR",
            "reference_number": "INV-001",
            "description": "Invoice #001",
            "status": "active"
        },
    }

@pytest.fixture
def mock_payment_link_update_response():
    return {
        "status": 200,
        "message": "Payment link updated successfully",
        "data": {
            "link_id": "8IT20WK7",
            "description": "Updated desc"
        },
    }

@pytest.fixture
def mock_payment_link_delete_response():
    return {
        "status": 200,
        "message": "Payment link deleted successfully"
    }


class TestPaymentLinkResource:
    @respx.mock
    def test_create_payment_link(self, client, mock_payment_link_create_response):
        respx.post("https://api.onepay.lk/v3/payment-link/?app_id=test_app_id_12345").mock(
            return_value=httpx.Response(200, json=mock_payment_link_create_response)
        )

        result = client.payment_links.create(
            amount=5000.00,
            currency="LKR",
            reference_number="INV-001",
            customer_first_name="Kasun",
            customer_last_name="Silva",
            customer_email="kasun@example.com",
            customer_phone_number="+94771234567",
            description="Invoice #001",
            expiration_date="2026-12-31"
        )

        assert isinstance(result, CreatePaymentLinkResponse)
        assert result.data.link_id == "8IT20WK7"
        assert result.data.link_url == "https://gateway.onepay.lk/payment-link/8IT20WK7"

    @respx.mock
    def test_get_payment_link(self, client, mock_payment_link_get_response):
        respx.get("https://api.onepay.lk/v3/payment-link/8IT20WK7/?app_id=test_app_id_12345").mock(
            return_value=httpx.Response(200, json=mock_payment_link_get_response)
        )

        result = client.payment_links.get(link_id="8IT20WK7")
        assert isinstance(result, GetPaymentLinkResponse)
        assert result.data.link_id == "8IT20WK7"

    @respx.mock
    def test_update_payment_link(self, client, mock_payment_link_update_response):
        respx.put("https://api.onepay.lk/v3/payment-link/8IT20WK7/").mock(
            return_value=httpx.Response(200, json=mock_payment_link_update_response)
        )

        result = client.payment_links.update(link_id="8IT20WK7", description="Updated desc")
        assert isinstance(result, UpdatePaymentLinkResponse)
        assert result.data.description == "Updated desc"

    @respx.mock
    def test_delete_payment_link(self, client, mock_payment_link_delete_response):
        respx.delete("https://api.onepay.lk/v3/payment-link/8IT20WK7/?app_id=test_app_id_12345").mock(
            return_value=httpx.Response(200, json=mock_payment_link_delete_response)
        )

        result = client.payment_links.delete(link_id="8IT20WK7")
        assert isinstance(result, DeletePaymentLinkResponse)
        assert result.message == "Payment link deleted successfully"
