"""Tests for customers resource."""

from __future__ import annotations

import httpx
import pytest
import respx

from onepay.models.customer import (
    CreateCustomerResponse,
    CustomerData,
    CustomerTransactionData,
    GetCustomerResponse,
)


@pytest.fixture
def mock_customer_create_response():
    return {
        "status": 200,
        "message": "Customer created successfully",
        "data": {
            "customer_id": "cus_907fa39a",
            "redirect_url": "https://gateway.onepay.lk/add-card/123"
        },
    }

@pytest.fixture
def mock_customer_request_token_response():
    return {
        "status": 200,
        "message": "Token requested successfully",
        "data": {
            "customer_id": "cus_907fa39a",
            "redirect_url": "https://gateway.onepay.lk/add-card/456"
        },
    }

@pytest.fixture
def mock_customer_list_response():
    return {
        "status": 200,
        "message": "Customers fetched successfully",
        "data": [
            {
                "customer_id": "cus_907fa39a",
                "first_name": "Nimal",
                "last_name": "Perera",
                "email": "nimal@example.com",
                "phone_number": "+94771234567"
            }
        ],
    }

@pytest.fixture
def mock_customer_get_response():
    return {
        "status": 200,
        "message": "Customer fetched successfully",
        "data": {
            "customer_id": "cus_907fa39a",
            "first_name": "Nimal",
            "last_name": "Perera",
            "email": "nimal@example.com",
            "phone_number": "+94771234567"
        },
    }

@pytest.fixture
def mock_customer_list_transactions_response():
    return {
        "status": 200,
        "message": "Transactions fetched successfully",
        "data": [
            {
                "transaction_id": "TXN_123",
                "amount": "1500.00",
                "currency": "LKR",
                "status": True,
                "paid_on": "2026-08-30 14:00:00"
            }
        ],
    }


class TestCustomerResource:
    @respx.mock
    def test_create_customer(self, client, mock_customer_create_response):
        respx.post("https://api.onepay.lk/v3/customers/").mock(
            return_value=httpx.Response(200, json=mock_customer_create_response)
        )

        result = client.customers.create(
            first_name="Nimal",
            last_name="Perera",
            email="nimal@example.com",
            phone_number="+94771234567",
            address="123 Colombo Rd",
            redirect_url="https://store.lk/card-saved"
        )
        assert isinstance(result, CreateCustomerResponse)
        assert result.data.customer_id == "cus_907fa39a"

    @respx.mock
    def test_request_token(self, client, mock_customer_request_token_response):
        respx.post("https://api.onepay.lk/v3/customers/").mock(
            return_value=httpx.Response(200, json=mock_customer_request_token_response)
        )

        result = client.customers.request_token(
            customer_id="cus_907fa39a",
            redirect_url="https://store.lk/card-saved"
        )
        assert isinstance(result, CreateCustomerResponse)
        assert result.data.redirect_url == "https://gateway.onepay.lk/add-card/456"

    @respx.mock
    def test_list_customers(self, client, mock_customer_list_response):
        respx.get("https://api.onepay.lk/v3/customers/").mock(
            return_value=httpx.Response(200, json=mock_customer_list_response)
        )

        result = client.customers.list()
        assert len(result) == 1
        assert isinstance(result[0], CustomerData)
        assert result[0].customer_id == "cus_907fa39a"

    @respx.mock
    def test_get_customer(self, client, mock_customer_get_response):
        respx.get("https://api.onepay.lk/v3/customers/cus_907fa39a/?app_id=test_app_id_12345").mock(
            return_value=httpx.Response(200, json=mock_customer_get_response)
        )

        result = client.customers.get(customer_id="cus_907fa39a")
        assert isinstance(result, GetCustomerResponse)
        assert result.data.customer_id == "cus_907fa39a"

    @respx.mock
    def test_list_transactions(self, client, mock_customer_list_transactions_response):
        respx.get("https://api.onepay.lk/v3/customers/cus_907fa39a/transactions/?app_id=test_app_id_12345").mock(
            return_value=httpx.Response(200, json=mock_customer_list_transactions_response)
        )

        result = client.customers.list_transactions(customer_id="cus_907fa39a")
        assert len(result) == 1
        assert isinstance(result[0], CustomerTransactionData)
        assert result[0].transaction_id == "TXN_123"
