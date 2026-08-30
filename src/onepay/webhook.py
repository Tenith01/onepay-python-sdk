"""Webhook payload parsing for OnePay server-to-server callbacks.

Provides framework-agnostic utilities for parsing and validating
webhook payloads received from OnePay.
"""

from __future__ import annotations

import json
from typing import Any, Dict, Optional, Union

from pydantic import BaseModel, Field


class WebhookEvent(BaseModel):
    """Parsed webhook callback payload from OnePay.

    OnePay sends this as a POST request to your configured callback URL
    when a transaction completes.
    """

    transaction_id: str = Field(
        ..., description="The OnePay transaction ID"
    )
    status: int = Field(
        ..., description="Numeric status (1 = SUCCESS)"
    )
    status_message: str = Field(
        ..., description="Status description (e.g. SUCCESS)"
    )
    additional_data: str = Field(
        "", description="Any additional data from transaction creation"
    )

    @property
    def is_success(self) -> bool:
        """Whether the payment was successful."""
        return self.status == 1 and self.status_message.upper() == "SUCCESS"


class Webhook:
    """Utility class for parsing webhook payloads.

    Example::

        from onepay import Webhook

        # In your webhook endpoint handler:
        event = Webhook.parse(request.body)
        if event.is_success:
            mark_order_paid(event.transaction_id)
    """

    @staticmethod
    def parse(payload: Union[str, bytes, Dict[str, Any]]) -> WebhookEvent:
        """Parse a webhook payload into a :class:`WebhookEvent`.

        Args:
            payload: The raw request body as a string, bytes, or
                already-parsed dictionary.

        Returns:
            :class:`WebhookEvent` with parsed fields.

        Raises:
            ValueError: If the payload cannot be parsed.
        """
        if isinstance(payload, (str, bytes)):
            try:
                data = json.loads(payload)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON in webhook payload: {exc}") from exc
        elif isinstance(payload, dict):
            data = payload
        else:
            raise ValueError(
                f"Expected str, bytes, or dict, got {type(payload).__name__}"
            )

        return WebhookEvent.model_validate(data)
