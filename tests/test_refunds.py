"""Tests for refunds resource."""

from __future__ import annotations

import httpx
import pytest
import respx

from onepay.models.refund import RefundResponse


class TestRefundResource:
    """Tests for the refunds.create() method."""

    @respx.mock
    def test_full_refund(self, client, mock_refund_response):
        """Full refund should succeed."""
        respx.post("https://api.onepay.lk/v3/transaction/refund/").mock(
            return_value=httpx.Response(200, json=mock_refund_response)
        )

        result = client.refunds.create(
            onepay_transaction_id="ONP2026072800001",
            refund_reason="REQUESTED_BY_CUSTOMER",
            refund_note="Customer requested a full refund",
        )

        assert isinstance(result, RefundResponse)
        assert result.data is not None
        assert result.data.status == "refund-initiated"
        assert result.data.is_partially is False

    @respx.mock
    def test_partial_refund(self, client):
        """Partial refund with amount should succeed."""
        respx.post("https://api.onepay.lk/v3/transaction/refund/").mock(
            return_value=httpx.Response(200, json={
                "status": 200,
                "message": "Successfully initiated refund request",
                "data": {
                    "ipg_transaction_id": "ONP2026072800001",
                    "refund_id": 43,
                    "status": "refund-initiated",
                    "is_partially": True,
                    "requested_amount": "500.00",
                    "refund_reason": "OTHER",
                },
            })
        )

        result = client.refunds.create(
            onepay_transaction_id="ONP2026072800001",
            refund_reason="OTHER",
            is_partially=True,
            amount=500.00,
            refund_note="Partial refund for cancelled item",
        )

        assert result.data is not None
        assert result.data.is_partially is True

    def test_partial_refund_without_amount_raises(self, client):
        """Partial refund without amount should raise ValueError."""
        with pytest.raises(ValueError, match="amount is required"):
            client.refunds.create(
                onepay_transaction_id="ONP2026072800001",
                refund_reason="OTHER",
                is_partially=True,
                # amount is missing
            )
