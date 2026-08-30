# Changelog

All notable changes to the OnePay Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.1.1] - 2026-08-30

### Added
- Initial release of the OnePay Python SDK
- **Checkout** — `client.checkout.create()` for payment session creation with automatic SHA-256 hash generation
- **Transaction Status** — `client.transactions.get_status()` for payment verification
- **Items** — Full CRUD via `client.items.create/list/update/delete()`
- **Payment Links** — Full CRUD via `client.payment_links.create/get/update/delete()`
- **Customers** — `client.customers.create/list/get/request_token/list_transactions()`
- **Cards** — `client.cards.list/get/delete/charge()`
- **Refunds** — `client.refunds.create()` with full and partial refund support
- **Payouts** — `client.payouts.get_transaction()` and auto-paginating `list_transactions()`
- **Subscriptions** — Experimental `client.subscriptions.create()`
- **Webhooks** — `Webhook.parse()` for framework-agnostic callback handling
- Sync (`OnePay`) and async (`AsyncOnePay`) clients
- Full type annotations with PEP 561 `py.typed` marker
- Pydantic v2 models for all request/response types
- Exception hierarchy: `OnePayError`, `AuthenticationError`, `InvalidRequestError`, `RateLimitError`, `NetworkError`
- Automatic retry with exponential backoff for 429 and 5xx errors
- Environment variable fallback for all credentials
- Context manager support (`with OnePay(...) as client:`)
