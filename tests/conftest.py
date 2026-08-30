"""Shared test fixtures for the OnePay SDK test suite."""

from __future__ import annotations

import pytest

from onepay import OnePay, AsyncOnePay


@pytest.fixture
def config_kwargs():
    """Common configuration keyword arguments for test clients."""
    return {
        "app_id": "test_app_id_12345",
        "hash_salt": "test_hash_salt_67890",
        "app_token": "test_app_token_abcde",
        "api_key": "test_api_key_fghij",
        "access_token": "test_access_token_klmno",
        "base_url": "https://api.onepay.lk",
        "timeout": 10.0,
        "max_retries": 0,  # No retries in tests for speed
        "debug": False,
    }


@pytest.fixture
def client(config_kwargs):
    """Create a sync OnePay client for testing."""
    c = OnePay(**config_kwargs)
    yield c
    c.close()


@pytest.fixture
def async_client(config_kwargs):
    """Create an async OnePay client for testing."""
    return AsyncOnePay(**config_kwargs)


@pytest.fixture
def mock_checkout_response():
    """Mock successful checkout API response."""
    return {
        "status": 200,
        "data": {
            "gateway": {
                "redirect_url": "https://gateway.onepay.lk/pay/abc123"
            },
            "ipg_transaction_id": "WQBV118E584C83CBA50C6",
        },
    }


@pytest.fixture
def mock_transaction_status_response():
    """Mock successful transaction status response."""
    return {
        "status": True,
        "data": {
            "status": True,
            "ipg_transaction_id": "WQBV118E584C83CBA50C6",
            "amount": "1000.00",
            "currency": "LKR",
            "paid_on": "2026-08-30 12:30:00",
        },
    }


@pytest.fixture
def mock_create_item_response():
    """Mock successful item creation response."""
    return {
        "status": 200,
        "message": "Item created successfully",
        "data": {"item_id": "item_abc123"},
    }


@pytest.fixture
def mock_list_items_response():
    """Mock item list response."""
    return {
        "status": 200,
        "message": "Items fetched successfully",
        "data": [
            {
                "item_id": "item_abc123",
                "name": "Widget",
                "description": "A nice widget",
                "price": "1400.99",
                "currency": "LKR",
                "image_url": None,
                "is_deleted": False,
                "metadata": [],
            }
        ],
    }


@pytest.fixture
def mock_refund_response():
    """Mock successful refund response."""
    return {
        "status": 200,
        "message": "Successfully initiated refund request",
        "data": {
            "ipg_transaction_id": "ONP2026072800001",
            "refund_id": 42,
            "status": "refund-initiated",
            "is_partially": False,
            "requested_amount": "1000.00",
            "refund_reason": "REQUESTED_BY_CUSTOMER",
        },
    }


@pytest.fixture
def mock_payout_transaction_response():
    """Mock payout transaction lookup response."""
    return {
        "status": 200,
        "message": "Transaction fetched successfully",
        "data": {
            "onepay_transaction_id": "WQBV118E584C83CBA50C6",
            "order_id": "ORDER-123",
            "currency": "LKR",
            "net_amount": "5.00",
            "commission_rate": "2.50",
            "commission_amount": "0.13",
            "settlement_amount": 4.87,
            "settlement_date": "2026-04-28 15:37",
        },
    }


@pytest.fixture
def mock_webhook_payload():
    """Mock webhook callback payload."""
    return {
        "transaction_id": "WQBV118E584C83CBA50C6",
        "status": 1,
        "status_message": "SUCCESS",
        "additional_data": "",
    }
