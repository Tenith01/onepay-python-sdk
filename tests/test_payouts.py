"""Tests for payouts resource."""

from __future__ import annotations

import httpx
import pytest
import respx

from onepay import OnePay
from onepay.models.payout import (
    GetPayoutTransactionResponse,
    ListPayoutTransactionsResponse,
    PayoutTransactionData,
)


@pytest.fixture
def mock_payout_list_response():
    return {
        "status": 200,
        "message": "Transactions fetched successfully",
        "data": {
            "total_records": 1,
            "total_pages": 1,
            "current_page": 1,
            "records": [
                {
                    "onepay_transaction_id": "TXN_777",
                    "order_id": "ORD-777",
                    "currency": "LKR",
                    "net_amount": "1000.00",
                    "commission_rate": "2.50",
                    "commission_amount": "25.00",
                    "settlement_amount": 975.00,
                    "settlement_date": "2026-08-30 12:00"
                }
            ]
        },
    }

class TestPayoutResource:
    @respx.mock
    def test_get_transaction(self, client, mock_payout_transaction_response):
        respx.get("https://api.onepay.lk/v3/payout/transaction/?onepay_transaction_id=WQBV118E584C83CBA50C6").mock(
            return_value=httpx.Response(200, json=mock_payout_transaction_response)
        )

        result = client.payouts.get_transaction(onepay_transaction_id="WQBV118E584C83CBA50C6")
        assert isinstance(result, GetPayoutTransactionResponse)
        assert result.data.onepay_transaction_id == "WQBV118E584C83CBA50C6"

    @respx.mock
    def test_list_transactions_page(self, client, mock_payout_list_response):
        respx.get("https://api.onepay.lk/v3/payout/transactions/?start_date=2026-08-01&end_date=2026-08-31&page=1&page_size=20").mock(
            return_value=httpx.Response(200, json=mock_payout_list_response)
        )

        result = client.payouts.list_transactions_page(
            start_date="2026-08-01",
            end_date="2026-08-31",
            page=1,
            page_size=20
        )
        assert isinstance(result, ListPayoutTransactionsResponse)
        assert result.data.total_records == 1
        assert len(result.data.records) == 1
        assert result.data.records[0].onepay_transaction_id == "TXN_777"

    @respx.mock
    def test_list_transactions_iterator(self, client, mock_payout_list_response):
        respx.get("https://api.onepay.lk/v3/payout/transactions/?start_date=2026-08-01&end_date=2026-08-31&page=1&page_size=20").mock(
            return_value=httpx.Response(200, json=mock_payout_list_response)
        )
        # Assuming the second page returns empty to stop iteration, wait, total_pages is 1.

        iterator = client.payouts.list_transactions(
            start_date="2026-08-01",
            end_date="2026-08-31",
            page_size=20
        )
        
        items = list(iterator)
        assert len(items) == 1
        assert isinstance(items[0], PayoutTransactionData)
        assert items[0].onepay_transaction_id == "TXN_777"
