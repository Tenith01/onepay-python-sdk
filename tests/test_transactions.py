"""Tests for transaction status resource."""

from __future__ import annotations

import httpx
import respx

from onepay.models.transaction import TransactionStatusResponse


class TestTransactionResource:
    """Tests for the transactions.get_status() method."""

    @respx.mock
    def test_get_status_success(self, client, mock_transaction_status_response):
        """Successful status check should return parsed transaction data."""
        respx.post("https://api.onepay.lk/v3/transaction/status/").mock(
            return_value=httpx.Response(200, json=mock_transaction_status_response)
        )

        result = client.transactions.get_status(
            onepay_transaction_id="WQBV118E584C83CBA50C6"
        )

        assert isinstance(result, TransactionStatusResponse)
        assert result.status is True
        assert result.data is not None
        assert result.data.ipg_transaction_id == "WQBV118E584C83CBA50C6"
        assert result.data.amount == "1000.00"
        assert result.data.currency == "LKR"

    @respx.mock
    def test_get_status_failed_payment(self, client):
        """Failed payment should return status=False."""
        respx.post("https://api.onepay.lk/v3/transaction/status/").mock(
            return_value=httpx.Response(200, json={
                "status": False,
                "data": {
                    "status": False,
                    "ipg_transaction_id": "TXN_FAILED",
                },
            })
        )

        result = client.transactions.get_status(
            onepay_transaction_id="TXN_FAILED"
        )

        assert result.status is False
