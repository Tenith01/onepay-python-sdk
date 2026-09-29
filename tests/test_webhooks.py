"""Tests for webhook parsing."""

from __future__ import annotations

import json
from typing import Any

import pytest

from onepay import Webhook
from onepay.webhook import WebhookEvent


class TestWebhookParsing:
    """Tests for the Webhook.parse() utility."""

    def test_parse_dict(self, mock_webhook_payload: dict[str, Any]) -> None:
        """Should parse a dict payload."""
        event = Webhook.parse(mock_webhook_payload)
        assert isinstance(event, WebhookEvent)
        assert event.transaction_id == "WQBV118E584C83CBA50C6"
        assert event.status == 1
        assert event.status_message == "SUCCESS"
        assert event.is_success is True

    def test_parse_string(self, mock_webhook_payload: dict[str, Any]) -> None:
        """Should parse a JSON string payload."""
        event = Webhook.parse(json.dumps(mock_webhook_payload))
        assert event.is_success is True

    def test_parse_bytes(self, mock_webhook_payload: dict[str, Any]) -> None:
        """Should parse a bytes payload."""
        event = Webhook.parse(json.dumps(mock_webhook_payload).encode())
        assert event.is_success is True

    def test_failed_payment(self) -> None:
        """Failed payment webhook should return is_success=False."""
        payload = {
            "transaction_id": "TXN_FAIL",
            "status": 0,
            "status_message": "FAIL",
            "additional_data": "",
        }
        event = Webhook.parse(payload)
        assert event.is_success is False

    def test_invalid_json_raises(self) -> None:
        """Invalid JSON should raise ValueError."""
        with pytest.raises(ValueError, match="Invalid JSON"):
            Webhook.parse("not valid json {{{")

    def test_invalid_type_raises(self) -> None:
        """Non-string/bytes/dict should raise ValueError."""
        with pytest.raises(ValueError, match="Expected str, bytes, or dict"):
            Webhook.parse(12345)  # type: ignore
