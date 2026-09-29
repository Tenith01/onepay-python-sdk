# OnePay Python SDK

The official Python SDK for the [OnePay](https://onepay.lk) payment gateway. Built for Python backend developers with full type safety, sync and async support, and a clean Pythonic API.

[![PyPI version](https://img.shields.io/pypi/v/onepay)](https://pypi.org/project/onepay/)
[![Python versions](https://img.shields.io/pypi/pyversions/onepay)](https://pypi.org/project/onepay/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Installation

```bash
# pip
pip install onepay

# uv
uv add onepay

# conda (after conda-forge feedstock is available)
conda install -c conda-forge onepay
```

## Quick Start

```python
from onepay import OnePay

client = OnePay(
    app_id="YOUR_APP_ID",
    hash_salt="YOUR_HASH_SALT",
    app_token="YOUR_APP_TOKEN",
)

# Create a checkout session
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

# Redirect your customer to this URL
print(result.redirect_url)

# Store this for later verification
print(result.ipg_transaction_id)
```

## Features

- **Checkout & Payments** : Create transactions, verify payment status
- **Items Management** : CRUD for line items attached to transactions
- **Payment Links** : Generate shareable payment URLs
- **Card on File** : Customer management, card tokenization, automated charging
- **Refunds** : Full and partial refund support
- **Payouts** : Transaction lookup and paginated settlement reports
- **Webhooks** : Framework-agnostic callback parsing
- **Subscriptions** : Experimental subscription billing support
- **Sync & Async** : Both `OnePay` and `AsyncOnePay` clients
- **Type Safe** : Full type annotations, Pydantic models, PEP 561 compliant

## Authentication

The SDK supports environment variables as fallback for credentials:

```bash
export ONEPAY_APP_ID="your_app_id"
export ONEPAY_HASH_SALT="your_hash_salt"
export ONEPAY_APP_TOKEN="your_app_token"
export ONEPAY_API_KEY="your_api_key"           # For payment links
export ONEPAY_ACCESS_TOKEN="your_access_token" # For customers/cards
```

```python
from onepay import OnePay

# Credentials auto-loaded from environment
client = OnePay()
```

## Usage Examples

### Verify Transaction Status

```python
status = client.transactions.get_status(onepay_transaction_id="WQBV118E584C83CBA50C6")
if status.data and status.data.status:
    print(f"Payment confirmed: {status.data.amount} {status.data.currency}")
```

### Item Management

```python
# Create an item
item = client.items.create(
    name="Pro Plan",
    description="Monthly subscription",
    price=2500.00,
    currency="LKR",
)
print(item.item_id)

# List all items
items = client.items.list()
```

### Payment Links

```python
link = client.payment_links.create(
    amount="5000.00",
    currency="LKR",
    reference_number="INV-001",
    customer_first_name="Kasun",
    customer_last_name="Silva",
    customer_email="kasun@example.com",
    customer_phone_number="+94771234567",
    description="Invoice #001",
    expiration_date="2026-12-31",
)
print(link.data.link_url)  # Share this URL with your customer
```

### Card on File (Automated Charging)

```python
# Create a customer and get card-entry URL
customer = client.customers.create(
    first_name="Nimal",
    last_name="Perera",
    email="nimal@example.com",
    phone_number="+94771234567",
    address="123 Colombo Rd",
    redirect_url="https://store.lk/card-saved",
)
# Redirect customer to: customer.data.redirect_url

# After customer saves their card, charge it
charge = client.cards.charge(
    customer_id="cus_907fa39a",
    token_id="tok_12345678",
    amount="1000.00",
    currency="LKR",
)
```

### Refunds

```python
# Full refund
refund = client.refunds.create(
    onepay_transaction_id="ONP2026072800001",
    refund_reason="REQUESTED_BY_CUSTOMER",
    refund_note="Customer requested refund",
)

# Partial refund
refund = client.refunds.create(
    onepay_transaction_id="ONP2026072800001",
    refund_reason="OTHER",
    is_partially=True,
    amount=500.00,
)
```

### Payout Reconciliation

```python
# Single transaction lookup
payout = client.payouts.get_transaction(onepay_transaction_id="WQBV118E584C83CBA50C6")
print(f"Settled: LKR {payout.data.settlement_amount}")

# Iterate all transactions in a date range (auto-paginated)
for txn in client.payouts.list_transactions(
    start_date="2026-04-01",
    end_date="2026-04-28",
):
    print(f"{txn.onepay_transaction_id}: {txn.settlement_amount}")
```

### Webhook Handling

```python
from onepay import Webhook

# In your webhook endpoint (framework-agnostic)
event = Webhook.parse(request.body)
if event.is_success:
    print(f"Payment {event.transaction_id} succeeded!")
```

### Async Usage

```python
from onepay import AsyncOnePay


async def process_payment():
    async with AsyncOnePay(
        app_id="...",
        hash_salt="...",
        app_token="...",
    ) as client:
        # Create a checkout session
        result = await client.checkout.create(
            amount=1000.00,
            currency="LKR",
            reference="ORDER-123",
            customer_first_name="Amila",
            customer_last_name="Perera",
            customer_phone_number="+94771234567",
            customer_email="amila@store.lk",
            transaction_redirect_url="https://store.lk/thank-you",
        )

        # Async iterator for paginated endpoints
        async for txn in client.payouts.list_transactions(
            start_date="2026-04-01",
            end_date="2026-04-28",
        ):
            print(f"{txn.onepay_transaction_id}: {txn.settlement_amount}")

        return result.redirect_url
```

## Error Handling

```python
from onepay import OnePay, OnePayError, AuthenticationError, RateLimitError

client = OnePay(...)

try:
    result = client.checkout.create(...)
except AuthenticationError:
    print("Check your credentials")
except RateLimitError as e:
    print(f"Rate limited. Retry after: {e.retry_after}s")
except OnePayError as e:
    print(f"OnePay error: {e.message}")
```

## Configuration

| Parameter      | Type  | Default                   | Description                           |
| -------------- | ----- | ------------------------- | ------------------------------------- |
| `app_id`       | str   | `""`                      | Your OnePay App ID                    |
| `hash_salt`    | str   | `""`                      | Your hash salt (secret)               |
| `app_token`    | str   | `""`                      | App token for Items, Refunds, Payouts |
| `api_key`      | str   | `""`                      | Company API key for Payment Links     |
| `access_token` | str   | `""`                      | Access token for Customers/Cards      |
| `base_url`     | str   | `"https://api.onepay.lk"` | API base URL                          |
| `timeout`      | float | `30.0`                    | Request timeout in seconds            |
| `max_retries`  | int   | `3`                       | Max retry attempts for 429/5xx errors |
| `debug`        | bool  | `False`                   | Enable debug logging                  |

## Development

```bash
# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Type checking
mypy src/onepay --strict

# Linting
ruff check src/ tests/
```

## License

MIT : see [LICENSE](LICENSE).
