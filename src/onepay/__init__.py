"""OnePay Python SDK — Official SDK for the OnePay payment gateway.

Quick start::

    from onepay import OnePay

    client = OnePay(
        app_id="YOUR_APP_ID",
        hash_salt="YOUR_HASH_SALT",
        app_token="YOUR_APP_TOKEN",
    )

    result = client.checkout.create(
        amount=1000.00,
        currency="LKR",
        reference="ORDER-123",
        customer_first_name="Amila",
        customer_last_name="Perera",
        customer_phone_number="+94771234567",
        customer_email="amila@store.lk",
        transaction_redirect_url="https://store.lk/thank-you",
    )
    print(result.redirect_url)

For async usage::

    from onepay import AsyncOnePay

    client = AsyncOnePay(...)
    result = await client.checkout.create(...)
"""

from __future__ import annotations

from onepay._version import __version__
from onepay.client import AsyncOnePay, OnePay
from onepay._auth import generate_hash
from onepay.webhook import Webhook, WebhookEvent

# Exceptions
from onepay.exceptions import (
    APIError,
    AuthenticationError,
    InvalidAmountError,
    InvalidAppIdError,
    InvalidCurrencyError,
    InvalidRequestError,
    NetworkError,
    OnePayError,
    RateLimitError,
    RefundNotAllowedError,
)

# Enums
from onepay.models.enums import (
    Currency,
    PaymentStatus,
    RefundReason,
    SubscriptionInterval,
)

__all__ = [
    # Version
    "__version__",
    # Clients
    "OnePay",
    "AsyncOnePay",
    # Utilities
    "generate_hash",
    "Webhook",
    "WebhookEvent",
    # Exceptions
    "OnePayError",
    "APIError",
    "AuthenticationError",
    "InvalidRequestError",
    "InvalidAppIdError",
    "InvalidAmountError",
    "InvalidCurrencyError",
    "RefundNotAllowedError",
    "RateLimitError",
    "NetworkError",
    # Enums
    "Currency",
    "PaymentStatus",
    "RefundReason",
    "SubscriptionInterval",
]
