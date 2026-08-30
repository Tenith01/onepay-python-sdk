# OnePay Documentation

# Table of Contents

- **API Documentation**
  - [https://docs.onepay.lk/api-documentation](https://docs.onepay.lk/api-documentation)
  - [https://docs.onepay.lk/api-documentation/authentication](https://docs.onepay.lk/api-documentation/authentication)
  - [https://docs.onepay.lk/api-documentation/error-handling](https://docs.onepay.lk/api-documentation/error-handling)
  - [https://docs.onepay.lk/api-documentation/currencies](https://docs.onepay.lk/api-documentation/currencies)
  - [https://docs.onepay.lk/api-documentation/payment-api#create-transaction](https://docs.onepay.lk/api-documentation/payment-api#create-transaction)
  - [https://docs.onepay.lk/api-documentation/items-management](https://docs.onepay.lk/api-documentation/items-management)
  - [https://docs.onepay.lk/api-documentation/payment-link](https://docs.onepay.lk/api-documentation/payment-link)
  - [https://docs.onepay.lk/api-documentation/customer-tokenizer](https://docs.onepay.lk/api-documentation/customer-tokenizer)
  - [https://docs.onepay.lk/api-documentation/refund](https://docs.onepay.lk/api-documentation/refund)
  - [https://docs.onepay.lk/api-documentation/payouts](https://docs.onepay.lk/api-documentation/payouts)
- **Testing**
  - [https://docs.onepay.lk/testing/test-cards](https://docs.onepay.lk/testing/test-cards)
- **SDKs and Plugins**
  - [https://docs.onepay.lk/api-documentation/onepay-js](https://docs.onepay.lk/api-documentation/onepay-js)
  - [https://docs.onepay.lk/plugins/javascript-sdk](https://docs.onepay.lk/plugins/javascript-sdk)
  - [https://docs.onepay.lk/plugins/wordpress](https://docs.onepay.lk/plugins/wordpress)
  - [https://docs.onepay.lk/plugins/shopify](https://docs.onepay.lk/plugins/shopify)
  - [https://docs.onepay.lk/plugins/whmcs](https://docs.onepay.lk/plugins/whmcs)
  - [https://docs.onepay.lk/plugins/zoho](https://docs.onepay.lk/plugins/zoho)
- **Guides**
  - [https://docs.onepay.lk/guide/getting-started](https://docs.onepay.lk/guide/getting-started)
  - [https://docs.onepay.lk/guide/policy-samples](https://docs.onepay.lk/guide/policy-samples)
  - [https://docs.onepay.lk/guide/resolution-templates](https://docs.onepay.lk/guide/resolution-templates)
  - [https://docs.onepay.lk/user-guide](https://docs.onepay.lk/user-guide)
- **Blog / Technical Articles**
  - [https://docs.onepay.lk/blogs/card-on-file](https://docs.onepay.lk/blogs/card-on-file)
  - [https://docs.onepay.lk/blogs/onepay-google-pay-press-release](https://docs.onepay.lk/blogs/onepay-google-pay-press-release)
  - [https://docs.onepay.lk/blogs/wellness-tourism-report](https://docs.onepay.lk/blogs/wellness-tourism-report)
  - [https://docs.onepay.lk/blogs/onepay-unified-checkout](https://docs.onepay.lk/blogs/onepay-unified-checkout)
  - [https://docs.onepay.lk/blogs/onepay-orchestration](https://docs.onepay.lk/blogs/onepay-orchestration)
  - [https://docs.onepay.lk/blogs/multi-currency-payments](https://docs.onepay.lk/blogs/multi-currency-payments)
  - [https://docs.onepay.lk/blogs/hotels-deposits](https://docs.onepay.lk/blogs/hotels-deposits)
  - [https://docs.onepay.lk/blogs/do-not-honour](https://docs.onepay.lk/blogs/do-not-honour)
  - [https://docs.onepay.lk/blogs/learning-center](https://docs.onepay.lk/blogs/learning-center)

---

# API Documentation

## OnePay REST API Docs

**Category**: API Documentation  
**Source URL**: https://docs.onepay.lk/api-documentation

# OnePay API Introduction

The OnePay API is built on REST principles. It uses predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes and authentication.

| Step | Action |
| --- | --- |
| **Get credentials** | App ID + Hash Salt |
| **Create transaction** | POST to /v3/checkout/link/ |
| **Redirect customer** | Same-window redirect |
| **Receive callback** | Verify via /v3/transaction/status/ |

#### Secure by design

Every request is signed with a SHA-256 hash, ensuring transaction integrity end to end. OnePay is ISO 27001 certified, the first payment gateway in Sri Lanka to hold this certification.

#### REST API

Standard HTTP verbs, predictable URLs, and JSON responses. Integrate in any language, PHP, Node.js, Python, Java, .NET, and more.

#### Sandbox environment

Test your integration in our sandbox before going live. Sandbox credentials are available from your OnePay merchant dashboard.

#### Multi-currency

Process payments in LKR and USD. Supports Visa, Mastercard, and all major card networks accepted in Sri Lanka.

### Base URLs

Live

```
https://api.onepay.lk
```

## Core Concepts

All Onepay APIs follow standard REST principles, using predictable resource oriented URLs and standard HTTP response codes.

### Response Formats

All API responses are returned in standard JSON format. Success responses typically include the requested data, while errors include a clear status message.

### API versioning

The current API version is `v3`. All endpoints are prefixed with `/v3/`. Breaking changes will be released under a new version prefix, and older versions will be supported with advance notice.

### Rate limiting

API requests are rate limited per App ID. If you exceed the limit, you will receive an HTTP `429 Too Many Requests` response. Implement exponential backoff in your retry logic. Contact support to request a higher rate limit for your use case.

---

## API Authentication

**Category**: API Documentation  
**Source URL**: https://docs.onepay.lk/api-documentation/authentication

# Authentication

OnePay uses a dual-credential authentication model. Every API request carries your App ID in the request body, and every sensitive request is signed with a SHA-256 HMAC hash generated server-side using your Hash Salt.

Your Hash Salt is a secret key. Never expose it in client-side JavaScript, mobile app binaries, or public repositories. All hash generation must happen on your backend server.

### Your credentials

Log in to your OnePay merchant dashboard to find your App ID and Hash Salt. Each business account has a separate set of live and sandbox credentials.

| CREDENTIAL | WHERE TO FIND | USAGE |
| --- | --- | --- |
| `app_id` | Merchant dashboard  API Keys | Included in every request body. Identifies your merchant account. |
| `hash_salt` | Merchant dashboard  API Keys | Used to generate the HMAC hash server-side. Never sent directly in requests. |

### Hash generation

For payment creation requests, you must include a SHA-256 hash that signs the key transaction parameters. This prevents tampering and validates that the request originated from your server.

```
SHA256( app_id + currency + amount + HASH_SALT )
```

Concatenate values as plain strings with no separators. The `amount` must match exactly what you send in the request body (e.g. "100.00").

---

## API Error Handling & HTTP Codes

**Category**: API Documentation  
**Source URL**: https://docs.onepay.lk/api-documentation/error-handling

# Errors

OnePay uses conventional HTTP response codes. Codes in the 2xx range indicate success. Codes in the 4xx range indicate a client error.

| HTTP CODE | MEANING |
| --- | --- |
| 200 | The checkout link has been successfully created |
| 400 | The request body is invalid due to one or more of the following errors. Detailed error information will be included in the response:   * Invalid app id * Invalid amount * Invalid app state * Currency type not available for the app |
| 401 | The Authorization header is either missing, contains an invalid application token, or includes an incorrect hash |
| 429 | Too many requests have been made within a one second period |

---

## Payment Methods & Currencies

**Category**: API Documentation  
**Source URL**: https://docs.onepay.lk/api-documentation/currencies

# Payment Options & Supported Currencies

Accept payments from customers worldwide using cards, mobile wallets, and internet banking. Multi-currency support is built in, so you can get paid in the currencies your customers already use.

## Payment Methods

### Debit & Credit Cards

Card Payment

### Mobile Wallets

Mobile Payment

## Supported Currencies

OnePay supports **10 currencies**, enabling your business to collect payments from customers across the world. Settlement to your bank account is always in **LKR**. Foreign currency amounts are converted at the applicable FX rate at the time of the transaction.

This is especially useful for travel businesses, hotels, and tour operators. Multi-currency acceptance works well for any business serving international visitors to Sri Lanka. Contact your Relationship Officer to confirm which currencies are enabled on your merchant account.

Settlement always happens in LKR. When a customer pays in a foreign currency, the amount is converted to LKR using the FX rate at the time of the transaction. For refunds on foreign currency transactions, the FX rate used is the one applicable on the refund date, not the original transaction date.

| Currency Code | Currency Name |
| --- | --- |
| **LKR** | Sri Lankan Rupee |
| **USD** | US Dollar |
| **GBP** | British Pound |
| **EUR** | Euro |
| **AUD** | Australian Dollar |
| **JPY** | Japanese Yen |
| **INR** | Indian Rupee |
| **CHF** | Swiss Franc |
| **CAD** | Canadian Dollar |
| **SGD** | Singapore Dollar |

**This is especially useful for travel businesses, hotels, and tour operators.** Multi-currency acceptance works well for any business serving international visitors to Sri Lanka. Contact your Relationship Officer to confirm which currencies are enabled on your merchant account.

**This is especially useful for travel businesses, hotels, and tour operators.** Multi-currency acceptance works well for any business serving international visitors to Sri Lanka. Contact your Relationship Officer to confirm which currencies are enabled on your merchant account.

Please note that, as per guidelines issued by **CBSL**, Sri Lankan-based businesses are **not permitted to accept USD payments** from domestic customers. It is important to comply with these regulations to avoid any potential penalties.

For more information, please refer to the official CBSL notice:<https://www.cbsl.gov.lk/sites/default/files/cbslweb_documents/press/pr/press_20260212_foreign_currency_transactions_between_residents_of_srilanka_e.pdf>

---

## Payment API Reference

**Category**: API Documentation  
**Source URL**: https://docs.onepay.lk/api-documentation/payment-api#create-transaction

# Payment API — Redirection

The Redirection Payment API is the most widely adopted integration method. Your server creates a checkout session, and the customer is redirected to the secure OnePay hosted payment page, no new tab, same window. After payment, the customer is returned to your `transaction_redirect_url`.

This is a same-window redirect flow. The payment page loads in the current browser tab — no pop-ups, no new tabs. This design passes strict browser pop-up blocking policies and improves conversion rates.

| Step | Action |
| --- | --- |
| **Get credentials** | App ID + Hash Salt |
| **Create transaction** | POST to /v3/checkout/link/ |
| **Redirect customer** | Use redirect\_url in response |
| **Receive callback** | Verify via status API |

---

### Base URL

All API requests should be made to the following base URL:

https://api.onepay.lk

### Onepay API hash generation tutorial

To secure your payment requests, Onepay requires a SHA-256 hash in the request body. This hash ensures that the transaction details have not been tampered with.

HASH FORMULA

SHA256(app\_id + currency + amount + HASH\_SALT)

Never share your **HASH\_SALT** in client-side code. This should be kept securely on your server.

### 1. Create Transaction

Creates a payment request and returns a redirect URL to the Onepay Payment Gateway. You can associate items with the transaction if needed.

POSThttps://api.onepay.lk/v3/checkout/link/

REQUEST BODY

| PARAMETER | TYPE | DESCRIPTION |
| --- | --- | --- |
| `app_id` required | string | Your unique application identifier from the merchant dashboard. |
| `amount` required | number | The transaction amount, e.g. `100.00`. Use two decimal places. |
| `currency` required | string | Three-letter ISO currency code. [View Supported Currencies→](/api-documentation/currencies) |
| `hash` required | string | SHA-256 hash of `app_id + currency + amount + HASH_SALT`. Generate server-side. |
| `reference` required | string | Your internal order or reference ID. Used to correlate transactions in your system. |
| `customer_first_name` required | string | Customer's first name. |
| `customer_last_name` required | string | Customer's last name. |
| `customer_phone_number` required | string | Customer's phone number in E.164 format, e.g. `+94771234567`. |
| `customer_email` required | string | Customer's email address. Used for payment receipts. |
| `transaction_redirect_url` required | string | The URL the customer is redirected to after payment. Must be HTTPS. |
| `additionalData` optional | string | Any additional metadata you want to associate with the transaction. |
| `items` optional | array | Array of item IDs created via the Items API. Attaches itemized billing details to the transaction. |

### How to Initiate a Postman Request

Follow the steps below to initiate a request using Postman. A detailed walkthrough video will be added shortly for your reference.

### 2. Transaction Status

After a customer completes (or cancels) payment, verify the outcome by querying the transaction status endpoint. Always verify server-side do not rely solely on URL parameters returned to your redirect page.

Endpoint

POSThttps://api.onepay.lk/v3/transaction/status/

REQUEST BODY

| PARAMETER | TYPE | DESCRIPTION |
| --- | --- | --- |
| `app_id` required | string | Your unique application identifier. |
| `onepay_transaction_id` required | string | The transaction ID returned in the `ipg_transaction_id` field when the transaction was created. |

RESPONSE FIELDS — 200 OK

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `status` | boolean | `true` if the payment was successful. |
| `ipg_transaction_id` | string | OnePay's internal transaction identifier. |
| `amount` | number | The amount charged. |
| `currency` | string | Currency of the transaction. |
| `paid_on` | string | Timestamp of payment confirmation in `YYYY-MM-DD HH:mm:ss` format. |

### 3. Onepay webhook callback setup

Set up your system to receive transaction status updates:

* Update your callback URL in the APP section of the Onepay portal
* Your endpoint should be configured to accept **POST** requests with JSON payloads
* After transaction completion, Onepay will send a callback with transaction details

SAMPLE CALLBACK PAYLOAD

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `transaction_id` | string | The provided transaction ID (e.g. `WQBV118E584C83CBA50C6`). |
| `status` | number | A numeric representation of the status (e.g. `1`). |
| `status_message` | string | A message describing the status (e.g. `SUCCESS`). |
| `additional_data` | string | Any additional data provided during the transaction creation. |

callback-response.json

```
{

"transaction_id": "WQBV118E584C83CBA50C6",

"status": 1,

"status_message": "SUCCESS",

"additional_data": ""

}
```

Use this callback data for logging, verification, and updating transaction status in your system.

---

## Items Management API

**Category**: API Documentation  
**Source URL**: https://docs.onepay.lk/api-documentation/items-management

# Items Management

Create and manage product or service line items. Attach items to a payment transaction via the `items` array to give customers a clear, itemized view of exactly what they are purchasing, only available for custom API integrations.

Up to two items will be added to the payment success receipt generated by OnePay. This communicates a clear purchase picture to your customers and builds trust at the point of payment.

#### E-commerce

Show product names and prices on the checkout receipt. Customers see exactly what they paid for, reducing disputes and chargebacks.

#### Subscriptions & SaaS

Attach the plan name and billing period as line items so customers recognise charges on their bank statement.

#### Invoicing

Map invoice line items to OnePay items for an itemized receipt that matches your invoice, useful for B2B reconciliation.

#### Custom metadata

Store internal attributes (SKU, brand, RAM, batch ID) in the `metadata` array for your own reporting without affecting the customer-facing display.

### Create Item

POSThttps://api.onepay.lk/v3/item/

PARAMETER

| PARAMETER | TYPE | DESCRIPTION |
| --- | --- | --- |
| `name` required | string | Product or service name. |
| `description` required | string | Short description of the item. |
| `price` required | number | Unit price, e.g. `1400.99`. |
| `currency` required | string | `LKR` or `USD`. |
| `image_url` optional | string | Public URL of a product image shown on checkout. |
| `metadata` optional | object | Arbitrary key-value pairs for internal cataloguing (e.g. brand, SKU, RAM). |

RESPONSE PARAMETERS

| Parameter | Type | Description |
| --- | --- | --- |
| `status` | Number | Status code of the response (e.g., 200 for success) |
| `message` | String | Response message indicating the result of the operation |
| `data` | Object | Contains the response data |
| `data.item_id` | String | Unique identifier of the created item |

### Get items

GEThttps://api.onepay.lk/v3/item/?app\_id={app\_id}

Returns all items created under your App ID. Pass `app_id` as a query parameter no request body required.

QUERY PARAMETERS

| PARAMETER | TYPE | DESCRIPTION |
| --- | --- | --- |
| `app_id` required | string | Your application identifier. |

RESPONSE PARAMETERS — 200 OK

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `status` | number | Status code of the response (e.g. `200` for success). |
| `message` | string | Response message indicating the result of the operation. |
| `data` | array | Array of item objects. |
| `data[].item_id` | string | Unique identifier for the item. |
| `data[].name` | string | Name of the item. |
| `data[].description` | string | Description of the item. |
| `data[].price` | string | Price of the item. |
| `data[].currency` | string | Currency code for the price. |
| `data[].image_url` | string | URL of the item's image. |
| `data[].is_deleted` | boolean | Indicates if the item has been deleted. |
| `data[].metadata` | array | Array of metadata objects for the item. |
| `data[].metadata[].key` | string | Key of the metadata property. |
| `data[].metadata[].value` | string | Value of the metadata property. |
| `data[].metadata[].is_deleted` | boolean | Indicates if this metadata property has been deleted. |

### Update item

PUThttps://api.onepay.lk/v3/item/{item\_id}/

Update any field on an existing item. Pass only the fields you want to change all other fields retain their current values.

REQUEST BODY

| PARAMETER | TYPE | DESCRIPTION |
| --- | --- | --- |
| `app_id` required | string | Your application identifier. |
| `name` optional | string | Updated item name. |
| `price` optional | number | Updated unit price. |
| `description` optional | string | Updated description. |
| `image_url` optional | string | Updated product image URL. |
| `metadata` optional | array | Updated metadata array. Replaces the existing metadata entirely. |

RESPONSE PARAMETERS

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `status` | number | Status code of the response (e.g. `200` for success). |
| `message` | string | Response message indicating the result of the operation. |
| `data` | object | Contains the response data. |
| `data.item_id` | string | Unique identifier of the updated item. |

### Delete Item

DELETEhttps://api.onepay.lk/v3/item/{item\_id}/?app\_id={app\_id}

Permanently removes an item record. Items already attached to completed transactions cannot be deleted.

QUERY PARAMETERS

| PARAMETER | TYPE | DESCRIPTION |
| --- | --- | --- |
| `app_id` required | string | Your application identifier. |

RESPONSE PARAMETERS

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `status` | number | Status code of the response (e.g. `200` for success). |
| `message` | string | Response message indicating the result of the operation. |

---

## Payment Link API Reference

**Category**: API Documentation  
**Source URL**: https://docs.onepay.lk/api-documentation/payment-link

# Payment Link API

Generate a unique, shareable payment URL programmatically. Ideal for invoicing software, accounting platforms, ERP systems, and any operational workflow where a specific, trackable payment link needs to be created and sent to a customer without redirecting them through a checkout session.

Best for: Zoho Books, QuickBooks, SAP, ERP payment collection, field sales, and any B2B workflow where the link is sent via email or SMS and paid independently.

Invoicing

#### Invoice-to-payment automation

Generate a link per invoice. When the customer pays, poll `is_complete` to auto-mark invoices as settled in your system.

ERP / Accounting

#### ERP-triggered collections

ERP raises an order → calls this API → attaches the `link_url` to the order record. Finance team tracks status directly in the ERP.

Partial Payments

#### Large-value partial collections

For amounts over LKR 100,000 or USD 100, enable `allow_partial_payment` to let customers pay in instalments. Minimum must be 30–100% of total.

Expiry Control

#### Time-limited payment requests

Set `expiration_date` to enforce payment deadlines. Expired links reject transactions, preventing late or duplicate payments.

# Authentication

Payment Link API authenticates via a Company API Key passed in the `Authorization` header, different from the hash-based signing used by the Payment API. Your App ID is passed as a URL query parameter, not in the request body.

AUTHENTICATION HEADERS

| HEADER | VALUE | REQUIRED |
| --- | --- | --- |
| `Authorization` | Your company API key | Yes |
| `Content-Type` | `application/json` | Yes |

### 1. Create payment link

POSThttps://api.onepay.lk/v3/payment-link/?app\_id={app\_id}

Create a new payment link with full customer and amount specifications. This link is immediately active upon creation until its expiration date.

QUERY PARAMETERS

| PARAMETER | TYPE | DESCRIPTION |
| --- | --- | --- |
| `app_id` required | string | Your OnePay App ID. |

### 2. Get payment link

GEThttps://api.onepay.lk/v3/payment-link/{link\_id}/?app\_id={app\_id}

Retrieve full details of a specific payment link using its 8-character link ID. Poll `is_complete` to detect when a customer has paid and trigger downstream ERP or accounting actions.

PATH & QUERY PARAMETERS

| PARAMETER | TYPE | IN | DESCRIPTION |
| --- | --- | --- | --- |
| `link_id` required | string | Path | The 8-character payment link ID (e.g. `8IT20WK7`). |
| `app_id` required | string | Query | Your OnePay App ID. |

RESPONSE PARAMETERS — 200 OK

Returns the same full object as the Create response. Key fields to watch:

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `data.is_complete` | boolean | `true` once the customer has fully paid. Use this to trigger order fulfillment in your system. |
| `data.is_delete` | boolean | `true` if the link has been soft-deleted. |
| `data.link_url` | string | The shareable payment URL. |
| `data.amount` | string | Original payment amount. |
| `data.expiration_date` | string | Link expiry date in `YYYY-MM-DD` format. |
| `data.created_at` | string | ISO 8601 creation timestamp. |
| `data.updated_at` | string | ISO 8601 last-updated timestamp. |

### 3. Update payment link

PUThttps://api.onepay.lk/v3/payment-link/{link\_id}/

Update the description of an existing payment link. Only the `description` field can be modified after creation. Amount, currency, reference number, customer details, and expiry date are all immutable to protect payment integrity.

PATH PARAMETERS

| PARAMETER | TYPE | IN | DESCRIPTION |
| --- | --- | --- | --- |
| `link_id` required | string | Path | The 8-character payment link ID. |

REQUEST BODY

| PARAMETER | TYPE | DESCRIPTION |
| --- | --- | --- |
| `app_id` required | string | Your OnePay App ID. |
| `description` required | string | The new description for the payment link. |

RESPONSE PARAMETERS — 200 OK

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `status` | number | `200` on success. |
| `message` | string | Confirmation message. |
| `data` | object | Updated link object with all current fields reflecting the new description. |

### 4. Delete payment link

DELETEhttps://api.onepay.lk/v3/payment-link/{link\_id}/?app\_id={app\_id}

Soft-deletes a payment link by setting `is_delete = true`. The link record is preserved for audit purposes but becomes inactive immediately.

A link can only be deleted if it has no successful transactions associated with it. Attempting to delete a link with completed payments returns a `400` error.

PATH & QUERY PARAMETERS

| PARAMETER | TYPE | IN | DESCRIPTION |
| --- | --- | --- | --- |
| `link_id` required | string | Path | The 8-character payment link ID. |
| `app_id` required | string | Query | Your OnePay App ID. |

RESPONSE PARAMETERS

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `status` | number | `200` on successful deletion. |
| `message` | string | Confirmation message. |

ERROR RESPONSE — 400

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `status` | number | `400` — deletion blocked. |
| `message` | string | "Cannot delete a link with successful transactions" |

---

## Card on File & Tokenizer API

**Category**: API Documentation  
**Source URL**: https://docs.onepay.lk/api-documentation/customer-tokenizer

# Card on File ( Automated Charging )

Card on File lets you save a customer's card once and charge it programmatically at any future point, without the customer needing to re-enter their details. Think of how Uber charges the passenger's card automatically at the end of every ride: the customer approves it once, and every charge after that is invisible to them.

Your customer enters their card details once and pre-approves your business to charge them in the future. You receive an encrypted token for their card. You store it. You charge it whenever you need to any amount, on demand, from your backend code alone.

### What can I use it for?

Card on File is suitable for any product or business where you have known, registered customers and want to charge them on demand without asking them to manually enter card details every time.

SaaS & subscriptions

#### Monthly subscription billing

Charge a fixed plan price on the 1st of every month. Customer approves once at signup, you handle every renewal silently. Works for Basic / Pro / Enterprise tiers.

Usage-based

#### Pay as you go

Tally API calls, data consumed, or seats used at period-end. Charge exactly what the customer owes, the token stays the same, only the amount changes each cycle.

Mobile & in-app

#### In-app purchases on demand

Multiple in-app purchases or on-demand services without redirecting users to a payment page each time. Charge instantly when the user triggers an action.

E-commerce

#### One-click repeat purchases

Returning customers checkout in one click. No card re-entry, no redirect. Especially powerful for high-frequency buyers and loyalty programs.

# How it works - 3 steps

The entire Card on File flow reduces to three things: get permission, store the token, charge when needed.

| Step | Action |
| --- | --- |
| **Get pre-approval** | Customer saves card once |
| **Store the token** | Save tok\_ ID in your DB |
| **Charge on demand** | Any amount, any time |

Step 1 — Pre-approval

Your customer creates a profile on your platform. You redirect them to the OnePay secure card-entry page. They enter their card details and **consent to future charges**. OnePay returns a `cus_` ID and a `redirect_url`.

Step 2 — Token Storage

After the customer completes card entry, call the List Cards endpoint to retrieve their `tok_` token. Store this token in your database alongside the customer record. This is the **only identifier** you need for all future charges.

Step 3 — Automated Charging

Whenever you need to charge the customer — on a schedule, on usage trigger, or on demand — make a single API call with their `customer_id`,`token_id`, and the`amount`. No customer interaction needed.

# Billing models

Once you have a token, you control exactly how and when you charge. Two patterns cover virtually every business model:

FIXED BILLING

#### Fixed price every billing cycle

Charge the exact same amount on a predictable schedule, weekly, monthly, or annually. Your system stores the next billing date and fires the charge endpoint automatically. No customer action, no payment page.

e.g. SaaS Pro plan at LKR 2,500/month cron fires on the 1st, charges`tok_XXXXX` for`"2500.00"`. Customer sees a charge on their card statement. Nothing else needed.

VARIABLE BILLING

#### Variable amount - pay as you go

Calculate the exact amount owed at the end of each billing period based on actual usage (API calls, data, seats, units). Charge precisely that amount. The token is reused, only the `amount` parameter changes each cycle.

e.g. API platform at LKR 0.50/call — tally 4,200 calls in April → charge`tok_XXXXX` for`"2100.00"`. Next month: 6,100 calls → charge `"3050.00"`. Token never changes.

# Detailed API flow

Create customer

POST

/v3/customers/

Redirect to card page

use

data.redirect\_url

Retrieve token

GET

/customers/{id}/cards/

Store token\_id

save in

your database

Charge on demand

POST

/customers/{id}/payments/

Authentication uses an **Access Token** in the `Authorization` header — different from the hash-based auth used by the Payment API. Format: `Authorization: 2c4e7c3ee0013882...`. Obtain from the merchant dashboard under API Keys.

# What is Card on File?

Tokenization is the process of replacing sensitive card data with a non-sensitive substitute, the token that has no exploitable value outside the system it was designed for.

When your customer enters their card details on the OnePay-hosted card page, those details are sent directly and securely to the card network (Visa or Mastercard) and the customer's issuing bank. The bank validates the card and returns a unique encrypted token back to OnePay. That token is what gets stored and what gets passed to your system as a `tok_` ID.

If that token were ever intercepted or leaked, it would be useless; it cannot be used to reconstruct the original card number, and it can only be charged by the specific merchant account it was issued for. This is fundamentally different from storing an encrypted card number, which could theoretically be decrypted.

**The flow in plain terms:** Customer enters card → card details go to the bank → bank issues a token → token comes back to OnePay → OnePay gives you a `tok_` ID → you store only the token ID. No card numbers ever touch your server or OnePay's database.

Card on File is currently available for **Visa** and **Mastercard** only. Other payment methods are not supported for automated charging at this time.

### Base URL

All API requests should be made to the following base URL:

https://api.onepay.lk

### Authentication

All endpoints require authentication via an Authorization header and a strictly defined Content-Type.

AUTHENTICATION HEADERS

| HEADER | VALUE | REQUIRED |
| --- | --- | --- |
| `Authorization` | Your Access Token (e.g. 2c4e7c3ee001...) | Yes |
| `Content-Type` | `application/json` | Yes |

# Customers

Manage your customer base. Each customer gets a unique `cus_` prefixed ID. Customers can have one or more saved card tokens. All endpoints require the `Authorization` access token header.

### List customers

GEThttps://api.onepay.lk/v3/customers/

Retrieves a list of all customers associated with the authenticated application. No query parameters required — authentication is via the `Authorization` header only.

RESPONSE PARAMETERS — 200 OK

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `status` | number | `200` on success. |
| `data` | array | Array of customer objects. |
| `data[].customer_id` | string | Unique customer identifier, e.g. `cus_907fa39a`. |
| `data[].first_name` | string | Customer's first name. |
| `data[].last_name` | string | Customer's last name. |
| `data[].email` | string | Customer's email address. |
| `data[].phone_number` | string | Customer's phone number. |
| `data[].address` | string | Customer's billing or physical address. |

### Get customer details

GEThttps://api.onepay.lk/v3/customers/{customer\_id}/?app\_id={app\_id}

Retrieves detailed information for a specific customer, including their associated cards and full transaction history.

PATH & QUERY PARAMETERS

| PARAMETER | TYPE | IN | DESCRIPTION |
| --- | --- | --- | --- |
| `customer_id` required | string | Path | Unique customer identifier, e.g. `cus_907fa39a`. |
| `app_id` required | string | Query | Your application identifier. |

RESPONSE PARAMETERS — 200 OK

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `data.customer_id` | string | Unique customer identifier. |
| `data.first_name` | string | Customer's first name. |
| `data.last_name` | string | Customer's last name. |
| `data.email` | string | Customer's email address. |
| `data.phone_number` | string | Customer's phone number. |
| `data.address` | string | Customer's billing or physical address. |
| `data.cards` | array | Array of saved card token objects associated with this customer. |
| `data.transactions` | array | Array of historical transaction objects for this customer. |

### Create customer and request card token

POSThttps://api.onepay.lk/v3/customers/

Creates a new customer profile and returns a `redirect_url`. Redirect the customer to that URL so they can securely enter and save their card. OnePay handles all card data, your system only ever receives back a token.

REQUEST BODY

| PARAMETER | TYPE | DESCRIPTION |
| --- | --- | --- |
| `app_id` required | string | Your application identifier. |
| `first_name` required | string | Customer's first name. |
| `last_name` required | string | Customer's last name. |
| `email` required | string | Customer's email address. |
| `phone_number` required | string | Phone number with country code, e.g. `+94771234567`. |
| `address` required | string | Customer's billing or physical address. |
| `redirect_url` required | string | The URL the customer will be redirected to after successfully adding their card. |

RESPONSE PARAMETERS — 200 OK

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `data.customer_id` | string | The newly created customer ID (e.g. `cus_907fa39a`). Store this in your database. |
| `data.redirect_url` | string | The secure OnePay-hosted URL where the customer enters their card details. |
| `data.first_name` | string | Customer's first name as stored. |
| `data.last_name` | string | Customer's last name as stored. |
| `data.email` | string | Customer's email address. |
| `data.phone_number` | string | Customer's phone number. |
| `data.address` | string | Customer's address. |

### Request token for existing customer

POSThttps://api.onepay.lk/v3/customers/

If a customer profile already exists in your system and they want to add a new card or update their payment method, pass their `customer_id`instead of full profile details. OnePay will generate a fresh card-entry redirect for that customer.

This uses the same endpoint as **Create Customer**. The difference is that you pass `customer_id`instead of the full profile fields. OnePay detects the existing profile and generates a new tokenization session for them.

REQUEST BODY

| PARAMETER | TYPE | DESCRIPTION |
| --- | --- | --- |
| `app_id` required | string | Your application identifier. |
| `customer_id` required | string | Existing customer identifier, e.g. `cus_907fa39a`. |
| `redirect_url` required | string | The URL the customer will be redirected to after adding their new card. |

RESPONSE PARAMETERS — 200 OK

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `data.customer_id` | string | The existing customer's ID, confirmed. |
| `data.redirect_url` | string | New secure card-entry URL to redirect the customer to. |

# Cards (Token)

Manage saved payment methods for your customers. Each saved card is identified by a `tok_` prefixed token ID. Use this token to charge the card raw card numbers never pass through your system.

### List customer cards

GEThttps://api.onepay.lk/v3/customers/{customer\_id}/cards/?app\_id={app\_id}

Retrieves all securely stored card tokens for a specific customer. Call this after the card-entry redirect completes to retrieve the new `token_id` and store it in your database for future charges.

PATH & QUERY PARAMETERS

| PARAMETER | TYPE | IN | DESCRIPTION |
| --- | --- | --- | --- |
| `customer_id` required | string | Path | Unique customer identifier, e.g. `cus_907fa39a`. |
| `app_id` required | string | Query | Your application identifier. |

RESPONSE PARAMETERS — 200 OK

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `data` | array | Array of card token objects. |
| `data[].token_id` | string | Secure card token identifier, e.g. `tok_12345678`. Use this for all charge requests. |
| `data[].card_type` | string | Card network, e.g. `Visa`, `Mastercard`. |
| `data[].masked_number` | string | Masked card number for display, e.g. `**** **** **** 4242`. |
| `data[].expiry` | string | Card expiry in `MM/YY` format. |
| `data[].is_deleted` | boolean | `true` if the card has been soft-deleted and cannot be used for charges. |

### Get single card

GEThttps://api.onepay.lk/v3/customers/{customer\_id}/cards/{token\_id}/?app\_id={app\_id}

Retrieves details for a specific saved card. Use the masked number, card type, and expiry to display the saved card in your UI e.g. "Visa ending in 4242, expires 12/27".

PATH & QUERY PARAMETERS

| PARAMETER | TYPE | IN | DESCRIPTION |
| --- | --- | --- | --- |
| `customer_id` required | string | Path | Unique customer identifier. |
| `token_id` required | string | Path | Secure card token, e.g. `tok_12345678`. |
| `app_id` required | string | Query | Your application identifier. |

RESPONSE PARAMETERS — 200 OK

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `data.token_id` | string | Secure card token identifier. |
| `data.card_type` | string | Card network, e.g. `Visa`, `Mastercard`. |
| `data.masked_number` | string | Masked card number, e.g. `**** **** **** 4242`. |
| `data.expiry` | string | Expiry date in `MM/YY` format. |
| `data.is_deleted` | boolean | `true` if the card has been soft-deleted. |

### Delete card (soft delete)

DELETEhttps://api.onepay.lk/v3/customers/{customer\_id}/cards/{token\_id}/?app\_id={app\_id}

Soft-deletes a saved card by setting `is_deleted = true`. The card token is immediately deactivated and cannot be used for any future charges. The customer profile and transaction history remain fully intact.

Deletion is irreversible. If the customer wants to pay again after a card is deleted, they must add a new card via the tokenization redirect flow.

PATH & QUERY PARAMETERS

| PARAMETER | TYPE | IN | DESCRIPTION |
| --- | --- | --- | --- |
| `customer_id` required | string | Path | Unique customer identifier. |
| `token_id` required | string | Path | The secure card token to be deleted. |
| `app_id` required | string | Query | Your application identifier. |

RESPONSE PARAMETERS — 200 OK

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `status` | number | `200` on successful deletion. |
| `message` | string | Confirmation message. |

# Charge a Card (Charge Token)

Charge a customer's saved card token for any amount triggered entirely from your server. No customer action required at payment time. This is the core of the auto-charging model.

POSThttps://api.onepay.lk/v3/customers/{customer\_id}/payments/

PATH PARAMETERS

| PARAMETER | TYPE | IN | DESCRIPTION |
| --- | --- | --- | --- |
| `customer_id` required | string | Path | Unique customer identifier, e.g. `cus_907fa39a`. |

REQUEST BODY

| PARAMETER | TYPE | DESCRIPTION |
| --- | --- | --- |
| `app_id` required | string | Your application identifier. |
| `token_id` required | string | The saved card token to charge, e.g. `tok_12345678`. |
| `amount` required | string | Amount to charge formatted as a string, e.g. `"1000.00"`. |
| `currency` required | string | Currency code, e.g. `LKR` or `USD`. |

RESPONSE PARAMETERS — 200 OK

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `status` | number | `200` on success. |
| `message` | string | Confirmation message. |
| `data.transaction_id` | string | Unique transaction identifier for this charge. |
| `data.status` | boolean | `true` if the charge was successfully processed. |
| `data.amount` | string | The amount charged. |
| `data.currency` | string | Currency of the charge. |
| `data.token_id` | string | The card token that was charged. |

##### BASIC CHARGE EXAMPLE

Charge a single saved card immediately. The foundation for all billing patterns.

##### FIXED BILLING EXAMPLE — SAME AMOUNT EVERY MONTH

Run this as a cron job on your chosen billing date. The amount is constant; only the timing changes.

##### VARIABLE BILLING EXAMPLE — PAY AS YOU GO

Calculate usage at period-end and charge exactly what was consumed. Token is constant; only the amount varies per customer per cycle.

# Customer Transactions

Retrieve the full billing history for a specific customer. Useful for displaying payment history in your product dashboard, generating invoices, reconciling subscription charges, or auditing billing cycles.

GEThttps://api.onepay.lk/v3/customers/{customer\_id}/transactions/?app\_id={app\_id}

PATH & QUERY PARAMETERS

| PARAMETER | TYPE | IN | DESCRIPTION |
| --- | --- | --- | --- |
| `customer_id` required | string | Path | Unique customer identifier, e.g. `cus_907fa39a`. |
| `app_id` required | string | Query | Your application identifier. |

RESPONSE PARAMETERS — 200 OK

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `status` | number | `200` on success. |
| `data` | array | Array of transaction objects ordered by most recent first. |
| `data[].transaction_id` | string | Unique identifier for the transaction. |
| `data[].amount` | string | Amount charged for this transaction. |
| `data[].currency` | string | Currency of the transaction. |
| `data[].status` | boolean | `true` if the transaction was successful. |
| `data[].token_id` | string | The card token used for this transaction. |
| `data[].created_at` | string | ISO 8601 timestamp of when the transaction was created. |

---

## Refund API Reference

**Category**: API Documentation  
**Source URL**: https://docs.onepay.lk/api-documentation/refund

# Refund

Initiate a full or partial refund for any successfully paid live transaction. Once submitted, the refund enters a `refund-initiated` state and is processed by OnePay's banking partner. Only one active refund request is allowed per transaction.

Full refund

Returns the entire transaction amount to the customer's card. Set `is_partially` to `false` and omit the `amount` field. OnePay uses the original transaction amount automatically.

Partial refund

Returns a specific portion of the transaction. Set `is_partially` to `true` and provide an `amount`. Useful for split-order cancellations and overcharge corrections.

POSThttps://api.onepay.lk/v3/transaction/refund/

AUTHENTICATION

| HEADER | VALUE | REQUIRED |
| --- | --- | --- |
| `Authorization` | Your merchant App Token | Yes |
| `Content-Type` | `application/json` | Yes |

REQUEST BODY

| PARAMETER | TYPE | DESCRIPTION |
| --- | --- | --- |
| `app_id` required | string | Your App ID. Must belong to the same app identified by the `Authorization` token. |
| `onepay_transaction_id` required | string | The OnePay transaction ID to refund. Must be a successful, live transaction that belongs to your app. |
| `refund_reason` required | string | One of the predefined refund reason codes. See the Refund Reasons table below. |
| `is_partially` optional | boolean | `true` for a partial refund; `false` for a full refund. Defaults to `false`. |
| `amount` conditional | decimal | The partial refund amount. Required when `is_partially` is `true`. Ignored for full refunds. |
| `refund_note` optional | string | A free-text note describing the reason for this refund. Useful for internal records and customer service. |

### Refund reason codes

| VALUE | DESCRIPTION |
| --- | --- |
| `DUPLICATED` | Transaction was a duplicate charge. |
| `FRAUDULENT` | Transaction was identified as fraudulent. |
| `OUT_OF_ORDER` | Service or product was unavailable or out of order. |
| `REQUESTED_BY_CUSTOMER` | Customer requested the refund directly. |
| `OTHER` | Any other reason. Use `refund_note` to provide detail. |

### Code examples

PHPNode.jsPythoncURL

```
// Full refund

$ch = curl_init('https://api.onepay.lk/v3/transaction/refund/');

curl_setopt_array($ch, [

CURLOPT_POST           => true,

CURLOPT_RETURNTRANSFER => true,

CURLOPT_HTTPHEADER     => [

'Authorization: YOUR_APP_TOKEN',

'Content-Type: application/json',

],

CURLOPT_POSTFIELDS => json_encode([

'app_id'                => 'YOUR_APP_ID',

'onepay_transaction_id' => 'ONP2026072800001',

'is_partially'          => false,

'refund_reason'         => 'REQUESTED_BY_CUSTOMER',

'refund_note'           => 'Customer requested a full refund',

]),

]);

$res = json_decode(curl_exec($ch), true);

if ($res['status'] === 200) {

update_order_status($res['data']['ipg_transaction_id'], 'REFUND INITIATED');

}

// Partial refund: add amount and set is_partially to true

// 'is_partially' => true, 'amount' => 500.00
```

RESPONSE PARAMETERS

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `status` | number | `200` on success. |
| `message` | string | `"Successfully initiated refund request"` |
| `data.ipg_transaction_id` | string | The OnePay transaction ID that was refunded. |
| `data.refund_id` | number | Unique identifier for this refund request. Store this for tracking. |
| `data.status` | string | `"refund-initiated"`. The transaction's status is updated to `REFUND INITIATED` at this point. |
| `data.is_partially` | boolean | Whether this was a partial refund. |
| `data.requested_amount` | string | The refund amount as a string. For full refunds, this is automatically set to the original transaction amount. |
| `data.refund_reason` | string | The reason code submitted with the request. |

### Error responses

| STATUS | ERROR | CAUSE |
| --- | --- | --- |
| 401 | `"Please provide request headers"` | The `Authorization` header is missing. |
| 400 | `"refund_reason: This field is required."` | The `refund_reason` field was omitted from the request body. |
| 400 | `"amount: Amount is required for a partial refund."` | `is_partially` was `true` but no `amount` was provided. |
| 400 | `"Invalid app credentials"` | The `app_id` does not match the app identified by the `Authorization` token. |
| 400 | `"Transaction not found"` | No matching transaction exists, or it belongs to a different app, or it is not a successful live transaction. |
| 400 | `"Refund already requested for this transaction"` | A refund has already been initiated for this transaction. Only one active refund is allowed per transaction. |

### Important notes

Live transactions only.

Refunds can only be initiated for transactions where both `status = true` (paid) and `is_live = true`. Test or sandbox transactions are not refundable via this endpoint.

One refund per transaction.

Only one active refund request is permitted per transaction. A subsequent refund attempt on the same transaction will be rejected until the existing refund record is resolved.

---

## Payouts & Settlement API

**Category**: API Documentation  
**Source URL**: https://docs.onepay.lk/api-documentation/payouts

# How Payouts Work

When a customer successfully completes a payment on your website, the funds are collected by OnePay's partner bank custodian account on your behalf and held in a settlement account. On your scheduled payout date, OnePay transfers the net amount directly to your registered bank account.

**Net amount = transaction value minus MDR (Merchant Discount Rate) and any applicable fees.** You will always receive the net figure, the gross transaction amount with processing costs already deducted.

Customer pays

Funds collected by partner bank

Settlement hold

Funds held in custodian account

Payout day

Net amount transferred via CEFT

Report sent

6pm &mdash; detailed payout report

### Payout report

You will receive a comprehensive payout report every day at **6:00 PM** on your scheduled payout date, but only on days when a payout actually occurs. If you have no transactions due for settlement that day, no report is sent.

The report includes a bank reference number for every payout transfer, giving you everything you need to tally the payout amount against your own records for reconciliation purposes.

**For reconciliation:** match the bank reference number in your payout report against the incoming CEFT transfer on your bank statement. If the amounts match, your settlement is complete.

### Payout method

All payouts are sent as **CEFT (Common Electronic Fund Transfer)** transactions directly to your registered bank account. This is the standard interbank transfer mechanism in Sri Lanka.

### Current limitations

#### No early payouts

OnePay does not support early or accelerated payouts before the scheduled settlement date at this time.

#### No split payouts

OnePay does not support split payout options (distributing a single payout to multiple bank accounts) at this time.

### Haven't received your payout?

If your expected payout has not arrived, please contact your **OnePay relationship officer** directly for clarification. Do not raise a dispute with your bank first, your relationship officer can view the exact transfer status and reason for any delay or hold.

# Payout Schedule

OnePay operates on a T+2 payout cycle, you receive your payout two **bank working days** after the transaction date. Weekends and public holidays are not counted.

**T+2 means bank working days only.** If the T+2 date falls on a weekend or public holiday, the payout moves to the next available bank working day.

### How T+2 works (examples)

| PAYMENT ACCEPTED ON | T+1 | PAYOUT ON (T+2) |
| --- | --- | --- |
| **Monday** | Tuesday | **Wednesday** |
| **Tuesday** | Wednesday | **Thursday** |
| **Wednesday** | Thursday | **Friday** |
| **Thursday** | Friday | **Monday** (weekend skipped) |
| **Friday** | Monday | **Tuesday** (weekend skipped) |

### Payout time

Payouts are processed before **6:00 PM** on the payout day. Your payout report is also sent at this time. Note that the exact credit time into your bank account depends on your bank's processing. CEFT transfers typically reflect within a few hours but may take until end of business day.

Payouts may occasionally be delayed due to **bank system downtime** (your bank or the partner bank) or other technical issues outside OnePay's control. If a CEFT transfer fails, for example due to the beneficiary bank being temporarily offline or an account being in inactive mode, you will be informed and the payout will be rescheduled for the next payout cycle.

### American Express (Amex) payouts

**Amex transactions follow a T+3 schedule**, one additional working day compared to Visa, Mastercard, and other payment methods. OnePay is actively working with its banking partner to align Amex payouts with the standard T+2 schedule.

| PAYMENT METHOD | PAYOUT SCHEDULE | NOTES |
| --- | --- | --- |
| Visa | **T+2** bank working days | Standard schedule |
| Mastercard | **T+2** bank working days | Standard schedule |
| Other methods | **T+2** bank working days | Standard schedule |
| American Express | **T+3** bank working days | Schedule alignment in progress |

# Payout Holds & Delays

In certain circumstances, OnePay may place a hold on your payout. This is done to protect both merchants and cardholders and to comply with card network regulations. Held payouts are released once the underlying issue is resolved.

If your payout has been held or delayed, contact your **OnePay relationship officer** immediately. They can advise on the specific reason and the steps needed to release the hold.

### Reasons a payout may be held

Unresolved chargeback

A cardholder has raised a dispute with their issuing bank. Payouts related to disputed transactions are held until the chargeback is resolved, either in your favour or settled.

Business nature conflict

A discrepancy has been identified between the business type you registered with OnePay and the actual transactions being processed. Your account is reviewed until the nature of business is confirmed and aligned.

Suspicious transaction flagged by card networks

Visa or Mastercard's fraud detection systems have flagged one or more transactions as suspicious. Payouts are held pending a review by the card network and OnePay's risk team.

Chargeback recoveries due

Outstanding chargeback amounts owed to OnePay from previous disputes may be offset against your upcoming payout until the recovery balance is cleared.

### Technical delays

Beyond holds, payouts can be delayed by technical issues that are outside OnePay's control:

| CAUSE | WHAT HAPPENS |
| --- | --- |
| Bank system downtime | The CEFT transfer cannot be processed. OnePay will retry on the next available opportunity and notify you of the delay. |
| Beneficiary account inactive | Your registered bank account is in inactive or dormant mode. The payout fails at the receiving bank. OnePay notifies you and reschedules for the next payout cycle. |
| Incorrect account details | The CEFT transfer is rejected by the receiving bank. Contact your relationship officer to update your registered bank account details. |

When a payout fails due to a bank-side issue, OnePay will inform you directly and reschedule the transfer for the next payout cycle. You do not need to raise a new request, the rescheduling is automatic.

# Transaction Lookup

The Transaction Lookup API gives you a real-time settlement breakdown for any individual OnePay transaction. Given a transaction ID, it returns the exact net amount received, the commission rate and amount that was deducted, the final settlement amount credited to your account, and the precise date and time that settlement occurred.

This is the endpoint to use when you need to verify exactly what was paid out for a specific transaction, whether you are reconciling a payout report, investigating a discrepancy with your finance team, or building an automated reconciliation pipeline inside your ERP or accounting system.

**Common use cases:** matching a customer's payment to your payout report, confirming commission deductions for finance reporting, building a reconciliation dashboard, or auditing individual transactions against your bank statement.

GEThttps://api.onepay.lk/v3/payout/transaction/?onepay\_transaction\_id={onepay\_transaction\_id}

AUTHENTICATION

| HEADER | VALUE | REQUIRED |
| --- | --- | --- |
| `Authorization` | Your App Token (e.g. `2c4e7c3ee0013882...`) | Yes |
| `Content-Type` | `application/json` | Yes |

QUERY PARAMETERS

| PARAMETER | TYPE | IN | DESCRIPTION |
| --- | --- | --- | --- |
| `onepay_transaction_id` required | string | Query | The OnePay transaction ID returned in `data.ipg_transaction_id` when the payment was originally created. This is the same ID you should have stored at checkout time. |

RESPONSE PARAMETERS, 200 OK

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `status` | number | `200` on success. |
| `message` | string | `"Transaction fetched successfully"` |
| `data.onepay_transaction_id` | string | The OnePay transaction identifier, echoed back for confirmation. |
| `data.order_id` | string | Your internal order or reference ID as passed during transaction creation. |
| `data.currency` | string | Currency of the transaction, e.g. `LKR`. |
| `data.net_amount` | string | The gross transaction amount the customer paid. |
| `data.commission_rate` | string | The MDR (Merchant Discount Rate) percentage applied to this transaction, e.g. `"2.50"` for 2.5%. |
| `data.commission_amount` | string | The exact fee amount deducted from the gross transaction. This is what OnePay charged for processing. |
| `data.settlement_amount` | number | The net amount credited to your bank account after deducting the commission. **This is the figure that should appear on your bank statement and payout report.** |
| `data.settlement_date` | string | The date and time the settlement was processed, in `YYYY-MM-DD HH:mm` format. |

### Code examples

PHPNode.jsPythoncURL

```
$tx_id = 'WQBV118E584C83CBA50C6'; // stored at checkout time

$ch    = curl_init(

'https://api.onepay.lk/v3/payout/transaction/?onepay_transaction_id=' . $tx_id

);

curl_setopt_array($ch, [

CURLOPT_RETURNTRANSFER => true,

CURLOPT_HTTPHEADER     => [

'Authorization: YOUR_APP_TOKEN',

'Content-Type: application/json',

],

]);

$res = json_decode(curl_exec($ch), true);

// Use for reconciliation

$settlement = $res['data']['settlement_amount'];   // what hit your bank

$commission = $res['data']['commission_amount'];   // MDR deducted

$settled_on = $res['data']['settlement_date'];    // when it was settled

echo "Settled: LKR {$settlement} on {$settled_on} (MDR: {$commission})";
```

### Understanding the amounts

The three amount fields form a simple equation you can use to verify every settlement:

net\_amount   −   commission\_amount   =   settlement\_amount

| FIELD | EXAMPLE | WHAT IT MEANS |
| --- | --- | --- |
| `net_amount` | `"5.00"` | Gross amount the customer paid. |
| `commission_rate` | `"2.50"` | Your MDR: 2.50% applied to this transaction. |
| `commission_amount` | `"0.13"` | LKR 0.13 deducted as the processing fee (2.5% of LKR 5.00). |
| `settlement_amount` | `4.87` | What was credited to your bank account: 5.00 − 0.13 = 4.87. |

The `settlement_date` in the response reflects when OnePay processed the payout, not when it appeared in your bank account. Allow for CEFT processing time (usually same day, before 6 PM). If `settlement_date` is populated, the funds have left OnePay and are in transit to your bank.

# Transaction List

The Transaction List API retrieves a paginated list of all settlement transactions within a specified date range. Use this to pull your full payout history for any period, ideal for building automated reconciliation pipelines, generating finance reports, and auditing settlement activity at scale without downloading reports manually from the dashboard.

Unlike the single Transaction Lookup endpoint which requires a known transaction ID, this endpoint lets you query by date range and page through all results, making it the right tool for period-end reconciliation, month-close accounting processes, and any scenario where you need to process multiple settlements in bulk.

**Common use cases:** end-of-day reconciliation jobs, month-end finance reports, ERP settlement imports, identifying transactions where `settlement_date` is `null` (not yet settled), and verifying total payout amounts against your bank statement for a given period.

GEThttps://api.onepay.lk/v3/payout/transactions/?start\_date={start\_date}&end\_date={end\_date}&page={page}&page\_size={page\_size}

AUTHENTICATION

| HEADER | VALUE | REQUIRED |
| --- | --- | --- |
| `Authorization` | Your App Token (e.g. `2c4e7c3ee0013882...`) | Yes |

QUERY PARAMETERS

| PARAMETER | TYPE | REQUIRED | DESCRIPTION |
| --- | --- | --- | --- |
| `start_date` required | string | Yes | Start of the date range in `YYYY-MM-DD` format, e.g. `2026-04-01`. Inclusive. |
| `end_date` required | string | Yes | End of the date range in `YYYY-MM-DD` format, e.g. `2026-04-28`. Inclusive. |
| `page` required | integer | Yes | Page number to retrieve. Starts at `1`. Use with `count` and `page_size` in the response to determine how many pages exist. |
| `page_size` required | integer | Yes | Number of records to return per page. Recommended: `20`–`100`. Use a consistent value when paginating to avoid missing or duplicating records. |

RESPONSE PARAMETERS, 200 OK

| FIELD | TYPE | DESCRIPTION |
| --- | --- | --- |
| `status` | number | `200` on success. |
| `message` | string | `"Transactions fetched successfully"` |
| `data.count` | number | Total number of transactions matching your date range across all pages. Use this to calculate total pages: `Math.ceil(count / page_size)`. |
| `data.page` | number | The current page number returned. |
| `data.page_size` | number | Number of records returned in this response. |
| `data.results` | array | Array of transaction objects for this page. |
| `data.results[].onepay_transaction_id` | string | OnePay's unique transaction identifier. |
| `data.results[].order_id` | string | Your internal order or reference ID as passed at transaction creation. |
| `data.results[].currency` | string | Transaction currency, e.g. `LKR`. |
| `data.results[].net_amount` | string | Gross amount the customer paid. |
| `data.results[].commission_rate` | string | The MDR percentage applied to this transaction. |
| `data.results[].commission_amount` | string | The fee amount deducted from the gross transaction. |
| `data.results[].settlement_amount` | number | Net amount credited to your bank account after fee deduction. |
| `data.results[].settlement_date` | string | null | `null` means the transaction has not yet been settled, it is pending in the upcoming payout cycle. A date value confirms settlement has been processed. |

**Identifying unsettled transactions:** filter the results for records where `settlement_date === null`. These are transactions that have been captured but not yet transferred to your bank account, they will appear in a future payout cycle.

### Pagination

The API uses page-based pagination. The `data.count` field tells you the total number of records, use it to calculate how many pages you need to fetch to get the complete dataset for your date range.

total\_pages  =  Math.ceil( data.count  /  page\_size )

For example: `count = 322` with `page_size = 20` means `Math.ceil(322/20) = 17` pages. Loop from `page=1` to `page=17` to retrieve all records.

### Code examples

PHPNode.jsPythoncURL

```
// Fetch all transactions for April 2026 — auto-paginated

function fetchAllTransactions($start, $end, $token) {

$all  = [];

$page = 1;

do {

$url = "https://api.onepay.lk/v3/payout/transactions/"

. "?start_date={$start}&end_date={$end}&page={$page}&page_size=100";

$ch = curl_init($url);

curl_setopt_array($ch, [

CURLOPT_RETURNTRANSFER => true,

CURLOPT_HTTPHEADER     => ["Authorization: {$token}"],

]);

$res  = json_decode(curl_exec($ch), true);

$data = $res['data'];

$all  = array_merge($all, $data['results']);

$total_pages = ceil($data['count'] / 100);

$page++;

} while ($page <= $total_pages);

return $all;

}

$txns = fetchAllTransactions('2026-04-01', '2026-04-28', 'YOUR_APP_TOKEN');

// Reconciliation — tally settled vs pending

$settled = array_filter($txns, fn($t) => $t['settlement_date'] !== null);

$pending = array_filter($txns, fn($t) => $t['settlement_date'] === null);

$total_settled = array_sum(array_column($settled, 'settlement_amount'));

echo "Settled: " . count($settled) . " txns | LKR {$total_settled}\n";

echo "Pending: " . count($pending) . " txns (next payout cycle)\n";
```

### Reading `settlement_date: null`

A `null` settlement date is not an error, it simply means the transaction has been captured but not yet included in a payout transfer. This will happen for transactions that fall within your date range but whose T+2 settlement date has not yet passed, or transactions currently under a payout hold.

| SETTLEMENT\_DATE VALUE | WHAT IT MEANS | ACTION |
| --- | --- | --- |
| `null` | Transaction captured, settlement pending. Not yet transferred to your bank. | No action needed, will appear in next payout cycle. Check again after the T+2 window. |
| `"2026-04-28 15:37"` | Settlement has been processed. Funds left OnePay at this timestamp. | Match `settlement_amount` against your bank statement CEFT credit for that date. |

---

# Testing

## Test Card Details

**Category**: Testing  
**Source URL**: https://docs.onepay.lk/testing/test-cards

# Test Card Details

Use the following test card details for integration testing:

| Card Type | Card Number | Expiration Date | CVV |
| --- | --- | --- | --- |
| Visa | 4508750015741019 | 01/39 | 100 |
| Visa | 4012000033330026 | 01/39 | 100 |
| Master | 5123450000000008 | 01/39 | 100 |
| Master | 5111111111111118 | 01/39 | 100 |

---

# SDKs and Plugins

## OnePay JS Checkout Overlay

**Category**: SDKs and Plugins  
**Source URL**: https://docs.onepay.lk/api-documentation/onepay-js

# OnePay JS

A lightweight checkout overlay for your website. No redirects, no page reloads, no lost customers halfway through a sale. Your buyer pays right where they are, and you get the result back in real time.

##### The simplest way to accept payments on your site.

Drop in one script tag, set a few fields, and OnePay JS handles the rest: the secure payment overlay, the bank communication, and the success or failure event your code can listen for.

## Why an overlay instead of a redirect

Sending a customer away from your website to pay, and hoping they come back, has always been a weak point in online checkout. Every redirect is a chance for someone to lose their place, get distracted, or simply give up.

OnePay JS solves this the way modern checkout experiences are meant to work. The payment form opens in a clean overlay on top of your page. Your customer never leaves your site. The moment they finish paying, your page hears about it instantly, with no polling and no guesswork.

#### Stays on your page

The payment form appears as an overlay, not a redirect. Your branding, your layout, your customer's attention stays exactly where you want it.

#### Instant result

Success and failure are pushed to your page the moment they happen, through simple browser events your code already knows how to listen for.

#### Works with what you already have

Plain HTML, PHP, React, or any modern frontend. One script tag and a small data object are all that's needed to get started.

#### Bank-grade security, zero extra work

Card details never touch your server. The hash signature protects every request, and OnePay handles the rest behind the scenes.

## Setup & Integration

Getting OnePay JS running on your site takes four short steps. Most teams have a working test payment within the hour.

1. ### Add the script

   Place this script tag in your page, ideally near the closing `</body>` tag so it loads after your content.

   ```
   <script src="https://storage.googleapis.com/onepayjs/onepayv2.js"></script>
   ```
2. ### Get your credentials

   Log in to your OnePay merchant dashboard and open the App section to find your **App ID**, **App Token**, and **Hash Salt**. You will use all three in the next step.

   ##### Warning

   Your Hash Salt should never be exposed in your frontend code. Generate the hash on your server and pass only the resulting `hashToken` value to the browser.
3. ### Set your payment data

   Define a `window.onePayData` object with your transaction details, then listen for the two events OnePay JS dispatches when the payment finishes.

   #### Configuration Fields

   | Field | Type | Description |
   | --- | --- | --- |
   | appid Required | string | Your OnePay App ID. |
   | hashToken Required | string | Your Hash Salt, used by the script to sign the request. Keep this server-managed where possible. |
   | apptoken Required | string | Your App Token, sent as the Authorization header when the payment request is created. |
   | amount Required | number | The amount to charge, e.g. `100.00`. |
   | currency Required | string | Three-letter currency code (e.g. LKR). |
   | orderReference Required | string | Your internal order or invoice reference. |
   | customerFirstName Required | string | Customer's first name. |
   | customerLastName Required | string | Customer's last name. |
   | customerPhoneNumber Required | string | Phone number in E.164 format, e.g. `+94771234567`. |
   | customerEmail Required | string | Customer's email address. |
   | transactionRedirectUrl Required | string | Fallback URL used by the gateway. The overlay flow does not navigate the customer away, but this is still required. |
   | additionalData Optional | string | Any extra metadata you want echoed back in the success or fail event. |

   #### Code Examples

   HTMLPHPReact

   ```
   <script>

   window.onePayData = {

   appid: "80NR1189D04CD635D8ACD",

   hashToken: "GR2P1189D04CD635D8AFD",

   amount: 100.00,

   orderReference: "7Q1M1187AE",

   customerFirstName: "Amila",

   customerLastName: "Perera",

   customerPhoneNumber: "+94771234567",

   customerEmail: "amila@yourstore.lk",

   transactionRedirectUrl: "https://yourstore.lk/thank-you",

   additionalData: "returndata",

   apptoken: "YOUR_APP_TOKEN",

   currency: "LKR"

   };

   // Fires when the customer completes payment

   window.addEventListener("onePaySuccess", function (e) {

   const successData = e.detail;

   console.log("Payment SUCCESS", successData);

   // show a confirmation, update your order, etc.

   });

   // Fires when the payment is declined or cancelled

   window.addEventListener("onePayFail", function (e) {

   const failData = e.detail;

   console.log("Payment FAIL", failData);

   });

   </script>

   <!-- OnePayJS automatically injects a "Pay Now" button here -->

   <div id="onepay-btn"></div>
   ```
4. ### Test, then go live

   Use your sandbox App ID and App Token first to confirm everything fires correctly. Once a test payment completes successfully on your page, switch to your live credentials and you're ready to accept real transactions.

   ##### Info

   OnePayJS automatically renders a **Pay Now** button inside the element with id `onepay-btn`. You don't need to build your own button, just provide the container and the data object.

## Events & Callbacks

OnePay JS talks back to your page using two browser events. No polling, no waiting, no extra requests. The moment the customer's payment is decided, your code finds out.

### OnePay Success

Dispatched the instant a payment completes successfully. The overlay closes itself automatically before this event fires, so your page is already clear to show a confirmation message.

| Field | Type | Description |
| --- | --- | --- |
| code | string | Result code, `"SUCCESS"` for this event. |
| transaction\_id | string | The OnePay transaction identifier. Store this for reconciliation and status lookups. |
| status | string | `"SUCCESS"` |

### OnePay Fail

Dispatched when a payment is declined, cancelled, or otherwise does not complete. Use this to let the customer know gently and offer them another attempt.

| Field | Type | Description |
| --- | --- | --- |
| code | string | Result code, `"FAIL"` for this event. |
| transaction\_id | string | The OnePay transaction identifier, useful for support and debugging. |
| status | string | `"FAIL"` |

#### Listening for both events

JavaScriptReact

```
window.addEventListener("onePaySuccess", function (e) {

const { transaction_id, status } = e.detail;

// Confirm the order in your own UI

document.getElementById("order-status").textContent = "Payment received, thank you!";

// Optional: verify server-side using the Transaction Status API

fetch("/api/confirm-order", {

method: "POST",

headers: { "Content-Type": "application/json" },

body: JSON.stringify({ transaction_id }),

});

});

window.addEventListener("onePayFail", function (e) {

const { transaction_id } = e.detail;

document.getElementById("order-status").textContent =

"That payment didn't go through. Please try again.";

});
```

##### Best practice

Treat the browser event as a signal to update your interface, but confirm the final order state server-side using the [Transaction Status API](/api-documentation/payment-api#transaction-status) before marking an order as paid in your database. This protects you if a browser event is ever missed due to a closed tab or network hiccup.

### Server-side callback

In addition to the two browser events, OnePay can send a server-to-server callback to a URL you configure in your dashboard. This is the most reliable way to confirm payment outcomes, since it does not depend on the customer's browser staying open.

Set your callback URL under the App section of your OnePay dashboard. Your endpoint should accept a POST request with a JSON body and respond with a `200` status.

#### Sample callback payload

```
{

"transaction_id": "WQBV118E584C83CBA50C6",

"status": 1,

"status_message": "SUCCESS",

"additional_data": ""

}
```

Use this payload to log the transaction, verify it against your own records, and update the order status in your system. Always treat the callback and the Transaction Status API as your source of truth, with the browser events as a fast, friendly layer on top for your customer's experience.

---

## JavaScript SDK

**Category**: SDKs and Plugins  
**Source URL**: https://docs.onepay.lk/plugins/javascript-sdk

# JavaScript SDK

The official OnePay SDK for JavaScript applications. It wraps the same checkout flow as OnePayJS in a typed class with proper event listeners, and adds first-class support for subscriptions. Published on npm as `@onepaynpm/onepay-sdk`, currently at version 1.0.3, with zero external dependencies.

**Best for:** React, Vue, and other modern frontend apps where you want a typed API instead of managing `window.onePayData` and global event listeners by hand. Also the only documented way to process subscriptions client-side.

### Installation

```
npm install @onepaynpm/onepay-sdk
```

### Basic setup

Create an `OnePaySDK` instance and initialize it once when your app loads.

```
import { OnePaySDK } from '@onepaynpm/onepay-sdk';

const onePaySDK = new OnePaySDK({

debug: true, // Enable debug logging

apiBaseUrl: 'https://api.onepay.lk' // Optional, defaults to this

});

// Initialize the SDK before processing any payment

await onePaySDK.initialize();
```

### Adding event listeners

**Important:** event listeners must be attached directly on the SDK instance, not on a ref or DOM element. Attaching to a ref's `.current` property will not work.

```
// Correct way

onePaySDK.addEventListener({

onSuccess: (result) => {

console.log('Payment successful:', result);

// handle the successful payment

},

onFail: (result) => {

console.log('Payment failed:', result);

// handle the failed payment

},

onClose: (result) => {

console.log('Payment modal closed:', result);

// handle the customer closing the modal

},

});

// This will not work

// onePaySDKRef.current.addEventListener({ ... })
```

### Processing a payment

Call `processPayment` with the same fields used by OnePayJS. This opens the secure payment overlay and resolves once the flow starts.

```
await onePaySDK.processPayment({

currency: 'LKR',

amount: 1000,

appid: 'your-app-id',

hashToken: 'your-hash-token',

orderReference: 'ORDER-123',

customerFirstName: 'John',

customerLastName: 'Doe',

customerPhoneNumber: '+94123456789',

customerEmail: 'john@example.com',

transactionRedirectUrl: 'https://your-site.com/payment-success',

apptoken: 'your-app-token',

});
```

### Processing a subscription

The SDK also exposes `processSubscription`, which sets up a recurring billing schedule directly, including trial periods. This is the only documented client-side path to subscription billing; the rest of OnePay's recurring billing is handled server-side through Card on File.

```
await onePaySDK.processSubscription({

currency: 'LKR',

amount: 500,

appid: 'your-app-id',

name: 'Monthly Subscription',

interval: 'month',

interval_count: 1,

days_until_due: 7,

trial_period_days: 14,

customer_details: {

first_name: 'John',

last_name: 'Doe',

email: 'john@example.com',

phone: '+94123456789',

},

apptoken: 'your-app-token',

});
```

### Subscription parameters

| Field | Type | Description |
| --- | --- | --- |
| `currency` | string | Three-letter currency code, e.g. `LKR`. |
| `amount` | number | The amount charged on each billing cycle. |
| `name` | string | A label for the subscription plan, shown to the customer. |
| `interval` | string | Billing interval unit, e.g. `"month"`. |
| `interval_count` | number | How many intervals between charges. `1` with `interval: "month"` means monthly. |
| `days_until_due` | number | Grace period in days before an unpaid invoice is considered overdue. |
| `trial_period_days` | number | Number of free trial days before the first charge. |
| `customer_details` | object | Customer's `first_name`, `last_name`, `email`, and `phone`. |

### Direct payment with an existing gateway URL

If you already have a `redirect_url` and transaction ID from a server-side call to the Payment API, you can open the payment overlay directly without calling `processPayment` again.

```
await onePaySDK.processDirectPayment({

directGatewayURL: 'https://payment-gateway-url',

directTransactionId: 'transaction-id',

});
```

### React example

A complete pattern for wiring the SDK into a React component, including initialization, event listeners, and a disabled state while a payment is processing.

```
import React, { useEffect, useState } from 'react';

import { OnePaySDK, PaymentResult } from '@onepaynpm/onepay-sdk';

const PaymentComponent: React.FC = () => {

const [onePaySDK] = useState(new OnePaySDK({ debug: true }));

const [isInitialized, setIsInitialized] = useState(false);

const [isProcessing, setIsProcessing] = useState(false);

useEffect(() => {

const initializeSDK = async () => {

try {

await onePaySDK.initialize();

setIsInitialized(true);

// Set up event listeners, the correct way

onePaySDK.addEventListener({

onSuccess: (result: PaymentResult) => {

console.log('Payment successful:', result);

setIsProcessing(false);

},

onFail: (result: PaymentResult) => {

console.log('Payment failed:', result);

setIsProcessing(false);

},

onClose: (result: PaymentResult) => {

console.log('Payment modal closed:', result);

setIsProcessing(false);

},

});

} catch (error) {

console.error('Failed to initialize OnePay SDK:', error);

}

};

initializeSDK();

}, [onePaySDK]);

const handlePayment = async () => {

if (!isInitialized) return;

setIsProcessing(true);

try {

await onePaySDK.processPayment({

currency: 'LKR',

amount: 1000,

appid: 'your-app-id',

hashToken: 'your-hash-token',

orderReference: `ORDER-${Date.now()}`,

customerFirstName: 'John',

customerLastName: 'Doe',

customerPhoneNumber: '+94123456789',

customerEmail: 'john@example.com',

transactionRedirectUrl: window.location.origin + '/payment-success',

apptoken: 'your-app-token',

});

} catch (error) {

console.error('Payment processing error:', error);

setIsProcessing(false);

}

};

return (

<div>

<button onClick={handlePayment} disabled={!isInitialized || isProcessing}>

{isProcessing ? 'Processing...' : 'Pay Now'}

</button>

</div>

);

};
```

### API reference

**Constructor options**

| Option | Type | Description |
| --- | --- | --- |
| `firebaseConfig` | object | Firebase configuration object. The SDK uses Firebase internally to listen for transaction updates in real time. |
| `apiBaseUrl` | string | Custom API base URL. Defaults to `https://api.onepay.lk`. |
| `debug` | boolean | Enables debug logging to the console. Defaults to `false`. |

**Methods**

| Method | Description |
| --- | --- |
| `initialize()` | Initializes the SDK. Call this once before processing any payment. |
| `addEventListener(listeners)` | Registers `onSuccess`, `onFail`, and `onClose` handlers on the SDK instance. |
| `removeEventListener(type, listener)` | Removes a previously registered event listener. |
| `processPayment(data)` | Opens the secure payment overlay for a standard one-time payment. |
| `processSubscription(data)` | Sets up a recurring billing subscription. |
| `processDirectPayment(data)` | Opens the payment overlay using a gateway URL and transaction ID you already obtained server-side. |
| `closePaymentGateway()` | Programmatically closes the payment overlay. |
| `isInitialized()` | Returns whether the SDK has completed initialization. |

**Event types**

| Event | Fires when |
| --- | --- |
| `onePaySuccess` | The payment completes successfully. |
| `onePayFail` | The payment fails or is declined. |
| `onePayClose` | The customer closes the payment modal without completing payment. |

### Troubleshooting

**Event listeners not firing**

If your listeners never trigger, double check that you are calling `addEventListener` on the SDK instance itself, not on a ref's `.current` value.

```
// Correct way

onePaySDK.addEventListener({ /* ... */ });

// This does not work

onePaySDKRef.current.addEventListener({ /* ... */ });
```

**Firebase listener issues**

The SDK uses Firebase internally to listen for transaction status updates. If payments seem to hang or events never fire, check that your Firebase configuration is correct and that `initialize()` has resolved before you call `processPayment`.

**License:** MIT. Zero external dependencies. If you would rather not add a package dependency, the raw script-tag approach documented under **OnePayJS** achieves the same checkout overlay without an npm install.

---

## WooCommerce / WordPress Plugin

**Category**: SDKs and Plugins  
**Source URL**: https://docs.onepay.lk/plugins/wordpress

# WordPress Plugin Integration

You need to have the WooCommerce plugin installed to use the Onepay plugin.

### Installation Steps

1. ### Install the Plugin

   You can install the plugin in one of two ways:
   * Visit [WordPress Plugin Directory](https://wordpress.org/plugins/onepay-payment-gateway-for-woocommerce/)
   * Or search for "Onepay Payment Gateway" from the WordPress plugins section
2. ### Activate the Plugin

   After installation, activate the plugin from your WordPress plugins page
3. ### Configure Plugin Settings

   Navigate to the plugin settings page and configure the following:
   * Copy your App ID from the merchant portal
   * Copy your App Token from the merchant portal
   * Copy your Hash Salt from the merchant portal
   * Paste these values in their respective fields in the Onepay plugin settings
4. ### Redirect Settings

   The default redirect is set to the WooCommerce thank you page. You can keep this setting unless you have specific requirements.

**All Set!** Your WordPress site is now ready to accept payments through Onepay.

---

## Shopify Payment Plugin

**Category**: SDKs and Plugins  
**Source URL**: https://docs.onepay.lk/plugins/shopify

# Shopify Plugin Install

[Get it on Shopify App Store](https://apps.shopify.com/onepay-payment-new)

## How to Uninstall the Old OnePay App from Your Shopify Store (Step-by-Step)

If you’re migrating to a new OnePay integration or simply removing the old app, follow this clean, comprehensive process. It ensures your checkout won’t break, stray code won’t slow your theme, and billing stops on time.

### TL;DR (Quick Checklist)

* Pause OnePay as a payment method: Settings → Payments → OnePay → Deactivate
* Remove the app: Settings → Apps and sales channels → Uninstall
* Clean theme code: Online Store → Themes → Edit code (search and remove “onepay” snippets/scripts)
* Turn off app embeds/blocks: Themes → Customize → App embeds/Sections
* Clear scripts & pixels: Settings → Customer events (remove OnePay scripts if any)
* Export data you need (payouts, settlements, mapping): from your OnePay dashboard (if applicable)
* Verify checkout & speed; publish theme

### Before You Start

* Access level: You’ll need Shopify admin access with permission to manage apps and theme code.
* Downtime plan: Deactivating a payment method affects new orders immediately—do this during a low-traffic window.
* Backup: Duplicate your live theme: Online Store → Themes → … → Duplicate.
* Data export (recommended): From the OnePay dashboard, export any settlement reports, reconciliation files, or mappings you’ll need for accounting and support.

1. ### Deactivate OnePay as a Payment Method

### Video Tutorial

1. ### Uninstall the Old OnePay App

   Path A (most common):

   Path B (older layout):

## How to Install the New OnePay App on Shopify (Step-by-Step)

Integrating OnePay into your Shopify store unlocks seamless payment processing, faster settlements, and multiple payment options for your customers. To make sure your setup is smooth, follow this detailed step-by-step installation guide.

### Before You Begin

* Shopify Access: You’ll need admin-level access.
* OnePay Account: Make sure you already have a OnePay merchant account (with approved credentials).
* Theme Backup (recommended): Duplicate your live theme in Online Store → Themes → … → Duplicate. This ensures you have a fallback in case of theme edits.

## Video Tutorial

1. ### Open the Shopify App Store
2. ### Add the OnePay App
3. ### Connect Your OnePay Merchant Account
4. ### Activate OnePay as a Payment Method
5. ### Enable App Embeds (If Applicable)

   Some features (e.g., branded checkout buttons) may use Shopify’s App embeds.
6. ### Test Your Integration
7. ### Go Live

   * Switch from Test Mode to Live Mode in OnePay settings.
   * Announce to your customers that you now support OnePay for faster and more secure payments.

### Troubleshooting

I don’t see OnePay in the payment providers list.

* Make sure the app is installed and you’ve activated it under Settings → Payments.

My payments are failing.

* Double-check API credentials. A typo in the secret key or merchant ID can cause issues.

Checkout page looks broken.

* Check if leftover code from an old app is interfering (see uninstall guide).
* Make sure OnePay app embeds are enabled.

### Best Practices

* Always test after installation before announcing live payments.
* Keep your OnePay credentials secure—never share publicly.
* Review your settlement reports regularly to match transactions with Shopify orders.

---

## WHMCS Payment Gateway Setup

**Category**: SDKs and Plugins  
**Source URL**: https://docs.onepay.lk/plugins/whmcs

# WHMCS Plugin Integration

[Download from GitHub](https://github.com/onepay-srilanka/onepay-WHMCS)

### Installation Steps

1. ### Get Plugin Files

   Download the plugin ZIP file from the [OnePay WHMCS GitHub repository](https://github.com/onepay-srilanka/onepay-WHMCS) (click **Code → Download ZIP**) or contact your OnePay Relationship Officer to receive the files directly.
2. ### Extract Files

   Unzip the file contents on your computer
3. ### Install Gateway Module

   On your WHMCS server:
   * Navigate to `modules/gateways` directory
   * Copy the `onepay` folder and `onepay.php` file from the extracted ZIP
   * Paste them into the gateways directory
4. ### Install Callback Handler

   Still on your WHMCS server:
   * Navigate to `gateways/callback` directory
   * Copy the `onepay.php` file from the callback folder in the ZIP
   * Paste it into the callback directory
5. ### Configure Plugin Settings

   In your WHMCS admin panel:
   * Locate Onepay in the payment gateways section
   * Copy your App ID from the merchant portal
   * Copy your App Token from the merchant portal
   * Copy your Hash Salt from the merchant portal
   * Paste these values in their respective fields
   * Click Save to apply your changes

### Video Tutorial

**All Set!** Your WHMCS installation is now ready to accept payments through Onepay.

---

## Zoho Books & Inventory Extension

**Category**: SDKs and Plugins  
**Source URL**: https://docs.onepay.lk/plugins/zoho

# Zoho OnePay Extension — Installation & Configuration Guide

## Zoho OnePay Extension — Installation & Configuration Guide

This guide walks you through installing and configuring the OnePay payment gateway extension for Zoho Books or Zoho Inventory, so your customers can make secure card payments directly through your invoices.

### Prerequisites

Before you begin, make sure you have:

* Admin access to your Zoho Books / Zoho Inventory account
* Access to the Zoho Marketplace
* An active OnePay Merchant Admin Console account with IPG Apps configured

1. ### Install the Extension from Zoho Marketplace

   
2. ### Access Payment Gateway Settings in Zoho

   
3. ### Retrieve Your API Keys from OnePay

   
4. ### Configure OnePay in Zoho

   
5. ### Enable OnePay on Your Invoices

   
6. ### Customer Checkout Experience

   Once the invoice is sent, your customer will see the following on their end:

   
7. ### Payment Confirmation in Zoho

   Once your customer successfully completes the payment through OnePay, Zoho automatically updates the following:

   

### Video Tutorial

## Troubleshooting

---

# Guides

## Getting Started & Onboarding

**Category**: Guides  
**Source URL**: https://docs.onepay.lk/guide/getting-started

# OnePay Docs

Explore the capabilities of OnePay through our user-friendly documentation. For developers, our comprehensive API documentation provides clear guidance and code samples for easy integration.

### Account Setup

Create your OnePay account, set up business details, and start accepting payments in minutes.

### Developers

Start building with our simple APIs for Payments, Tokens, and more. Built for scale and speed.

### No Code Tools

Invoicing, payment links, POS and more. OnePay's tools work out of the box so you can launch fast.

### Integrations

Connect OnePay to Shopify, WooCommerce, WHMCS and other platforms with our seamless plugins.

# About OnePay

### Our Story

OnePay was launched in 2021 by **Spemai (Pvt) Ltd**, a technology company backed by a reputed Japanese corporate investor since 2019. What began as a bold idea to modernise digital payments in Sri Lanka has grown into the country's most trusted and scalable payment infrastructure. In just four years, OnePay has crossed **LKR 10 billion** in payment volume, onboarded **4,500+ active merchants**, and earned the distinction of being Sri Lanka's first payment gateway to achieve **ISO 27001 certification**, the global gold standard for information security.

### Our Vision

To transform the future of finance and digital services by building intelligent, inclusive, and accessible solutions that empower businesses and people globally.

### Our Mission

To innovate and deliver cutting-edge fintech and AI-powered platforms that simplify payments, automate financial operations, and enhance customer experiences across emerging markets.

### Why OnePay?

| WHAT SETS US APART | DETAILS |
| --- | --- |
| **Lowest Monthly Fee** | Starting at just LKR 499/month, more affordable than any competitor. |
| **Global Card Networks** | Directly integrated with Visa, Master, Amex, Dinners Club, Discover and UnionPay. |
| **Multi-Channel Payments** | Cards, mobile wallets - all in one. |
| **Plug-in Ready** | Native plugins for Shopify, WooCommerce, WHMCS, Odoo and more. |
| **Developer Friendly** | Clean RESTful APIs, iOS & Android SDKs, OnePay JS for embedded checkout. |
| **No-Code Billing** | OnePay Billing for subscriptions, recurring payments & automated invoicing. |
| **4+ Years of Trust** | Over LKR 10B processed · 4,500+ merchants · growing every day. |

# Who Can Use OnePay?

OnePay is built for a wide spectrum of Sri Lankan businesses. Whether you are a freelancer just starting out or a publicly listed company processing thousands of transactions a day, OnePay has a plan and a path for you.

### Supported Business Types

|  |  |
| --- | --- |
| **Individuals** (Freelancers & Professionals) | Designers, consultants, tutors, developers, and other independent professionals. |
| **Sole Proprietorships** | Single-owner businesses registered in Sri Lanka. |
| **Partnerships** | Formally registered partnership businesses. |
| **Clubs & Societies** | May have compliance restrictions; approval process may vary. |
| **Limited Liability Companies** (Pvt Ltd) | Most straightforward approval path for incorporated businesses. |
| **Publicly Quoted Companies** (PLC) | Full enterprise support with dedicated relationship management. |

**IMPORTANT:** Clubs & Societies may have additional compliance requirements. Required documents and approval processes may vary depending on the business type.

Register business with OnePay partners: [Click here.](#)

### Restricted Business Categories

Certain business types and models are not eligible for OnePay services due to card network compliance requirements and regulatory guidelines.

Unsupported Business Categories

* Gems & Jewellery business
* Unauthorised Software licence business
* Dating services
* Donation platforms
* Betting / Gambling

Unsupported Business Models

* Drop-shipping
* Print-on-demand
* Multi-vendor platforms

**NOTE:** If you are unsure whether your business qualifies, please reach out to our team at [support@onepay.lk](mailto:support@onepay.lk) before starting the onboarding process. We are happy to guide you.

# Getting Started - The Onboarding Journey

Getting set up with OnePay is straightforward. We've designed the process to be paperless, fast, and fully guided. Here is exactly what to expect from the moment you decide to move with OnePay.

### The 5-Step Onboarding Flow

| STEP | WHAT HAPPENS | WHO DOES IT |
| --- | --- | --- |
| 1 | You decide to join OnePay and contact our team or reach out through the website | You |
| 2 | We send you a document checklist. You gather and submit the required documents | You + OnePay Team |
| 3 | We review your documents and prepare the merchant agreement | OnePay Team |
| 4 | We send a digital signature request. You sign electronically or request a physical PDF copy from your Relationship Officer | You |
| 5 | We submit your application and website to the Bank for card network compliance clearance. Approval takes a maximum of 3 working days | OnePay Team |

**✓ TIP:** Once everything is approved, we will notify you immediately. The maximum turnaround time from submission to live approval is **3 working days**.

# Required Documents

The exact document requirements depend on your business type. Please refer to the specific category that applies to your business.

### 1. Individual / Freelancer & Sole Proprietorship

A side-by-side comparison of common and specific documents required for individuals and sole proprietorships.

| DOCUMENT | INDIVIDUAL / FREELANCER | SOLE PROP. |
| --- | --- | --- |
| National Identity Card (NIC) copy |  |  |
| Passport (if non-citizen) |  |  |
| Business Registration Certificate |  |  |
| Bank Account details (Bank verification document / Online banking statement) \* Must contain Bank Logo, Bank name, Account holder name, Account number (Less than 3 months old) |  |  |
| Utility Bill or Address Proof (For Passport holders: billing proof from Electricity/Water or Gramasewaka address verification) |  |  |
| Website or Social media page with pricing plan |  |  |
| Policies (Refund policy, Return policy, Privacy Policy) |  |  |
| Gramasewaka Certificate |  |  |
| Recent Education Qualification (Only for education category - should be in the same stream) |  |  |

### 2. Partnership

| DOCUMENT | REQUIRED |
| --- | --- |
| Business Registration Certificate |  |
| NIC copies of all Partners |  |
| Business Bank Account details |  |
| Business Logo |  |

### 3. Club & Society

| DOCUMENT | REQUIRED |
| --- | --- |
| Constitution / Articles of Association |  |
| Meeting Minutes (authorising payment gateway integration) |  |
| Billing Proof for address verification (Bank statement or Electricity bill) |  |
| Business Bank Account details |  |
| NIC copies of Secretary, Treasurer, and President individually |  |

### 4. Pvt Ltd / PLC

| DOCUMENT | REQUIRED |
| --- | --- |
| Certificate of Incorporation (Form 01) |  |
| Memorandum & Articles of Association (M&A) |  |
| Board Resolution for Payment Gateway (OnePay has a template available) |  |
| NIC copies of all Directors |  |
| Director Email addresses & Contact numbers |  |
| Business Bank Account details |  |
| Utility Bill or Address Proof for the registered office |  |
| Website or Social media page with pricing plan |  |
| Policies (Refund policy, Return policy, Privacy Policy) |  |

**NOTE:** Not sure what to submit? Contact your dedicated Relationship Officer and they will walk you through exactly what is needed for your specific business structure.

# Website Requirements Before Compliance Review

Before OnePay can submit your application to the Bank for card network clearance, your website must have the following policy pages and requirements in place. This is a mandatory requirement from the card networks (VISA, Mastercard, etc.) and is not optional.

### 1. Refund Policy

Your refund policy must clearly state the conditions under which customers can receive a refund, the refund timeframe, and the process to initiate a refund. It should be easy to find from your homepage or checkout page.

### 2. Privacy Policy

Your privacy policy must explain what personal data you collect from customers, how you use it, how it is stored, and how customers can request deletion. This is also required under Sri Lanka's Personal Data Protection Act.

### 3. Return Policy

If you sell physical products, your return policy must outline the conditions for accepting returns, the return window (e.g., 14 days), and whether the customer or merchant bears the return shipping cost.

### 4. Terms & Conditions

Your Terms & Conditions page sets out the legal agreement between your business and your customers. It must cover the scope of your products or services, payment terms, limitations of liability, dispute resolution process, and governing law. Card networks require that customers have access to your T&C at the point of checkout.

### 5. Contact Detail

Your website must display clear, accurate, and reachable contact information for your business. This is a key trust signal for both customers and the card networks during compliance review. Required contact details include:

* Business email address (a working inbox that is actively monitored)
* Physical business address (P.O. Box addresses are not accepted)
* Contact telephone number (a working number reachable during business hours)

Download sample policies: [Click](/guide/policy-samples)

Download resolution template: [Click](/guide/resolution-templates)

**IMPORTANT:** These policies and requirements must be live on your website before OnePay submits your application for card network compliance review. Compliance review is handled entirely by OnePay on your behalf — you just need the requirements in place.

**✓ TIP:** Need help drafting these policies? Our team can point you to free, customisable policy templates used by thousands of Sri Lankan merchants. Just ask your Relationship Officer.

# Payment Options & Supported Currencies

Accept payments from customers worldwide using cards, mobile wallets, and internet banking. Multi-currency support is built in, so you can get paid in the currencies your customers already use.

## Payment Methods

### Debit & Credit Cards

Card Payment

### Mobile Wallets

Mobile Payment

## Supported Currencies

OnePay supports **10 currencies**, enabling your business to collect payments from customers across the world. Settlement to your bank account is always in **LKR**. Foreign currency amounts are converted at the applicable FX rate at the time of the transaction.

This is especially useful for travel businesses, hotels, and tour operators. Multi-currency acceptance works well for any business serving international visitors to Sri Lanka. Contact your Relationship Officer to confirm which currencies are enabled on your merchant account.

Settlement always happens in LKR. When a customer pays in a foreign currency, the amount is converted to LKR using the FX rate at the time of the transaction. For refunds on foreign currency transactions, the FX rate used is the one applicable on the refund date, not the original transaction date.

| Currency Code | Currency Name |
| --- | --- |
| **LKR** | Sri Lankan Rupee |
| **USD** | US Dollar |
| **GBP** | British Pound |
| **EUR** | Euro |
| **AUD** | Australian Dollar |
| **JPY** | Japanese Yen |
| **INR** | Indian Rupee |
| **CHF** | Swiss Franc |
| **CAD** | Canadian Dollar |
| **SGD** | Singapore Dollar |

**This is especially useful for travel businesses, hotels, and tour operators.** Multi-currency acceptance works well for any business serving international visitors to Sri Lanka. Contact your Relationship Officer to confirm which currencies are enabled on your merchant account.

**This is especially useful for travel businesses, hotels, and tour operators.** Multi-currency acceptance works well for any business serving international visitors to Sri Lanka. Contact your Relationship Officer to confirm which currencies are enabled on your merchant account.

Please note that, as per guidelines issued by **CBSL**, Sri Lankan-based businesses are **not permitted to accept USD payments** from domestic customers. It is important to comply with these regulations to avoid any potential penalties.

For more information, please refer to the official CBSL notice:<https://www.cbsl.gov.lk/sites/default/files/cbslweb_documents/press/pr/press_20260212_foreign_currency_transactions_between_residents_of_srilanka_e.pdf>

# Pricing & Charges

OnePay believes in simple, transparent pricing. No hidden fees. No surprises. Here is everything you need to know.

Standard Plan

LKR 499.00 monthly

Payment processing fee is 3.50%

Features:

Accepts payment from Links, Plugins, API, SDK

* Team Access
* Accepts payment from Links, Plugins, API, SDK
* General Support
* Visa, Master, Amex and GooglePay payments
* Daily Payouts 2 days after payment
* Monthly Payment Limit LKR 100,000

Essential Plan

LKR 799.00 monthly

Payment processing fee is 3.25%

Features:

Everything in Standard Plan, plus

* Team Access
* Automated Charging - Card On File
* USD, GBP, EURO, INR, JPY acceptance and payout
* Accepts payment from Links, Plugins, API, SDK
* General Support
* Visa, Master, Amex and GooglePay payments
* Daily Payouts 2 days after payment
* Subscription waived-off limit LKR 500,000
* Monthly Payment Limit LKR 600,000

Elevate Plan

LKR 2,999.00 monthly

Payment processing fee is 2.75%

Features:

Everything in Essential Plan, plus

* Team Access
* Automated Charging - Card On File
* USD, GBP, EURO, INR, JPY acceptance and payout
* Accepts payment from Links, Plugins, API, SDK
* General Support
* Visa, Master, Amex and GooglePay payments
* Daily Payouts 2 days after payment
* Subscription waived-off limit LKR 2,000,000
* Monthly Payment Limit LKR 2,250,000

Premier Plan

LKR 5,999.00 monthly

Payment processing fee is 2.50%

Features:

Everything in Elevate Plan, plus

* Team Access
* Automated Charging - Card On File
* USD, GBP, EURO, INR, JPY acceptance and payout
* Accepts payment from Links, Plugins, API, SDK
* General Support
* Visa, Master, Amex and GooglePay payments
* Daily Payouts 2 days after payment
* Subscription waived-off limit LKR 3,000,000
* Unlimited Monthly Payment Limit

### Merchant Discount Rate (MDR)

In addition to the monthly subscription, a Merchant Discount Rate (MDR) applies to each transaction. The MDR is a small percentage of the transaction value retained to cover card network fees, bank processing costs, and platform maintenance. Your specific MDR will be confirmed in your merchant agreement and depends on your business category and transaction volume. Speak to your Relationship Officer for a personalised rate.

**✓ TIP:** The higher your monthly transaction volume, the more room there is to negotiate a better MDR. As your business scales, reach out to your Relationship Officer to review your rate.

### Other Charges

| CHARGE TYPE | DESCRIPTION |
| --- | --- |
| **Setup Fee** | Approximately LKR 1,500. This is required prior to proceeding with the application and agreement. The fee will be refunded if card network compliance is not approved. |
| **Subscription Payment** | Based on the selected package. |

# Payouts

Understanding how and when you receive your funds is critical for managing your business cash flow. OnePay makes this as transparent and predictable as possible.

### How Payouts Work

When a customer successfully completes a payment on your website, the funds are collected by OnePay's partner bank Custodian Account on your behalf and held in a settlement account. On your scheduled payout date, OnePay transfers the net amount transaction value minus MDR and any applicable fees directly to your registered bank account via a CEFT (Common Electronic Fund Transfer) transaction.

### Payout Schedule T+2

OnePay operates on a T+2 payout cycle, where T is the date the payment was accepted. The payout date must fall on a bank working day.

| Payment Accepted (T) | Payout Date (T+2) |
| --- | --- |
| Monday | Wednesday |
| Tuesday | Thursday |
| Wednesday | Friday |
| Thursday | Monday (next bank working day) |
| Friday | Tuesday (skipping weekend) |
| Saturday / Sunday | Counted from next bank working day |

QUICK FACT

Payout day is before 6:00 PM Sri Lanka Standard Time. You will receive your payout report on the same day at 6:00 PM but only on days when a payout is made.

### American Express (AMEX) Payout T+3

AMEX transactions follow a T+3 payout cycle. OnePay is currently working with our banking partner to bring the AMEX settlement timeline in line with Visa, Mastercard, and other payment methods. We will notify all merchants when this change takes effect.

### Your Daily Payout Report

On every payout day, OnePay sends you a comprehensive payout report by 6:00 PM. The report includes:

* A full breakdown of all transactions included in the payout
* The net payout amount transferred to your bank account
* The bank reference number for the CEFT transfer
* Any deductions (MDR, fees, chargeback recoveries)

You can use this report to tally the payout amount against your bank statement for reconciliation purposes. If you have not received your payout or payout report, please contact your OnePay Relationship Officer for clarification.

**NOTE** No payout? No report. The payout report is only sent on days when a payout is actually processed to your account.

### Payout Delays

Occasionally, payouts may be delayed due to factors outside OnePay's direct control. Known causes include:

* Bank system downtime or technical issues on the sending or receiving side
* CEFT network delays during peak banking hours
* Beneficiary bank (your bank) system downtime or maintenance
* Your bank account being placed in inactive mode by your bank

If a payout fails due to a beneficiary bank-side failure such as your bank's system being down or your account being inactive OnePay will inform you immediately and reschedule the payout for the next available payout cycle.

**IMPORTANT** To avoid failed payouts, ensure your registered bank account remains active and that your account details on file with OnePay are always up to date. Contact your Relationship Officer to update your bank account details.

### Payout Hold

OnePay may place a temporary hold on your payout in the following specific circumstances:

| Hold Reason | Explanation |
| --- | --- |
| **Unresolved Chargeback** | A chargeback has been raised against your account and is pending resolution. Funds may be held to cover the potential reversal amount. |
| **Business Nature Conflict** | A discrepancy has been identified between the business type agreed upon in your merchant agreement and the actual transactions being processed. |
| **Suspicious Transaction Flag** | One or more transactions have been identified as suspicious by the card networks (Visa, Mastercard, etc.) and are under review. |
| **Chargeback Recovery Due** | Outstanding chargeback fees or recovered amounts are owed and will be offset against your pending payout. |

If your payout is placed on hold, OnePay will notify you promptly with a clear explanation and the steps required to resolve it. Contact your Relationship Officer as soon as possible to expedite the resolution.

### Current Payout Limitations

| Feature | Status | Notes |
| --- | --- | --- |
| Early Payout (before scheduled date) | Not available | OnePay does not currently offer early or on-demand payout before the scheduled T+2 date. |
| Split Payout (partial amounts) | Not available | OnePay does not currently support splitting a single payout into multiple partial transfers. |

**NOTE** These features are on our product roadmap. We will announce availability through your merchant dashboard and via email when they become available.

**✓ TIP** The best way to avoid payout holds is to maintain clear product/service descriptions, respond promptly to customer queries, and keep your chargeback rate below 1% of monthly transaction volume.

# Refund Process

Handling refunds professionally and promptly is one of the most effective ways to maintain customer trust and avoid chargebacks. OnePay makes the refund process simple.

### When Should You Issue a Refund?

A refund should be issued when:

* 1. The customer did not receive the product or service they paid for
* 2. The product or service delivered was significantly different from what was described
* 3. A duplicate payment was made in error
* 4. The customer cancelled before fulfilment and is entitled to a refund per your policy
* 5. A technical error caused an incorrect charge
* 6. Item out of stocks

### How to Process a Refund

Refunds can be initiated directly from your OnePay merchant dashboard. The process is as follows:

|  |  |
| --- | --- |
| 7 | Log in to your OnePay Merchant Dashboard |
| 8 | Navigate to Transactions and locate the transaction to be refunded |
| 9 | Click Refund and enter the refund amount (full or partial refunds are supported) |
| 10 | Submit the refund request, it is reviewed and processed by OnePay |
| 11 | The customer receives the refund to their original payment method within the standard processing time |

### Refund Processing Timeframes

| Refund Type | Timeframe | Notes |
| --- | --- | --- |
| **Standard Refund** | 3-5 bank working days | Funds returned to customer's original payment method |
| **Mobile Wallet Refund** (Frimi, Qplus and Helapay) | 3-5 bank working days | Returned to the original wallet |

### What if There Are No Funds in Your Payout Account?

If your future payout balance or recent transaction volume is insufficient to cover the refund amount, OnePay will contact you and request that you deposit the required funds to initiate the refund

* For **local (LKR) transactions**: you deposit the exact refund amount to the OnePay designated account.
* For **foreign currency transactions**: you must deposit the equivalent amount in LKR, calculated at the applicable FX rate on the date the refund is being processed. OnePay will provide you with the account details and the applicable FX rate at that time.

**FOR MERCHANTS**  
Responding to refund requests within 24 hours significantly reduces the chance of a customer escalating to a chargeback, which is more costly and time-consuming for everyone.

### When Refunds Take Longer Than Expected

On rare occasions, refunds may take significantly longer than the standard timeframe due to bank reconciliation issues on the card issuer's side. In these cases, OnePay has no direct authority to follow up with the card-issuing bank on the cardholder's behalf.

If a refund has not appeared within the stated timeframe and the standard resolution steps have been exhausted, the cardholder should initiate a chargeback directly through their card-issuing bank.

### How to Fast-Track the Refund Process

One of the quickest ways to recover your payment is by raising a chargeback through your bank.

### What is a Chargeback?

A chargeback is a process where your bank reverses a transaction and refunds the amount back to your account, usually in cases of disputes such as cancellations or non-delivery of services.

### Steps to Raise a Chargeback:

|  |  |
| --- | --- |
| 1 | Contact your bank (Card Center via hotline). |
| 2 | Inform them that you would like to raise a chargeback for a transaction. |
| 3 | Provide the required transaction details (date, amount, merchant name, etc.). |
| 4 | Clearly state the reason as: "Event cancellation – refund not received." |
| 5 | Request and note down the reference number for your case. |

### What Happens Next?

The bank will process your request, and in most cases, the amount will be credited back to your account within a few working days.

**IMPORTANT**  
Keep checking your bank statements and follow up with your bank if needed.

# Understanding Chargebacks

A chargeback is when a customer contacts their bank or card issuer to dispute a transaction and request a forced reversal of funds **bypassing** the merchant entirely. Chargebacks are one of the most serious issues a merchant can face, and understanding them is essential.

### How a Chargeback Happens

Here is the typical chargeback flow:

|  |  |
| --- | --- |
| 1 | Customer disputes a transaction with their bank (e.g., claims they never received goods, or did not authorise the payment) |
| 2 | The issuing bank raises a chargeback and contacts OnePay through the card network |
| 3 | OnePay notifies you and requests evidence to dispute the chargeback |
| 4 | You submit evidence (order confirmation, delivery proof, customer communication, etc.) |
| 5 | The card network reviews the evidence and makes a final decision |
| 6 | If the decision favours the customer, the transaction amount plus a chargeback fee is debited from your account |

### Common Chargeback Reasons

| Reason Code | What It Means | Prevention Strategy |
| --- | --- | --- |
| **Item Not Received** | Customer claims they never got what they paid for | Always issue a tracking number; confirm delivery |
| **Item Not As Described** | Product or service differed from what was advertised | Use accurate, detailed product descriptions and images |
| **Unauthorised Transaction** | Customer claims they did not make the purchase | Enable 3D Secure (OTP) for all card payments |
| **Duplicate Transaction** | Customer was charged twice for the same item | Implement duplicate payment detection in your checkout |
| **Subscription Cancelled** | Customer was charged after cancelling a subscription | Ensure cancellation confirmations are sent immediately |

### How to Win a Chargeback Dispute

Evidence is everything. When OnePay notifies you of a chargeback, compile the following as quickly as possible:

* Order confirmation with date, amount, and product/service details
* Proof of delivery (courier tracking, digital delivery logs)
* Customer communication (emails, WhatsApp messages accepting delivery)
* Terms & conditions shown at checkout (including your refund and return policy)
* IP address and device fingerprint of the transaction (available from your dashboard)

**WARNING**  
The chargeback response window is typically 7-14 days from the date of notification. Missing this deadline means an automatic loss. Set up email alerts in your OnePay dashboard to ensure you never miss a notification.

### Chargeback Ratio - Keep It Low

Card networks (VISA, Mastercard) set strict thresholds for acceptable chargeback ratios. If your monthly chargeback rate exceeds these thresholds, your account may be flagged, suspended, or your merchant agreement terminated. The standard industry threshold is below 1% of monthly transactions.

**IMPORTANT**  
If your chargeback ratio starts climbing, contact OnePay immediately. We can work with you on fraud prevention settings, 3D Secure configuration, and customer communication strategies to bring the rate down.

# Business Verification & Compliance

OnePay is committed to operating **within** Sri Lanka's financial regulations and global card network standards. Part of this commitment involves periodic business verification for all **merchants on the** platform.

### Periodic Verification

OnePay may request updated business documents from you periodically, typically annually or when significant changes occur in your business. You will be notified in advance with a clear checklist of what is required and a reasonable deadline. Common triggers for a periodic verification request include:

* Annual KYB (Know Your Business) review
* Change in business ownership or directorship
* Change in business address or bank account
* Significant increase in transaction volume
* Expansion into new product categories

**IMPORTANT**  
Failing to respond to a verification request within the specified deadline may result in a temporary hold on your payout or account suspension. Always respond promptly to keep your account in good standing.

### Approval Scope - What OnePay Approves

It is important to understand that OnePay's approval covers only the initial business operations as declared in your merchant application and agreement. Your approval is scoped to the specific business type, product categories, and transaction nature you described during onboarding.

OnePay continuously monitors transaction activity on the platform. If transactions are identified that fall outside the agreed scope of your approved business operations, OnePay will flag those activities. This may result in:

* A formal notice requesting clarification on the nature of the transactions
* A temporary hold on your payout pending review
* Suspension of your merchant account while the matter is investigated
* In serious cases, termination of your merchant account

**IMPORTANT**  
Your approval is tied to what you declared at onboarding. If your business evolves, new products, new services, **new** business models always inform your Relationship Officer before processing those transactions. Getting ahead of this is far simpler than resolving a **compliance** issue.

### Processing Time & Status

You can track the status of your application and any pending verification at any time through your OnePay merchant dashboard or by contacting your Relationship Officer. Standard processing times are:

| Process | Typical Timeframe |
| --- | --- |
| New merchant application to live approval | Maximum 3 working days (from complete submission) |
| OnePay new approval | Maximum 1 working day |
| New Bank account add or change | Maximum 2 working **day** |
| Refund processing (standard) | 3-5 bank working days |
| Chargeback dispute response window | Based on the Cardnetwork time frame |

# Account Termination

OnePay reserves the right to terminate a merchant account in the following circumstances:

* Repeated breach of the merchant agreement terms
* Sustained high chargeback or fraud ratio exceeding card network thresholds
* Discovery that the business falls into a restricted category
* Failure to comply with document verification requests
* Fraudulent activity or misrepresentation
* Transacting outside the approved scope of business operations

In most cases, OnePay will attempt to work with the merchant to resolve the issue before proceeding to termination. If your account is at risk, you will receive a formal notice with a defined cure period.

### Consequences of Termination - What You Must Know

**WARNING** **This** is one of the most important sections in this guide. Please read it carefully.

If a merchant account is terminated due to a compliance breach or policy violation, the consequences extend far beyond losing access to OnePay. Here is what happens:

| Consequence | Details |
| --- | --- |
| **Card Network Notification** | OnePay is required to notify the relevant card networks (Visa, Mastercard, etc.) of the termination. This is a mandatory obligation under card network compliance rules. |
| **Business Flagging** | The card networks will flag your business in their global merchant databases. This flag is shared across all payment processors and acquiring banks worldwide. |
| **Director & Owner Impact** | All directors and owners of the business will be personally impacted. Their names and identification details are linked to the flagged business record. |
| **Future Gateway Applications** | The flag significantly affects, and in most cases prevents the directors and owners from successfully applying for a payment gateway with any other payment processor or acquiring bank in Sri Lanka and internationally. |
| **Bank Payment Gateway Access** | Bank-issued payment gateways are also subject to the same card network compliance databases. A flagged record will affect applications to bank payment gateway services **as well**. |

**WARNING**  
A termination flag is not a local issue — it travels with your business and your personal identity globally through the card network compliance systems. The best protection is simple: always operate within your approved business scope, maintain a low chargeback rate, and communicate proactively with your Relationship Officer when anything changes.

**NOTE**  
If you receive a termination notice and believe it is in error, contact our support team at **info@onepay.lk** within 5 business days. We will review the case and respond within 3 business days.

# 3D Secure - How OnePay Protects Every Transaction

All transactions processed through OnePay are secured using 3D Secure (3DS) authentication. OnePay does not support 2D (non-authenticated) transactions under any circumstances. Understanding the difference between 3DS and 2DS is important for both merchants and customers.

### What is 2D (Non-Authenticated) Payment?

A 2D transaction also called a non-3DS or card-not-present transaction is a basic payment where the customer enters their card number, expiry date, and CVV. There is no additional identity verification step. The payment is either approved or declined purely based on card data.

* No additional authentication required from the cardholder
* Faster checkout experience with fewer steps
* Higher fraud risk: stolen card details can be used to make purchases
* In the event of fraud, the liability falls on the merchant

### What is 3D Secure (3DS)?

3D Secure is a global authentication protocol developed by the card networks (Visa calls it **Verified by Visa**; Mastercard calls it **Mastercard Identity Check**). It adds an additional verification step after the customer enters their card details, typically a One-Time Password (OTP) sent to their registered mobile number by their issuing bank.

* The customer enters their card number, expiry date, and CVV
* The issuing bank sends a one-time password (OTP) to the customer's registered mobile number
* The customer enters the OTP to authenticate the payment
* Only after successful OTP verification does the transaction proceed

**QUICK FACT**  
OnePay mandates 3DS for ALL transactions. There are no exceptions. This protects you as a merchant from fraudulent transactions and liability disputes.

### 3DS vs 2DS - Risk Comparison

| Factor | 2D (Non-Authenticated) | 3D Secure (3DS) |
| --- | --- | --- |
| **Authentication** | Card details only (no OTP) | OTP verification via issuing bank |
| **Fraud Risk** | High: stolen cards can be used freely | Low: requires access to cardholder's phone |
| **Liability on Fraud** | Merchant bears full liability | Liability shifts to the issuing bank |
| **Chargeback Exposure** | High: merchant must defend all disputes | Significantly reduced: bank-authenticated transactions are harder to dispute |
| **Customer Experience** | Faster (fewer steps) | Slightly more steps but much safer |
| **OnePay Support** | Not supported | Mandatory for all transactions |

### 3DS Enabled vs Disabled Cards

Not all cards have 3DS enabled. The decision to enable or disable 3DS on a card rests entirely with the card-issuing bank, not with OnePay or the merchant.

### Cards with 3DS Disabled

Some issuing banks disable 3DS authentication on certain cards or for certain transaction types. Common scenarios include:

* Certain international cards where 3DS adoption is limited
* Specific card products designed for certain transaction categories
* Corporate or prepaid cards where OTP-based authentication is not configured

### Who Bears the Risk When 3DS is Disabled?

When a card does not support 3DS and a transaction is completed without authentication, the liability for any resulting fraud or dispute does **NOT** fall on the merchant. In this scenario:

* The card-issuing bank assumes full liability for the transaction
* The merchant is protected from chargebacks arising from fraudulent use
* This is a deliberate liability-shift policy enforced by Visa and Mastercard

**✓ TIP**  
As a merchant on OnePay, you are never required to take action based on whether a customer's card has 3DS enabled or disabled. OnePay's system automatically handles the authentication flow.

**NOTE**  
If a customer did not receive an OTP during checkout, this is most likely a 3DS configuration issue with their issuing bank **not** an OnePay issue. Ask the customer to contact their bank to enable 3DS, or to try a different card.

---

## Policy Sample Documents

**Category**: Guides  
**Source URL**: https://docs.onepay.lk/guide/policy-samples

# Policy Samples

### What are Policy documents?

When you accept payments Online from your customers, you need to inform them about your business policies such as what is your delivery period, how you accept returns & issue refunds, how you handle their personal data & etc.

Policy documents are displayed in websites/apps to inform these business policies to your customers in an informative way.

### What are the Policy documents I need to display?

You need to have the following Policy documents clearly displayed on your website/app for your customers' reference:

* Refund Policy
* Privacy Policy
* Terms & Conditions

**IMPORTANT:** Your Onepay Activation will be rejected by our partner banks if you do not have them in place.

### How should I display them?

You may display them in separate pages in your website/app & include links to those pages in your landing page (usually in the footer).

You can refer the following examples documents. Please note that these example documents are provided as general guideline & you need to draft your own documents to suit your business.

**Note:** Please make sure to replace the **highlighted** words with your details if you copy them.

# Sample Refund Policy

Copy Policy

### Refund Policy

Thank you for shopping at **[Your eCommerce Website]**. We value your satisfaction and strive to provide you with the best online shopping experience possible. If, for any reason, you are not completely satisfied with your purchase, we are here to help.

#### Returns

We accept returns within **[X]** days from the date of purchase. To be eligible for a return, your item must be unused and in the same condition that you received it. It must also be in the original packaging.

#### Refunds

Once we receive your return and inspect the item, we will notify you of the status of your refund. If your return is approved, we will initiate a refund to your original method of payment. Please note that the refund amount will exclude any shipping charges incurred during the initial purchase.

#### Exchanges

If you would like to exchange your item for a different size, color, or style, please contact our customer support team within **[X]** days of receiving your order. We will provide you with further instructions on how to proceed with the exchange.

#### Non-Returnable Items

Certain items are non-returnable and non-refundable. These include:

* Gift cards
* Downloadable software products
* Personalized or custom-made items
* Perishable goods
* Damaged or Defective Items

In the unfortunate event that your item arrives damaged or defective, please contact us immediately. We will arrange for a replacement or issue a refund, depending on your preference and product availability.

#### Return Shipping

You will be responsible for paying the shipping costs for returning your item unless the return is due to our error (e.g., wrong item shipped, defective product). In such cases, we will provide you with a prepaid shipping label.

#### Processing Time

Refunds and exchanges will be processed within **[X]** business days after we receive your returned item. Please note that it may take additional time for the refund to appear in your account, depending on your payment provider.

#### Contact Us

If you have any questions or concerns regarding our refund policy, please contact our customer support team. We are here to assist you and ensure your shopping experience with us is enjoyable and hassle-free.

# Sample Privacy Policy

Copy Policy

### Privacy Policy

At **[Your eCommerce Website]**, we are committed to protecting the privacy and security of our customers' personal information. This Privacy Policy outlines how we collect, use, and safeguard your information when you visit or make a purchase on our website. By using our website, you consent to the practices described in this policy.

#### Information We Collect

When you visit our website, we may collect certain information about you, including:

* Personal identification information (such as your name, email address, and phone number) provided voluntarily by you during the registration or checkout process.
* Payment and billing information necessary to process your orders, including credit card details, which are securely handled by trusted third-party payment processors.
* Browsing information, such as your IP address, browser type, and device information, collected automatically using cookies and similar technologies.

#### Use of Information

We may use the collected information for the following purposes:

* To process and fulfill your orders, including shipping and delivery.
* To communicate with you regarding your purchases, provide customer support, and respond to inquiries or requests.
* To personalize your shopping experience and present relevant product recommendations and promotions.
* To improve our website, products, and services based on your feedback and browsing patterns.
* To detect and prevent fraud, unauthorized activities, and abuse of our website.

#### Information Sharing

We respect your privacy and do not sell, trade, or otherwise transfer your personal information to third parties without your consent, except in the following circumstances:

* **Trusted service providers:** We may share your information with third-party service providers who assist us in operating our website, processing payments, and delivering products.
* **Legal requirements:** We may disclose your information if required to do so by law or in response to valid legal requests or orders.

#### Data Security

We implement industry-standard security measures to protect your personal information from unauthorized access, alteration, disclosure, or destruction. However, please be aware that no method of transmission over the internet or electronic storage is 100% secure.

#### Contact Us

If you have any questions, concerns, or requests regarding our Privacy Policy or the handling of your personal information, please contact us using the information provided on our website.

# Sample Terms & Conditions

Copy Policy

### Terms and Conditions

Welcome to **[Your eCommerce Website]**. These Terms and Conditions govern your use of our website and the purchase and sale of products from our platform. By accessing and using our website, you agree to comply with these terms.

#### 1. Use of the Website

* You must be at least **[X]** years old to use our website or make purchases.
* You are responsible for maintaining the confidentiality of your account information.
* You agree to provide accurate and current information during the registration and checkout process.
* You may not use our website for any unlawful or unauthorized purposes.

#### 2. Product Information and Pricing

* We strive to provide accurate product descriptions, images, and pricing information.
* Prices are subject to change without notice.

#### 3. Orders and Payments

* By placing an order, you are making an offer to purchase the selected products.
* We reserve the right to refuse or cancel any order for any reason.
* You agree to provide valid and up-to-date payment information.

#### 4. Intellectual Property

All content and materials on our website are protected by intellectual property rights and are the property of **[Your eCommerce Website]** or its licensors.

#### 5. Limitation of Liability

In no event shall **[Your eCommerce Website]**, its directors, or affiliates be liable for any indirect, incidental, or consequential damages arising out of your use of our website.

---

## Board Resolution Templates

**Category**: Guides  
**Source URL**: https://docs.onepay.lk/guide/resolution-templates

# Board Resolution Templates

### What is a Board Resolution?

A Board Resolution is a formal document that records decisions made by a Private Limited (Pvt Ltd) Company's Board of Directors. For Onepay merchant onboarding, acquiring partner banks (such as Hatton National Bank PLC and Seylan Bank PLC) require a formal board resolution authorizing your company to enter into a Merchant Agreement.

This document confirms that your company is legally authorized to process online payments, accept credit/debit card transactions, and nominate authorized directors to execute merchant agreements on behalf of the entity.

### Submission Guidelines

Please adhere to the following checklist before submitting your Board Resolution document to Onepay or partner banks:

* **Company Letterhead:** Print the completed resolution on your official company letterhead.
* **Director Signatures:** Must be signed in ink by authorized Directors as stated in your Form 1 / Form 20 documents.
* **Company Seal:** Affix your official company rubber stamp or common seal over the signatures.
* **Secretary Certification:** Ensure the Company Secretary or Chairman signs the extract certification at the bottom.

**IMPORTANT:** Onepay merchant activation cannot be completed without a valid, signed, and stamped Board Resolution submitted for your nominated acquiring bank.

# Hatton National Bank (HNB) Resolution

Standard Board Resolution format for merchants acquiring payments via HNB PLC.

**Tip:** Use the **Customize Details** button to fill in your company details live, or click **Download PDF** / **Download .DOCX** for offline editing.

HNB

### HNB Board Resolution

PVT LTD Merchant Affiliation Resolution

Customize DetailsCopy Text[Download .DOCX](/downloads/templates/HNB_Board_Resolution_Template.docx)Download PDF

## Board Resolution

Merchant Affiliation (HNB)

An extract from the Minutes of the Meeting of the Board of Directors of [Company Name] held at [Company Address] on this day of 08th day of July 2026.

Present:

1. [Director 1 Name]

2. [Director 2 Name]

It is hereby resolved that [Company Name], a Company duly incorporated under the laws of Sri Lanka and having its registered office at [Company Address] in Democratic Socialist Republic of Sri Lanka, enter into a Merchant Agreement with Spemai Pvt Ltd, having its Registered Office at No 292, Gamsabha Junction, High-level Road, Nugegoda, as an Accredited Dealer (Merchant) to accept and honour all valid MasterCards, Visa Cards issued by the Hatton National Bank PLC and or any other Bank MasterCards, China Union Pay and Visa Cards in favour of their customers and any other account to account Bank transactions.

It is further resolved that this company shall adhere to all the terms and conditions specified in the Merchant Agreement to be executed with Hatton National Bank PLC.

For this purpose, to sign, seal, execute and deliver to the Hatton National Bank PLC the application and the Merchant Agreement and any other documents required by the Hatton National Bank PLC from time to time and that every such sealing be attested by 1 Director of the Company.

Signed and sealed in the presence of:

(Signature)

Director 1

Name: [Director 1 Name]

(Signature)

Director 2

Name: [Director 2 Name]

Chairman / Company Secretaries

I certify that the above is a true extract from the recorded minutes of the Company.

(Signature)

Chairman or Company Secretary

# Seylan Bank Board Resolution

Standard Board Resolution format for merchants acquiring payments via Seylan Bank PLC.

**Tip:** Use the **Customize Details** button to fill in your company details live, or click **Download PDF** / **Download .DOCX** for offline editing.

Seylan Bank

### Seylan Bank Board Resolution

PVT LTD Merchant Affiliation Resolution

Customize DetailsCopy Text[Download .DOCX](/downloads/templates/Seylan_Board_Resolution_Template.docx)Download PDF

## Board Resolution

Merchant Affiliation (Seylan Bank)

An extract from the Minutes of the Meeting of the Board of Directors of [Company Name] held at [Company Address] on this day of 16th day of March 2026.

Present:

1. [Director 1 Name]

2. [Director 2 Name]

It is hereby resolved that:

The company does enter into a Merchant Agreement with Seylan Bank PLC as an Accredited Dealer/ Merchant to accept and honor all valid VISA/MasterCard International Cards issued by the Licensed Issuing Banks in favor of their customers. It is also further resolved that the company shall adhere to all the terms and conditions specified in the Merchant Agreement.

That for this purpose the company does sign, seal, execute and deliver to the Seylan Bank PLC from time to time all such instruments and documents of whatsoever nature or description as may be required by Seylan Bank PLC and that every such sealing be attested by 1 director of the company.

By this resolution the company does hereby warrant, represent, confirm and declare that in terms of the Memorandum and Articles of Association of the Company, the company is duly authorized to enter into an agreement as resolved above and is acting intra vires in doing so.

I certify that the above is a true extract from the recorded minutes of the company.

(Signature)

Director 1

Name: [Director 1 Name]

(Signature)

Director 2 / Secretary

Name: [Director 2 Name]

---

## Merchant System User Guide

**Category**: Guides  
**Source URL**: https://docs.onepay.lk/user-guide

13 Steps to Go Live

# Merchant Onboarding

Everything you need to create your OnePay account, configure your integration, and start accepting live payments on Sri Lanka's leading ISO 27001 certified payment gateway.

# Phase 1 — Account Setup

1. ### Set Your Password

   You will receive an email from **noreply@onepay.lk** to complete your merchant registration. Check your spam folder if you do not see it in your inbox. Click "Click Here" in the email to set your password.

   

   Registration Email Screenshot (Replace with screenshot showing the 'Click Here' email)

   Your password must meet the following requirements:

   * 8 to 128 characters
   * One uppercase letter (A–Z)
   * One lowercase letter (a–z)
   * One number (0–9)
   * One special character

   

   Password Setup Screen (Replace with the Merchant Registration password form screenshot)

   Enter your password, confirm it, and click **Submit** to complete the registration step.
2. ### Go to the OnePay Website

   Visit the OnePay website to access the merchant portal login page.

   

   OnePay Homepage — 'Payments Made Simple for Growing Business'

   Bookmark **onepay.lk** for quick access to your merchant portal at any time.
3. ### Log In to the Merchant Portal

   Enter your registered **User Email** and the **Password** you set in Step 2. Click the **Login** button to enter your dashboard.

   

   Merchant Portal Login Screen (Replace with login page screenshot)

   * Enter your Email here
   * Enter your Password here
   * Click Login

   Use **Forgot Password** on the login screen if you need to reset your credentials at any time.

# Phase 2 — Developer Configuration

1. ### Merchant Dashboard Overview

   After logging in, you will land on the Overview dashboard. Key metrics are visible at a glance:

   * Transaction Volumes
   * Recent Transaction
   * Today's Sales
   * Last Payout
   * Pending Payout

   

   Merchant Dashboard Overview Screenshot
2. ### Navigate to Developer Configurations

   Scroll down in the left sidebar and click **Developer Configurations** to expand the section. Then click **IPG Apps** from the sub-menu.

   

   Left Sidebar — Developer Configurations Expanded
3. ### Update Developer Details

   In the IPG Apps section, fill in your developer profile fields and click **Update** to save.

   * Developer Name
   * Developer Email
   * Developer Phone

   

   IPG Apps — Developer Details Form

# Phase 3 — App Creation and Configuration

1. ### Add a New App

   Click the **Add New App** button in the top right of the IPG Apps section. A dialog will appear to configure your integration.

   

   IPG Apps — Add New App Button
2. ### Configure the New App

   In the "App New App" dialog, complete the following fields: **App Name**, **Description**, and select all payment services your integration requires.

   * Mastercard / Visa LKR
   * Mastercard / Visa USD
   * American Express LKR
   * FriMi
   * HelaPay
   * QPlus

   

   App New App Dialog — Full Form
3. ### Set Callback URL and Token

   Under **Status Callback Configuration**, provide the two values that let OnePay communicate payment results to your system:

   **URL** — the endpoint on your server that receives payment status notifications (e.g. `https://yoursite.lk/payment/callback`)

   **Callback Token** — a secret key to validate that incoming callbacks are genuinely from OnePay

   

   Status Callback Configuration Section
4. ### Submit the App

   Click **Add** to create the app. It appears in your IPG Apps list with status **On Development**. Click the three-dot menu (⋮) on the app card to access:

   * View — App ID, Token, Hash Salt
   * Update — Modify app settings
   * Deactivate — Disable the app
   * Request to go Live

   

   App Card — 'On Development' Status with Three-Dot Menu

   Click **View** to retrieve the App ID and App Token needed for API integration in your codebase.

# Phase 4 — Go Live Approval

1. ### Request to Go Live

   Once your integration and testing are complete, open the three-dot menu on your app card and select **Request to go Live**.

   In the dialog, enter a star (\*) in the CIDR permission field to allow all IP addresses, or enter specific IPs for tighter security control.

   

   'Request to Go Live' Dialog

   After you request to go live, you cannot modify the app without OnePay administrator permission.
2. ### Agree and Submit

   Check the box to agree with the OnePay Payment Gateway Terms and Conditions. Click **Request To Go Live**.

   Your app status will update. The OnePay team will review and approve your request.

   

   Terms Checkbox and 'Request To Go Live' Button

   On Development→Pending Approval→Live

   Once approved, your integration is live and ready to process real payments. Maximum turnaround is 3 working days.

# How to Upgrade Your Package

1. ### Go to Account Settings

   From the main dashboard, scroll down the left sidebar and click **Account Settings**.

   

   Account Settings Sidebar
2. ### Open Billing and Subscription

   Under Account Settings, click **Billing and Subscription**.

   

   Billing and Subscription Menu
3. ### Update Payment Card Details

   Provide your card details so they can be securely tokenised for automated subscription payments.

   

   Update Payment Card Details Form

   The tokenization flow will prompt you to save your card securely. Please avoid using People's Bank, BOC, NSB, or Amex cards for tokenization. A nominal LKR 5.00 charge is made and reversed upon completion.
4. ### Select a Package

   Choose the plan that best fits your business and click the **Get Started** button.

   Standard

   LKR 499/mo

   3.50% processing fee

   * Visa, Master, Amex, QR
   * General Support
   * Daily Payouts T+2
   * Monthly limit 100K

   Essential

   LKR 799/mo

   3.25% processing fee

   * USD acceptance + payouts
   * Visa, Master, Amex, QR
   * Daily Payouts T+2
   * Limit waived to 500K

   Elevate

   LKR 2,999/mo

   2.75% processing fee

   * USD acceptance + payouts
   * Visa, Master, Amex, QR
   * Daily Payouts T+2
   * Limit waived to 2M

   Premier

   LKR 5,999/mo

   2.50% processing fee

   * USD acceptance + payouts
   * Visa, Master, Amex, QR
   * Daily Payouts T+2
   * Limit waived to 3M

   

   Billing and Subscription — Package Selection Page

---

# Blog / Technical Articles

## What Is Card-on-File? Merchant Guide

**Category**: Blog / Technical Articles  
**Source URL**: https://docs.onepay.lk/blogs/card-on-file

# What Is Card-on-File? A Complete Guide for Sri Lankan Merchants

Card-on-file lets your customers save their card details once and pay with a single click on every future visit. It powers subscriptions, faster checkouts, and recurring billing. When implemented correctly through OnePay, it does all of this without your business ever touching raw card data.

## What Is Card-on-File?

Card-on-file is a payment arrangement where a customer authorises a merchant to store their card details for use in future transactions. Instead of re-entering a 16-digit card number, expiry date, and CVV on every visit, the details are stored securely and mapped to a token. A token is a randomised reference string that represents the card without exposing it.

You have almost certainly experienced this as a customer. When a streaming service charges you every month without asking for your card again, or when you check out on an e-commerce site and see **"Pay with saved card ending 3301"**, that is card-on-file at work.

##### Quick Fact

Card-on-file transactions do not store your customer's actual card number. What is stored is a **token**: a secure reference that is useless to anyone who intercepts it. Only OnePay's payment infrastructure can resolve a token back to a card for authorisation.

## How Card-on-File Works on OnePay

When a customer saves their card on your OnePay-powered checkout, here is what happens behind the scenes:

1

### Customer enters card details at checkout

The card number, expiry date, and CVV are entered once on the OnePay checkout page. These details are encrypted in the customer's browser before they ever reach any server, including OnePay's.

2

### 3D Secure authentication completes

OnePay mandates 3DS for all transactions. The customer receives a One-Time Password from their issuing bank and confirms their identity. This step is required before any card can be saved.

3

### OnePay creates a token

After successful authentication, OnePay's vault generates a unique token for that customer-merchant combination. Your system receives the token, not the raw card data. You store the token, which by itself is worthless to attackers.

4

### Future payments use the token

On the customer's next purchase, you pass the token to OnePay's API. OnePay resolves the token, re-authenticates where required, and processes the payment. The customer gets a one-click checkout experience.

5

### You receive instant confirmation

Your system receives a payment result via OnePay's webhook callback. The transaction is complete. No card data was ever stored on your server.

##### PCI DSS Scope Reduction

Because raw card data never touches your server, only tokens do, your PCI DSS compliance scope is significantly reduced. OnePay handles the sensitive data in its secure vault, and your obligation shifts to the much simpler SAQ A self-assessment questionnaire.

## Types of Card-on-File Transactions

Not all card-on-file payments are the same. Visa and Mastercard classify COF transactions into distinct types, and OnePay's API supports all of them. Understanding the difference matters because each type has different authentication, liability, and compliance implications.

| Transaction Type | Who Initiates | Schedule | Example |
| --- | --- | --- | --- |
| **One-click / Saved Card** | Customer (CIT) | On demand | Returning shopper selects "Pay with saved card" at checkout |
| **Recurring (Fixed)** | Merchant (MIT) | Fixed intervals | Monthly subscription at LKR 999, charged every 1st of the month |
| **Recurring (Variable)** | Merchant (MIT) | Fixed intervals, variable amount | Utility bill collected monthly at varying amounts |
| **Unscheduled COF** | Merchant (MIT) | Non-fixed, triggered by event | Auto top-up when wallet balance drops below LKR 500 |
| **Instalment** | Merchant (MIT) | Fixed, pre-agreed number of charges | Three-instalment payment plan for a LKR 30,000 product |

**CIT (Cardholder-Initiated Transaction):** The customer is present and actively initiates the payment. 3DS authentication is typically required.

**MIT (Merchant-Initiated Transaction):** The merchant initiates the charge without the customer being present, based on a prior agreement. Authentication requirements differ and liability rules apply.

##### Merchant-Initiated Transactions in Sri Lanka

MIT capability via OnePay requires specific enablement on your merchant account. Contact your OnePay Relationship Officer to discuss recurring billing and subscription use cases before building your integration.

## Who Should Use Card-on-File?

Card-on-file is not just for large enterprise merchants. Any OnePay merchant with repeat customers, whether you sell courses, software subscriptions, memberships, or physical products, can benefit from implementing COF.

#### Education and Tuition

Charge monthly tuition fees automatically. Parents register once and fees are collected on the same date every month without manual follow-up.

#### E-commerce

Returning customers skip re-entering card details. One-click checkout reduces abandonment at the payment step significantly.

#### SaaS and Software

Charge monthly or annual licence fees automatically. Integrate with OnePay Billing to manage subscription lifecycles end-to-end.

#### Travel and Hospitality

Save card at booking to charge no-show fees or complete balance payments closer to the date without customer intervention.

#### Gyms and Memberships

Monthly membership dues collected automatically. Reduce failed payments from card expiry using OnePay's account updater capability.

#### Healthcare and Services

Save card on file for recurring consultations, therapy sessions, or service retainer agreements with patient or client consent.

## Tokenization: The Technology Behind COF

Tokenization is the process that makes card-on-file secure. When a customer saves their card, the raw card number (Primary Account Number) is never stored in your system. Instead, OnePay generates a **token**: a random alphanumeric string that acts as a secure reference to the original card.

### Token Types

| Token Type | Stored By | How It Works |
| --- | --- | --- |
| **Gateway Token (OnePay Vault)** | OnePay | OnePay stores the encrypted card and returns a reference token to your system. This is the most common COF implementation. |
| **Network Token** | Card Scheme (Visa / Mastercard) | Generated at the card network level. Survives card replacements and expiry updates automatically. Produces higher authorisation rates. |

### Token Lifecycle

A token is not permanent. It has a lifecycle that you need to manage as a merchant.

| Event | What Happens to the Token | Your Action |
| --- | --- | --- |
| **Customer saves card** | Token created and returned via API or webhook | Store the token against the customer record in your system |
| **Card expires** | Token may become invalid | Prompt customer to update card, or use OnePay's account updater |
| **Card replaced (lost or stolen)** | Token becomes invalid for old card | Customer re-saves new card; a new token is issued |
| **Customer requests deletion** | Token deleted from OnePay vault | Remove token from your database; do not attempt further charges |
| **Merchant account closed** | All tokens for that merchant are purged | Export token references before account closure if needed for reconciliation |

## COF vs. Standard Payment: A Direct Comparison

With Card-on-File

### Frictionless checkout experience

* ✓ Customer checks out in one click
* ✓ No re-entry of card details
* ✓ Subscriptions run automatically
* ✓ Fewer abandoned carts at the payment step
* ✓ Tokens survive most card replacements with network tokens
* ✓ Your server never stores raw card data
* ✓ Reduced PCI DSS compliance burden

Without Card-on-File

### Standard high-friction checkout

* ✗ Customer re-enters all card details every time
* ✗ Subscriptions require manual payment each cycle
* ✗ Higher payment abandonment at checkout
* ✗ No automated recurring billing possible
* ✗ Card expiry causes failures with no recovery path
* ✗ Poor experience for loyal, returning customers

## Integrating Card-on-File with OnePay

Card-on-file is available to merchants using **OnePay Checkout (hosted)** or the **OnePay API (custom integration)**. The path you take depends on your technical setup.

### OnePay Hosted Checkout

The simplest path. OnePay's checkout page handles the entire save-card flow, consent capture, tokenisation, and 3DS authentication. You receive the token via webhook. There is no PCI DSS scope impact on your servers.

##### Token Storage Rule

You must store the token with a **unique customer reference** (`customer_ref`) in your system. This reference links the token to a specific customer. Do not reuse the same customer reference across different customers. If you delete a customer's data from your system, you must also request token deletion from OnePay.

## Security, Compliance, and Consent

### Getting Explicit Customer Consent

Before saving a customer's card, you must obtain clear, informed consent. This is required by both card network rules (Visa and Mastercard) and Sri Lanka's Personal Data Protection Act. The consent must explain the following:

| What to Disclose | Example Wording |
| --- | --- |
| **What is being saved** | "Save my card for future purchases" |
| **How it will be used** | "Your card will be charged automatically each month for your subscription" |
| **How to revoke consent** | "You can remove your saved card at any time from your account settings" |
| **Who stores the data** | "Your card details are securely stored by OnePay and never held on our servers" |

### Liability and 3DS

For the initial card-saving transaction, OnePay mandates **3D Secure (3DS) authentication**. This is non-negotiable. The 3DS step creates the cardholder's binding consent and triggers the liability shift: if a fraudulent transaction occurs on a 3DS-authenticated card, the liability rests with the card-issuing bank, not with you as the merchant.

For subsequent MIT transactions where the customer is not present, authentication requirements are different. OnePay handles this automatically when you correctly flag the transaction type in your API request.

##### Chargeback Protection

COF transactions where the initial save was 3DS-authenticated are significantly harder for customers to dispute as "unauthorised." The 3DS authentication record is your evidence that the cardholder was present and consented. Always retain the original transaction reference linking the saved card to the 3DS event.

## Frequently Asked Questions

### Does card-on-file work with all card types on OnePay?

Card-on-file works with Visa and Mastercard debit and credit cards on OnePay. AMEX, Diners Club, and UnionPay support depends on the specific card product and issuing bank configuration. If you are building a subscription product, test your integration with both Visa debit and credit cards, as these represent the majority of Sri Lankan cardholders.

### Can a customer save multiple cards?

Yes. Each saved card generates a unique token. Your system can store multiple tokens per customer reference and present them as options at checkout, for example "Visa ending 3301" or "Mastercard ending 7890". The customer selects which card to charge.

### What happens when a saved card expires?

OnePay will mark the token as expired. Any attempt to charge an expired token will return a decline. You should implement a flow in your application to detect expired tokens ahead of time using the `card_expiry` field returned when the token was created, and prompt customers to update their card before the expiry date.

### Is OTP required for every saved card payment?

For customer-initiated transactions where the customer is present at checkout, 3DS OTP is required. For merchant-initiated transactions such as subscriptions and auto-billing where the customer is not present, OTP is not prompted. The original card-save must have been 3DS-authenticated. OnePay handles this distinction automatically when you set the correct `transaction_type` in your API request.

### How does OnePay handle card-on-file if the customer's bank blocks e-commerce?

If the customer's bank blocks the initial card-save transaction with Response Code 05 (Do Not Honour), the token cannot be created. The customer will need to enable online payments with their bank first, then re-attempt saving their card. [Read our full guide on Response Code 05 →](/blogs/do-not-honour)

### Who is responsible if a fraudulent charge occurs on a saved card?

If the initial card-save was 3DS-authenticated, which OnePay mandates, the liability for fraudulent charges on subsequent MIT transactions shifts to the card-issuing bank, not the merchant. This is one of the most important benefits of OnePay's 3DS-mandatory policy. Always keep the original transaction reference from the card-save event as your evidence record.

---

## OnePay Enables Google Pay in Sri Lanka

**Category**: Blog / Technical Articles  
**Source URL**: https://docs.onepay.lk/blogs/onepay-google-pay-press-release

@keyframes checkout-float {
0%, 100% { transform: translateY(0); }
50% { transform: translateY(-8px); }
}

Press Release

Colombo, Sri Lanka

# OnePay Brings Google Pay to Sri Lanka's Grassroots Businesses Through Its Unified Checkout

Spemai Pvt Ltd, the Japanese funded technology company behind OnePay, has enabled Google Pay across its Unified Checkout, giving home based sellers and listed companies alike a faster, more familiar way to get paid online.

For immediate release. Issued by **OnePay**, a product of **Spemai Pvt Ltd**.

OnePay, Sri Lanka's payment gateway built for businesses of every size, has activated Google Pay support on its Unified Checkout. The update means any business already using OnePay can accept Google Pay payments today, with no additional setup, no new integration, and no extra cost.

For a country where digital payment habits are still forming outside the capital, this is a small technical update with a large practical effect. A tuk-tuk driver's wife running a home bakery in Kurunegala and a publicly listed retail chain in Colombo now share the exact same checkout technology. Both can offer their customers a one-tap Google Pay option, the same experience shoppers already trust on the world's largest platforms.

### Why This Matters for Sri Lanka

Sri Lanka's digital payment landscape has grown quickly over the past five years, but adoption has remained uneven. Larger, urban businesses moved early. Smaller, home based, and rural businesses were often left waiting for tools built with them in mind.

OnePay was built to close that gap from day one. **Enabling Google Pay on the same checkout used by a home seller and a PLC company is a deliberate choice, not a coincidence.** It reflects how OnePay has approached every product decision since launch: build it once, build it well, and make it available to everyone on the platform at the same time.

"This is not just a new payment button. It is proof that grassroots businesses in Sri Lanka deserve the same checkout technology as the largest companies in the country. That has been the whole premise of OnePay from the start."

**Spemai Pvt Ltd**, on the Google Pay rollout

### Five Years Building Sri Lanka's Payment Infrastructure

Spemai Pvt Ltd has spent five years building OnePay into one of the country's most widely used payment platforms. Backed by Japanese investment since its early days, the company has focused on a single mission: make digital payments simple enough for a home business to adopt on day one, and robust enough for a publicly listed company to depend on at scale.

5

Years building Sri Lanka's digital payment infrastructure

~5,000

Businesses powered, from home sellers to PLCs

1st

Sri Lankan gateway to unify Google Pay across every merchant tier

That track record is what makes this announcement more than a feature update. OnePay has spent half a decade earning the trust required to bring a product like Google Pay to the grassroots level, not just to the businesses that could already afford modern payment infrastructure.

### More Than a Checkout: Automation Built In

OnePay's role in a business does not end at the payment confirmation screen. The platform connects directly into the tools businesses already run on, including Zapier, n8n, accounting software, ERPs, and a wide range of industrial systems used across Sri Lanka's commercial sector.

#### What This Means in Practice

* **A payment received through Google** Pay can automatically trigger an invoice in your accounting software.
* **Order data can flow directly** into an ERP without manual entry.
* **Zapier and n8n workflows let** businesses connect OnePay to hundreds of other tools without writing code.
* **Industrial and enterprise software integrations** support businesses operating at scale.

For a small business, this means a payment is not the end of the admin work. It is the start of an automated process that used to take hours of manual reconciliation. For a larger company, it means OnePay can sit inside an existing technology stack rather than requiring one to be rebuilt around it.

### One Checkout, Every Business

Google Pay joins OnePay Unified Checkout alongside Visa, Mastercard, American Express, and local mobile wallets including FriMi, QPlus, and HēlaPay. Every payment method appears on the same branded page, regardless of which OnePay merchant a customer is paying.

That consistency is central to what OnePay is trying to build. A customer who has used Google Pay to buy groceries should be able to use it just as easily to pay a home baker, book a guesthouse, or settle an invoice with a large distributor. The technology should not change depending on the size of the business behind it.

### What Comes Next

OnePay continues to expand its merchant network across Sri Lanka, with a continued focus on bringing modern payment and automation tools to businesses that have historically been underserved by traditional financial infrastructure. The Google Pay rollout is part of a broader roadmap to keep OnePay's checkout aligned with how people actually want to pay, both in Colombo and far beyond it.

## Start Accepting Google Pay Today.

Offer your customers the fast, familiar checkout experience they expect. Built directly into OnePay Unified Checkout with no extra integration required.

[Talk to our team](https://www.onepay.lk/contact-us)

---

## Sri Lanka Wellness Tourism Report 2026

**Category**: Blog / Technical Articles  
**Source URL**: https://docs.onepay.lk/blogs/wellness-tourism-report

#1

World's Top Trending Wellness Destination, 2026

# Sri Lanka Just Won Wellness Tourism. *Is Your Checkout Ready for the Guests It Brings?*

BookRetreats.com ranked Sri Lanka first in the world for wellness travel demand growth. Arrivals are at a record high. But most of the country still runs on cash. Here is the data, and what it means for tourism businesses.

+100%

YoY wellness travel demand growth

2.36M

Tourist arrivals in 2025

90-95%

Of transactions still in cash

### The World Just Noticed Sri Lanka's Wellness Industry

In June 2026, BookRetreats.com published its State of Retreats 2026 Report. It ranked Sri Lanka as the world's top trending wellness destination, ahead of Australia, Morocco, England, and Spain. The number behind that ranking is striking: wellness traveller demand for Sri Lanka grew 100 percent year on year.

That is not a small bump. It is the kind of growth that gets noticed by travel media, tour operators, and the next wave of travellers deciding where to book a retreat. **BookRetreats attributed Sri Lanka's rise to three things: its 2,000-year-old Ayurvedic tradition, its affordability compared to similar experiences in Europe, and its natural attractions, from year-round beaches to wild elephants and blue whales.**

"Wellness travellers do not just visit once. They spend more, stay longer, and tell people. The question is whether the payment experience matches the product they came for."

### Top Trending Wellness Destinations for 2026

Ranked by year-on-year growth in wellness traveller demand, based on BookRetreats.com's State of Retreats 2026 Report.

1

Sri Lanka

+100%

2

Australia

+85%

3

Morocco

+83%

4

England

+82%

5

Spain

+80%

6

Nepal

+52%

7

Thailand

+48%

8

Mexico

+44%

9

Costa Rica

+42%

10

Canada

+36%

##### About This Ranking

This ranking reflects year-on-year growth in unique page views on BookRetreats.com, a wellness retreat booking platform, alongside a survey of 1,040 US travellers conducted between December 2025 and January 2026. It is a strong signal of rising demand on one major platform, not an official government or independent market measurement.

### Tourist Arrivals Are Climbing to Record Highs

Sri Lanka closed 2025 with 2,362,521 tourist arrivals, up 15.1 percent from the year before, and ahead of the country's previous 2018 peak. The momentum has been building for several years.

Sri Lanka Annual Tourist Arrivals

2022 to 2025 · in millions

0.72M

2022

Recovery year

1.49M

2023

+106% YoY

2.05M

2024

+38% YoY

2.36M

2025

+15.1% · Record

Source: Sri Lanka Tourism Development Authority (SLTDA) and Central Bank of Sri Lanka arrival statistics. 2025 figure surpassed the previous 2018 peak by 1.23 percent. Tourism earnings reached USD 3.22 billion in 2025, though earnings per tourist softened slightly as arrivals grew faster than total spend.

### India Leads, But Europe Brings the Wellness Crowd

India is now Sri Lanka's largest source market by volume. But for wellness and Ayurveda specifically, Germany stands out, contributing more than half of all tourists who name health and Ayurveda as their primary reason for visiting.

India

27%

United Kingdom

9%

Russia

8%

Germany

6%

China

6%

Australia

5%

##### Germany's Ayurveda Connection

Of all tourists who cited health or Ayurveda as their main purpose for visiting Sri Lanka in the first half of 2025, German travellers made up roughly 53 percent. These are exactly the guests most accustomed to cashless, contactless payments at home, and most likely to be surprised by a cash-only Ayurveda retreat in the hills of Kandy.

### A Premium Industry, Running on a Cash Economy

Here is the tension at the centre of this opportunity. Sri Lanka is being celebrated globally for a high-value, premium travel experience. But the infrastructure underneath it has not caught up. Industry estimates put cash transactions at 90 to 95 percent of all retail activity in the country.

92%CASH ESTIMATE

90 to 95% Cash

Tuk-tuks, wayside shops, rural retreats, temples

5 to 10% Digital

Hotels, supermarkets, urban restaurants

This is not a criticism of the country's progress. Digital payment infrastructure has actually moved quickly. LankaQR, the Central Bank's national QR standard, now reaches more than 400,000 merchants.

The gap is not technology. It is reach. Wellness retreats, spice gardens, Ayurveda centres, and tuk-tuk transfers—the exact businesses serving the guests this BookRetreats ranking is about to send—are often the last to adopt these tools.

### The Math Behind a Wellness Traveller

Wellness travellers are not average tourists. Globally, the Global Wellness Institute found that international wellness tourists spend about 41 percent more per trip than typical international travellers. They also tend to stay longer and book higher-value experiences.

#### Ayurveda Resorts & Retreats

Accept card payments for multi-day packages and treatments, including international cards from the German, UK, and Australian guests driving this demand.

#### Spas & Day Wellness Centres

Send a payment link for advance bookings instead of relying on walk-in cash. A guest can confirm and pay from their phone before they ever arrive.

#### Boutique Villas

Kandy, the south coast, and the Cultural Triangle are where most wellness travel happens, and where card acceptance is often thinnest. A simple payment link changes that.

#### Tour Operators & Transfers

Bundle transport, guided tours, and retreat bookings into a single invoice payment link, so guests pay once instead of juggling cash for every leg of the trip.

### What This Means for Your Payment Setup

OnePay was built for exactly this kind of gap: a growing industry, an international audience, and a need for payments that work as smoothly as the experience being sold.

1

#### Accept international cards without a website

Send a payment link or invoice payment link directly over WhatsApp or email. A guest booking a retreat from Germany or the UK can pay in seconds.

2

#### Accept payments in the currency your guest understands

OnePay supports multiple currencies including USD, GBP, EUR, AUD, and more.

3

#### Settle in LKR or foreign currency

Choose how you want to receive your earnings. Standard settlement comes in LKR.

4

#### Get set up in days, not weeks

Whether you run a single retreat property or a network of wellness centres, OnePay's onboarding team can get your account active quickly.

## The World Is Booking Sri Lanka. Make Sure You Can Get Paid.

Set up your OnePay account and start accepting international card payments for your wellness, retreat, or tourism business today.

[Talk to our team](https://www.onepay.lk/contact-us)

---

## OnePay Unified Checkout Overview

**Category**: Blog / Technical Articles  
**Source URL**: https://docs.onepay.lk/blogs/onepay-unified-checkout

@keyframes checkout-float {
0%, 100% { transform: translateY(0); }
50% { transform: translateY(-8px); }
}

Sri Lanka's Trusted Payment Gateway

# OnePay Unified Checkout. *Built to Be Sri Lanka's Most Trusted Payment Page.*

OnePay Checkout is a single, customisable payment page that accepts cards and local mobile wallets, carries your brand, and gives every customer a reason to trust the "Pay" button they are about to tap.

Customisable, branded checkout Cards + mobile wallets, one page 3D Secure on every transaction

### The Checkout Page Is Where Trust Is Won or Lost

A customer has already decided to buy. They have picked the product, agreed to the price, and clicked through to pay. This is the moment a sale either closes or quietly disappears.

Most of the time, what makes a customer hesitate at that final step is not the price. It is the page itself. A checkout that looks unfamiliar, carries no branding, or feels like it was bolted on from somewhere else makes people pause. And a pause at checkout is often the same thing as a lost sale.

**This is exactly the problem OnePay Checkout was built to solve.** One unified payment page, fully customisable to your brand, built to feel like a natural part of your business rather than a foreign detour.

"People do not abandon a purchase because they changed their mind. They abandon it because the last screen they saw did not feel like it belonged to the business they trusted a moment earlier."

### One Checkout Page. Every Way Your Customer Wants to Pay.

OnePay Checkout is a hosted payment page that brings every payment method your customer might use into a single, clean screen. It shows your brand name, the exact amount due, and a clear reference number, so there is never any confusion about what is being paid for.

#### Fully Branded

Your business name and logo appear clearly on the checkout page. Customers see your brand, not a generic payment screen that feels disconnected from the purchase they just made.

#### Cards and Wallets Together

Visa, Mastercard, American Express, Diners Club, Discover, and UnionPay sit alongside local mobile wallets like FriMi, QPlus, and HēlaPay, all on one page.

#### 3D Secure by Default

Every transaction processed through OnePay Checkout is protected with 3D Secure authentication. There are no exceptions, and no 2D fallback that leaves your business exposed.

#### Multi-Currency Ready

Accept payments in 10 supported currencies for customers paying from outside Sri Lanka, while your settlement always lands cleanly in LKR.

#### Works on Any Device

The checkout page is built to render cleanly on a phone, tablet, or desktop, because most of your customers are reaching for their phone, not a laptop.

#### Fast to Integrate

Whether you use OnePay's hosted checkout, a payment link, or the REST API, the same trusted payment experience appears every time, with no separate setup for each channel.

### Every Card. Every Local Wallet. One Page.

Your customers should never have to think about which payment method will work. OnePay Checkout brings the full range of accepted methods into view, all at once, on the same screen.

Debit and Credit Cards

Local Mobile Wallets

### Supported Currencies

OnePay supports 10 currencies, so customers paying from outside Sri Lanka can complete their purchase in a currency they recognise. Settlement to your bank account is always made in LKR, converted at the applicable exchange rate at the time of the transaction.

LKR

Sri Lankan Rupee

USD

US Dollar

GBP

British Pound

EUR

Euro

AUD

Aus Dollar

JPY

Japanese Yen

INR

Indian Rupee

CHF

Swiss Franc

CAD

Canadian Dollar

SGD

Singapore Dollar

##### A Quick Compliance Note

Per Central Bank of Sri Lanka guidelines, Sri Lankan-based businesses cannot accept USD payments from domestic customers. Multi-currency acceptance through OnePay is intended for customers paying from outside Sri Lanka, such as international travel bookings or overseas clients. Speak to your Relationship Officer to confirm which currencies are enabled on your account.

### Built on Four Years of Processing Real Payments

OnePay was launched in 2021 by Spemai Pvt Ltd, a technology company backed by a Japanese corporate investor since 2019. In the years since, it has grown into one of Sri Lanka's most widely used payment infrastructures.

* **LKR 10B+** In payment volume processed
* **4,500+** Active merchants onboarded
* **ISO 27001** Information security certified

OnePay was Sri Lanka's first payment gateway to achieve ISO 27001 certification, the global standard for information security management. For a business owner, that is not a technical footnote. It means the checkout your customers are typing their card details into has been independently audited against an internationally recognised security standard.

### From Cart to Confirmed Payment, in One Smooth Page

1

#### Customer reaches the OnePay Checkout page

Whether triggered from your website, a payment link, or an invoice, the customer lands on a single page showing your brand, the amount due, and a clear reference number.

2

#### Customer chooses how to pay

Card or mobile wallet, all visible on the same screen. No separate pages, no redirect to a third-party app that breaks the flow of the purchase.

3

#### 3D Secure authentication runs automatically

For card payments, the issuing bank sends a one-time password to the customer's phone. This step is mandatory on every OnePay transaction, with no exceptions.

4

#### Payment confirms instantly

The customer sees a clear confirmation. You receive an instant notification on your dashboard, and the transaction appears in your records right away.

5

#### Funds settle to your account on a T+2 schedule

OnePay transfers the net amount, after MDR and applicable fees, directly to your registered bank account two working days after the transaction, via CEFT transfer.

### Three Ways to Use OnePay Unified Checkout

OnePay Checkout is not locked to a single setup. Choose the path that matches how technical your team is and how quickly you want to launch.

**1. Hosted Checkout, No Code Required:** Generate a payment link from your OnePay dashboard and share it anywhere. The customer taps the link and lands directly on your branded OnePay Checkout page.

**2. Embedded Checkout for Your Website:** Using OnePay JS, developers can embed the checkout experience directly into an existing website or app.

**3. Full API Integration:** For businesses with custom platforms, OnePay's REST API and SDKs allow complete control over the payment flow.

```
// Example: creating a payment link via the OnePay API

POST https://api.onepay.lk/v1/payment-links

{

"amount": 25000.00,

"currency": "LKR",

"reference": "ORD-2024-00847",

"description": "Order payment",

"app_id": "your_app_id"

}
```

### What Makes a Payment Gateway Actually Convenient

| What Matters | OnePay Checkout | Typical Alternative |
| --- | --- | --- |
| Branded checkout page | Your logo and name shown | Often generic or unbranded |
| Cards and wallets on one screen | Yes | Often split across pages |
| Mandatory 3D Secure | Every transaction | Varies by provider |
| No-code payment links | Built in | Often requires a developer |
| Transparent payout schedule | T+2, clearly documented | Often unclear or delayed |
| Local mobile wallet support | FriMi, QPlus, HēlaPay | Frequently missing |

### Frequently Asked Questions

#### Is OnePay Checkout customisable to match my brand?

Yes. Your business name and logo appear on the checkout page, so customers see a payment experience that feels connected to the purchase they just made.

#### How quickly do I receive my money after a sale?

OnePay operates on a T+2 payout schedule for most payment methods. Funds are transferred directly to your registered bank account via CEFT.

#### Is 3D Secure required for every transaction?

Yes. OnePay mandates 3D Secure authentication on all card transactions with no exceptions. This protects your business from fraud liability.

## Give Your Customers a Checkout They Actually Trust.

Set up OnePay Checkout in minutes. One branded page, every card and wallet your customers use, and 3D Secure protection built in from day one.

[Talk to our team](https://www.onepay.lk/contact-us)

---

## OnePay Orchestration & Smart Routing

**Category**: Blog / Technical Articles  
**Source URL**: https://docs.onepay.lk/blogs/onepay-orchestration

One Connection. Endless Possibilities.

# One Connection. Every Payment Path Routed Right.

OnePay Orchestration connects your acquirers, payment methods, banks, fraud tools, and CX tools into a single smart routing layer. The result is a higher approval rate, fewer failed transactions, and one simple integration instead of five.

OnePayOrchestration

AcquirersMultiple banks

Payment MethodsVisa · MC · Amex

BanksLocal + foreign

Smart RoutingReal-time logic

CX ToolsCheckout, support

Fraud ToolsRisk scoring

## A Declined Payment Costs More Than the Sale

A customer adds an item to cart. They reach checkout. They enter their card. The payment fails for no reason they understand, and most of them never come back to try again.

For a lot of Sri Lankan businesses, that failed payment is not actually a card problem. It is a routing problem. The transaction went down one fixed path, through one acquirer, with no alternative if that path had a hiccup. **One bad route, one lost sale.**

This is the gap OnePay Orchestration closes. Instead of locking your business into a single rigid connection, OnePay routes every transaction intelligently across multiple acquirers, payment methods, banks, fraud tools, and CX tools, choosing the path most likely to succeed in that exact moment.

"A payment gateway processes transactions. A payment orchestration layer decides the smartest way to process each one."

That distinction matters more than it sounds. Most Sri Lankan businesses are used to thinking of a payment gateway as a single pipe: card goes in, payment comes out. OnePay Orchestration treats it differently. Every transaction gets evaluated and routed through the path that gives it the best chance of success, automatically, in real time.

## What Payment Orchestration Actually Means

Payment orchestration is the layer that sits between your checkout and the many systems involved in processing a card payment. Instead of connecting your business to one acquirer and hoping every transaction goes through cleanly, orchestration connects you to several, and intelligently decides which one handles each transaction.

Customer Pays

OnePay Orchestration

Best Route Chosen

Behind that one decision sit six connected systems, all working together so your business does not have to manage them separately.

#### Acquirers

Multiple acquiring banks connected behind one integration, so a transaction always has more than one path to succeed.

#### Payment Methods

Visa, Mastercard, and American Express, all processed through the same checkout without separate setup for each.

#### Banks

Local and foreign currency banking relationships connected so settlement reaches your account the way you need it.

#### Fraud Tools

Real-time risk scoring on every transaction, catching suspicious activity without slowing down genuine customers.

#### CX Tools

A checkout experience and support layer designed around what actually helps customers complete a purchase.

#### Routing

The logic that decides, transaction by transaction, which acquirer and path gives the best chance of approval.

## Why Smart Routing Means a Higher Approval Rate

Every card transaction has a chance of being declined for reasons that have nothing to do with the customer or your business. A temporary issue at one acquirer, a bank-side glitch, a network timeout. When there is only one path for a transaction to take, any one of these issues becomes a lost sale.

OnePay Orchestration removes that single point of failure. If one path is not performing well for a particular transaction, the routing layer can direct it through an alternative acquirer or method automatically. The customer sees one smooth checkout. Behind the scenes, OnePay is doing the work of choosing the best route for that payment.

##### What This Means in Practice

For a business processing hundreds or thousands of transactions a month, even a small improvement in approval rate adds up to real revenue. Fewer declined payments means fewer abandoned carts, fewer frustrated customers, and fewer support tickets asking why a payment did not go through.

## One Routing Layer. Every Currency You Need.

OnePay Orchestration is also where multi-currency acceptance lives. When a customer pays in USD, GBP, EUR, or any of OnePay's supported currencies, the routing layer chooses the right processing path for that currency automatically, without you needing separate integrations for each one.

This is the same infrastructure covered in our guide on [multi-currency payments on OnePay](/blogs/multi-currency-payments). Orchestration is what makes that multi-currency experience feel seamless from the customer's side, while your business manages everything from a single dashboard.

## From Checkout to Settlement, in Four Steps

1

### Your customer reaches checkout

Customer side

Whether it is a hosted checkout page, a payment link, or an API integration, the customer sees one clean payment screen. They do not see or need to know what happens next.

2

### OnePay evaluates the best route

Behind the scenes

The orchestration layer checks acquirer performance, payment method, currency, and fraud signals in real time, then routes the transaction through the path most likely to succeed.

3

### Fraud and CX tools run automatically

Automatic

Risk scoring happens on every transaction without adding friction for genuine customers. CX tools keep the checkout experience fast, clear, and consistent regardless of which path the payment took.

4

### Settlement reaches your account automatically

Automated payout

Once the transaction is approved, payout processing is automated. Funds settle to your bank account in LKR or foreign currency, depending on your account setup, without manual reconciliation work on your end.

## Why This Matters for Hotels, Cafés, and Online Sellers

### Fewer failed payments, fewer lost customers

A hotel taking advance booking payments cannot afford a guest's card to fail at checkout for no clear reason. Smart routing reduces the chance of that happening, which means more confirmed bookings and fewer awkward follow-up messages.

### One integration instead of five

Without orchestration, accepting multiple payment methods and currencies often means juggling separate integrations, separate dashboards, and separate support contacts. OnePay brings all of it under one connection, one dashboard, and one support relationship.

### Built-in fraud protection without the overhead

Most small businesses cannot afford to build their own fraud detection system. OnePay's fraud tools run on every transaction by default, giving café owners, event organisers, and online sellers the same level of protection that larger platforms rely on.

### Automated payouts that just arrive

Freelancers and small business owners do not have time to chase down settlement manually. OnePay's automated payout process means funds move to your account on schedule, whether you are settling in LKR or foreign currency.

## OnePay Orchestration vs. a Single-Acquirer Gateway

Most payment gateways in Sri Lanka connect your business to one acquiring path. Here is what changes when you add an orchestration layer on top of that.

| Feature | OnePay Orchestration ✓ | Single-Acquirer Gateway |
| --- | --- | --- |
| **Routing paths per transaction** | ✓ Multiple acquirers | ✗ One fixed path |
| **Approval rate optimisation** | ✓ Automatic, real time | ✗ Not available |
| **Multi-currency support** | ✓ Built into routing | ✗ Limited or none |
| **Fraud detection** | ✓ Included by default | ✗ Often a separate add-on |
| **Automated payouts** | ✓ Yes | ✓ Most gateways |
| **Number of integrations needed** | ✓ One | ✗ Often several |

##### What OnePay Currently Does Not Support

To be clear about what OnePay Orchestration covers today, here is what it does not include. OnePay does not support LankaQR, eZ Cash, mCash, or internet banking payments. Card payments through Visa, Mastercard, and American Express are processed through OnePay's orchestration layer, with multi-currency acceptance and smart routing applied across all of them.

## One Connection. Endless Possibilities.

Set up your OnePay account once and let orchestration handle the rest. Higher approval rates, multi-currency acceptance, built-in fraud protection, and automated payouts, all from a single integration.

[Talk to Our Team](https://onepay.lk/contact-us)

# The Bottom Line

A payment gateway gets a transaction from point A to point B. A payment orchestration layer makes sure point A to point B is the smartest path available for that exact transaction, every time.

For Sri Lankan businesses competing for international guests, processing recurring subscriptions, or simply trying to stop losing sales to random declines, that difference is not a technical detail. It shows up directly in revenue.

**OnePay Orchestration brings acquirers, payment methods, banks, fraud tools, CX tools, and smart routing together under one connection.** Built for scale. Designed for success. Powering growth while protecting trust.

---

## Accept Payments in 10 Currencies

**Category**: Blog / Technical Articles  
**Source URL**: https://docs.onepay.lk/blogs/multi-currency-payments

Sri Lanka's Only 10-Currency Gateway

# Accept Payments in 10 Currencies. Grow Without Borders.

Your guests and customers are booking from around the world. OnePay is the only payment gateway in Sri Lanka that lets you accept cards in 10 currencies, so they pay in their currency and you get settled in yours.

USD · GBP · EUR · AUD · JPYCAD · CHF · SGD · INR · LKRSettle in LKR or foreign currency

Interactive Demo — Click a Currency

#### Customer Pays In

USDUS Dollar

GBPBritish Pound

EUREuro

AUDAustralian Dollar

JPYJapanese Yen

INRIndian Rupee

CHFSwiss Franc

CADCanadian Dollar

SGDSingapore Dollar

LKRSri Lankan Rupee

Payment  
ReceivedMULTI-  
CURRENCY

$1,250.00

USD • Visa card ending 4521 •Approved

Pay $1,250.00 in USD

You settle in LKR • onepay.lk

## Your Guests Are Global. Your Payment Setup Should Be Too.

A British couple books a villa in Mirissa. An Australian family checks into a guesthouse in Kandy. A Japanese business traveller pays for a private tour. These guests want to pay in the currency they know. The amount should appear in pounds, dollars, or yen on their bank statement, not in a currency they have to Google.

For years, Sri Lankan travel businesses, hotels, booking platforms, and SaaS products had no way to offer this. You accepted LKR and hoped international cardholders would not abandon the checkout when they saw an unfamiliar currency.

**OnePay changes that.** As the only payment gateway in Sri Lanka supporting 10 currencies, OnePay lets your customers pay in the currency they use every day, while you manage your business in the currency that suits you best.

"When a customer sees their own currency at checkout, conversion rates go up. Checkout abandonment goes down. That single change can meaningfully increase your revenue from international guests."

This is not a minor convenience. Research consistently shows that customers are more likely to complete a purchase when prices are displayed in their own currency. For travel businesses and SaaS platforms serving international clients, multi-currency acceptance is not optional. It is a competitive requirement.

## 10 Currencies. One Gateway. Only on OnePay.

OnePay is the only payment gateway in Sri Lanka that supports all 10 of these currencies for online card acceptance. Your customers pay in their local currency; you receive funds in LKR or foreign currency depending on your account setup.

USDUS Dollar

GBPBritish Pound

EUREuro

AUDAustralian Dollar

JPYJapanese Yen

INRIndian Rupee

CHFSwiss Franc

CADCanadian Dollar

SGDSingapore Dollar

LKRSri Lankan Rupee

| Code | Currency | Best For | Region |
| --- | --- | --- | --- |
| USD | **US Dollar** | Global standard | North America · Global |
| GBP | **British Pound** | UK travellers and clients | United Kingdom |
| EUR | **Euro** | European guests | Eurozone (27 countries) |
| AUD | **Australian Dollar** | Australian travellers | Australia |
| JPY | **Japanese Yen** | Japanese tourism | Japan |
| INR | **Indian Rupee** | Indian visitors and SaaS | India |
| CHF | **Swiss Franc** | European high-value guests | Switzerland |
| CAD | **Canadian Dollar** | Canadian travellers | Canada |
| SGD | **Singapore Dollar** | Singapore and SEA guests | Singapore |
| LKR | **Sri Lankan Rupee** | Local and domestic payments | Sri Lanka |

##### Only On OnePay in Sri Lanka

No other payment gateway currently operating in Sri Lanka offers multi-currency acceptance across 10 currencies for domestic merchants. OnePay is the first and currently the only gateway to make this available to local businesses of all sizes.

## Built for the Businesses That Serve the World

Multi-currency payment acceptance is most valuable for businesses with a significant share of international customers. Here is where OnePay's 10-currency support makes the biggest difference.

#### Travel Agents and Tour Operators

You book tours for guests from the UK, Germany, Japan, and Australia. When your checkout shows GBP or EUR, your international clients complete the booking without hesitation. There is no currency confusion, no abandoned carts, and no WhatsApp messages asking "what is this in pounds?"

High impact for international bookings

#### Hotels, Villas, and Guesthouses

A guest booking directly through your website should see prices in their own currency. OnePay's multi-currency checkout makes direct bookings feel as seamless as Booking.com, without the 15% commission. USD, EUR, AUD, and SGD travellers all get a native checkout experience.

Direct booking conversion

#### Booking Engines and OTA Platforms

If you are running a booking platform for Sri Lankan properties, multi-currency is a core feature your clients expect. OnePay's API lets you present the right currency to the right customer automatically, based on their location or preference. No custom forex logic needed on your end.

Platform and marketplace ready

#### SaaS Products and Digital Services

If your software has customers in India, Singapore, the UAE, or Europe, you need multi-currency billing. OnePay lets SaaS businesses price in USD or the customer's local currency, reducing friction at the subscription checkout and improving renewal rates from international users.

Subscription and recurring billing

#### Education and Online Learning

Sri Lankan e-learning platforms and tutoring services serve students across South Asia, Southeast Asia, and Europe. Accepting INR, SGD, and EUR directly removes the biggest barrier at checkout: an unfamiliar currency with an unclear exchange rate.

Remove checkout friction

#### E-commerce with International Reach

Selling handcrafts, tea, apparel, or specialty goods to buyers in the UK, Australia, or the US? Multi-currency checkout means your customers see a price in pounds or dollars, not an LKR amount they have to convert in their head. That reduces friction and increases purchase confidence.

International e-commerce

## From International Card to Your Account in Three Steps

The technical complexity is handled entirely by OnePay. Here is what the process looks like from your side and your customer's side.

1

### Your customer reaches the checkout page

Customer side

OnePay's checkout detects or displays the selected currency. The customer sees the amount in USD, GBP, EUR, or whichever of the 10 currencies you have enabled. No manual conversion, no ambiguity.

2

### Payment is processed via Visa or Mastercard

OnePay processes

The customer pays using their international card. OnePay processes the transaction in the selected currency through the card network. 3D Secure OTP authentication protects every transaction. Approval happens in seconds.

3

### You receive settlement in your chosen currency

Your settlement

Depending on your account setup, funds settle to your account in LKR or in the original foreign currency. Foreign currency settlement requires an account with one of OnePay's partner banks. Settlement typically arrives within 2 to 3 business days.

## Choose How You Want to Receive Your Money

OnePay gives you two settlement options depending on your business model and banking setup. Both are available to OnePay merchants once your account is approved.

### Settle in LKR

Receive your international payments converted to Sri Lankan Rupees and deposited directly into your local bank account. Simple, straightforward, and available with any standard OnePay merchant account. No additional banking setup required.

Available with standard OnePay account · Any local bank

### Settle in Foreign Currency

Retain earnings in USD, GBP, EUR, or other accepted currencies by receiving settlement directly into a foreign currency account. This is ideal for businesses managing international expenses, reinvesting in foreign markets, or optimising for exchange rates. Requires an account with one of OnePay's designated partner banks in Sri Lanka.

Requires foreign currency account at an OnePay partner bank

##### Foreign Currency Account Setup

To receive settlement in a foreign currency, you will need to open a foreign currency account with one of OnePay's partner banks in Sri Lanka. OnePay's onboarding team will guide you through the exact requirements when you apply. Most businesses with a valid Export of Services registration can open a foreign currency account through this route.

## OnePay vs. Other Sri Lankan Payment Gateways

Multi-currency acceptance is where OnePay stands alone in the Sri Lankan market. Here is a direct comparison against the alternatives currently available to local merchants.

| Feature | OnePay ✓ | Other Sri Lankan Gateways |
| --- | --- | --- |
| **Multi-currency acceptance** | ✓ 10 currencies | ⚡ Limited currencies |
| **USD acceptance** | ✓ Yes | ✓ Most gateways |
| **EUR, GBP, AUD acceptance** | ✓ All supported | ⚡ Some gateways |
| **JPY, CHF, CAD, SGD, INR** | ✓ All supported | ✗ Not available |
| **Foreign currency settlement** | ✓ Via partner banks | ✗ LKR settlement only |
| **International Visa and Mastercard** | ✓ Yes | ✓ Most gateways |
| **Hosted payment page** | ✓ Yes | ✓ Most gateways |
| **Payment link and invoice link** | ✓ Yes | ✓ Some gateways |
| **API integration** | ✓ Full REST API | ✓ Most gateways |

## What Multi-Currency Acceptance Actually Does for Your Business

### Fewer abandoned checkouts from international customers

When an international card holder sees an amount in LKR, many of them pause. They open a converter, do the mental maths, and second-guess the purchase. Some abandon the checkout entirely. Showing the price in their own currency removes that friction and keeps the booking moving.

### Higher trust and a more professional first impression

A checkout that displays USD or GBP signals that your business is set up for international customers. It is a small detail with a real effect on trust. Travellers booking expensive tours or hotel stays are more comfortable paying through a gateway that speaks their currency.

### No currency risk pushed onto your customer

When a customer pays in LKR using a foreign card, their bank applies its own exchange rate and often adds a foreign transaction fee. They end up paying more than they expected. When they pay in their home currency through OnePay, the rate is known and the experience is clean. That is better for your reputation and your reviews.

### A real advantage over competitors still on LKR-only gateways

Most of your competitors are still collecting international payments in LKR. If your checkout offers USD, GBP, or EUR while theirs does not, you have a genuine conversion advantage on any channel where international visitors are comparing options, including Google, TripAdvisor, and direct social enquiries.

##### For SaaS Products: Price in the Right Currency, Grow the Right Market

SaaS pricing psychology is real. A product priced at LKR 4,900 per month looks confusing to an Indian or Singaporean buyer. The same product priced at USD 16 or SGD 22 reads clearly. OnePay's multi-currency support lets you present pricing in the currency your target market understands, which directly impacts trial signups and subscription conversions.

## How to Enable Multi-Currency on Your OnePay Account

### Sri Lanka's Only 10-Currency Gateway. Start Accepting International Payments Today.

Join OnePay and give your international customers a checkout that feels built for them. Set up in minutes. No hidden fees. Settlement in LKR or foreign currency.

[Create Your Account Free →](https://onepay.lk/contact-us)[Talk to Our Team](https://onepay.lk/contact-us)

Contact the OnePay team directly to enable multi-currency acceptance on your account. Reach us via WhatsApp on **+94 76 052 3025** or email at **info@onepay.lk**. The team will confirm your eligible currencies, configure your account, and guide you through foreign currency settlement setup if needed.

---

### The Bottom Line

Sri Lanka's inbound tourism is recovering strongly, and international demand for Sri Lankan products, services, and digital products is growing. **The businesses that convert more international visitors into paying customers are the ones with checkouts built for international buyers.**

Multi-currency payment acceptance is no longer a luxury feature. For travel agents, hotels, booking platforms, and SaaS businesses serving international customers, it is a fundamental part of a modern, conversion-optimised payment setup.

OnePay is the only payment gateway in Sri Lanka that makes this available across 10 currencies today. Whether you settle in LKR through your existing bank account or in a foreign currency through an OnePay partner bank, the infrastructure is ready. Your checkout can be too.

---

## Hotels: Get Paid When Guests Book

**Category**: Blog / Technical Articles  
**Source URL**: https://docs.onepay.lk/blogs/hotels-deposits

# Sri Lankan Hotels and Tour Operators: Get Paid Online *the Moment a Guest Agrees to Book*

Most bookings start on WhatsApp or Instagram. By the time you send a bank account number, the guest has moved on. There is a better way, and it takes about 30 seconds to set up.

##### 68% of unconfirmed reservations

Research on Sri Lanka's hotel sector found that properties without advance payment systems lose the majority of tentative bookings to no-shows and last-minute cancellations, with no recourse to charge fees.

## The Real Problem: An Unconfirmed Booking Is Not a Booking

Picture a scene that plays out every week across Sri Lankan guesthouses, boutique hotels, tour operators, and surf camps. A guest messages on Instagram. They are excited. They want two nights in Mirissa, a whale-watching tour at 6am, a room with a sea view. You reply quickly. You send the rate. They say "I'll confirm tomorrow." They never do. The room sits empty.

This is not bad luck. It is a payment timing problem. **The moment a guest agrees to book is the moment you need to collect payment.** Every hour you wait, the chance of losing that booking grows. Most hospitality businesses in Sri Lanka have no tool to act on that moment. OnePay is built for exactly this.

##### The booking window is the chat window

"When a guest reaches out on social media and you cannot send a payment link in the same conversation, you have already started losing them."

Properties that rely on verbal confirmations and WhatsApp promises face a real no-show problem. This gets worse during quieter months, when guests feel less committed to reservations they never paid for. The conversation ends, life gets in the way, and another property's payment link lands in their inbox.

Sri Lanka welcomed over **2 million tourists in 2024**, a 38% increase year on year, and that number is expected to keep growing. The demand is there. The interest is real. The gap is between a guest saying yes on social media and money actually arriving in your account.

## Where Bookings Actually Happen: Most Bookings Start on Social Media. Not a Booking Website.

The reality for most Sri Lankan hotels and tour operators today is that guests do not start their journey on a booking engine. They see your photos on Instagram. They send a message on WhatsApp. They leave a comment on Facebook. That moment of interest is your booking window. It is short. Once it closes, it rarely opens again.

The businesses that turn these conversations into confirmed, paid bookings are the ones with a payment link ready to send the moment they confirm availability. One link. The guest taps it, pays by card in under a minute, and the booking is done. No follow-up needed. No chasing required.

The businesses without that link send a bank account number, or ask the guest to confirm later, or say pay at check-in. Those conversations rarely turn into revenue. The guest moves on. You are left wondering what happened.

##### The chat window is the booking window. OnePay keeps it open.

OnePay turns any social media conversation into an instant payment moment. While the guest is still engaged and interested, you send a payment link or an invoice payment link. They pay by card in 60 seconds. You get a notification. The booking is confirmed. That is how social conversations convert to real revenue.

2M+

Tourists visited Sri Lanka in 2024, a 38% increase year on year

68%

Of unconfirmed reservations turn into no-shows at properties without online payment

15%

Is what OTAs like Booking.com take from every booking you make through their platform

## What's Actually Happening: Why the Old Approach Keeps Failing

Most Sri Lankan hospitality businesses handle advance booking payments in ways that make sense on paper but fall apart in practice. Here is an honest look at what is not working, and what does.

What's Not Working

### Why You Keep Losing Bookings

* ✗ Guests promise to pay at check-in. Many simply do not show up.
* ✗ Asking guests to wait for an invoice email breaks the energy of the conversation.
* ✗ Cash-only policies rule out every overseas or remote booking from the start.
* ✗ No digital record of the booking means no recourse when guests cancel.
* ✗ A broken card machine at check-in is the kind of thing that ends up on TripAdvisor.
* ✗ Listing on OTAs solves one problem but costs 12 to 18% of every booking, forever.

What Works with OnePay

### Get Paid While the Guest Is Still in the Conversation

* ✓ Generate a payment link in seconds. No website needed, no technical setup.
* ✓ Share it on WhatsApp, Instagram DM, Facebook, email, or SMS. Wherever the conversation is happening.
* ✓ The guest pays by card in under 60 seconds. Visa, Mastercard, or Amex, on any phone.
* ✓ You get an instant notification. The booking is confirmed. Nothing else needed.
* ✓ Full payment history in your OnePay dashboard, exportable whenever you need it.
* ✓ Zero OTA commission. The payment goes directly to your account.
* ✓ Works for partial advance payment or full payment upfront. Your choice.

## The Process: From Instagram DM to Confirmed Booking, Step by Step

No website required. No developer needed. No visit to the bank. Here is exactly how the process works from first message to paid booking.

1

### A guest messages you about availability

It could come through WhatsApp, Instagram, Facebook, TripAdvisor, or a direct call. The channel does not matter. What matters is what you do next. This is the moment to act.

2

### You log into OnePay and create a payment link

Enter the amount, add the guest name and booking reference, and set an expiry if you want. You can create a simple payment link or an invoice payment link with full booking details. It takes about 30 seconds.

3

### You send the link in the same conversation

Copy the link and paste it directly into WhatsApp, Instagram DM, an email, or an SMS. You do not ask the guest to reply to confirm. You give them a link they can act on immediately, while they are still engaged.

4

### The guest pays by card from anywhere in the world

The OnePay checkout works on any device and any browser. Visa, Mastercard, American Express. A guest in Germany, Singapore, or Kandy can complete the payment in under a minute. Every transaction is protected with 3D Secure OTP.

5

### You get an instant notification. The booking is secured.

The moment payment goes through, you receive a push notification and an email. The guest gets a receipt. Both parties have a digital record. Settlement reaches your bank account within 2 to 3 business days.

## Regional Context: How Other Markets Solved This. What Sri Lanka Can Learn.

Sri Lanka is not alone in this. Small hospitality businesses across South and Southeast Asia faced the same challenge: collecting advance booking payments from guests who enquire informally, without a complex booking engine behind them. Here is how they handled it, and what OnePay brings to Sri Lanka.

🇮🇩

#### Bali, Indonesia

Villa rentals, guesthouses, surf camps

Villa operators share payment links on Instagram and WhatsApp the moment a guest enquires. Mobile payment apps made instant collection the norm for even the smallest properties. No-show rates dropped significantly as a result.

🇹🇭

#### Thailand

Island guesthouses, tour operators, dive schools

Small properties in Koh Samui and Koh Lanta send payment links via LINE app the moment a guest agrees to book. The guest pays in the same conversation. No website, no OTA fees. Social enquiry converts to confirmed revenue in under a minute.

🇱🇰

#### Sri Lanka, powered by OnePay

Hotels, villas, tour operators, surf camps, adventure tours

OnePay gives Sri Lankan hospitality businesses the same capability. Generate a payment link in 30 seconds, share it on WhatsApp or Instagram, and the guest pays by card from anywhere in the world. Social conversation converts to confirmed, paid booking.

The pattern is the same across every market. Once small hospitality businesses get access to a simple, mobile-first payment link tool, **direct bookings increase, dependence on OTAs drops, and no-show rates fall.** Sri Lanka has that tool now. It is called OnePay.

## Full Comparison: OnePay vs. What You Are Using Today

| Feature | OnePay ✓ | Booking.com / Agoda | Cash at Check-in |
| --- | --- | --- | --- |
| No website required | ✓ Yes | ✗ Needs a profile | ✓ Yes |
| Works via WhatsApp or Instagram | ✓ Instantly | ✗ No | ✗ No |
| Commission per booking | ✓ None | ✗ 12 to 18% | ✓ None |
| International card acceptance | ✓ Visa · MC · Amex | ✓ Yes | ⚡ Rarely |
| Instant payment confirmation | ✓ Immediate | ✓ Yes | ✗ Only at check-in |
| No-show protection | ✓ Paid booking = committed guest | ✓ Card hold | ✗ None |
| Setup time | ✓ 2 Working Days | ⚡ Days | ✓ None |
| Invoice payment link option | ✓ Yes, branded with booking details | ✗ No | ✗ No |

## Real Use Cases: How Different Businesses Use OnePay to Confirm Bookings

### Surf Camp Advance Bookings in Arugam Bay

Surf camps typically receive enquiries from overseas guests three to eight weeks ahead, mostly through Instagram. Sending an advance payment link directly in the DM removes the "we'll confirm when we land" problem. The guest pays, the spot is secured, and the camp has real occupancy data to plan staffing and equipment hire well ahead of time.

### Whale Watching Tour Pre-Payments in Mirissa

Boat operators work at a fixed capacity. Without advance payment, there is no way to know which guests will actually show up at 5:30am. A payment link sent via WhatsApp at the moment of booking, USD 100 per person, removes ghost bookings entirely. The social conversation closes with payment, not a vague promise.

### Boutique Hotel and Villa Advance Payments in Galle and Unawatuna

High-value stays at USD 150 or more per night are the most at-risk unconfirmed reservations. An invoice payment link sent within 24 hours of an enquiry moves the guest from interested to committed before they start browsing alternatives. The link includes all booking details, the check-in date, and a cancellation policy. It works as a professional booking confirmation on its own.

### Private Tour Operator Advance Bookings

Tour operators offering cultural itineraries, wildlife safaris, or custom packages can use OnePay to collect a booking confirmation payment of USD 100 to 150 per itinerary. This confirms the guide's time before any planning begins. No more cancelled custom tours after two hours of preparation work.

#### No website required. That is exactly the point.

Most surf instructors in Arugam Bay, whale-watching operators in Mirissa, and tour guides in the hill country do not have, and do not need, a full e-commerce website to accept online payments. A OnePay payment link shared in the same WhatsApp conversation does the job completely. Generate the link. Share it. Get paid. Done.

Illustrative Scenario · Hikkaduwa

### From 40% No-Shows to Fully Confirmed Weekends

A boutique dive resort in Hikkaduwa with 12 rooms was losing three to four bookings every weekend to no-shows. They had a call-to-confirm policy, but guests rarely followed through. After including a OnePay payment link in every WhatsApp availability reply, set at USD 100 per room and credited to the final bill, they stopped releasing rooms without payment first.  
  
The link went out in the same message as the availability confirmation. The conversation converted to payment immediately. Within one month, weekend no-shows dropped to zero. Occupancy increased by 22%. And the payment confirmation became their booking receipt, making check-in faster and dispute-free.

22% occupancy increase · Zero no-shows · No website required

## Your Next Booking Should Come With Payment.

Create your first payment link in under five minutes. Send it in the same message as your availability reply. Get paid before the guest has a chance to move on. No website, no code, no bank visit needed.

[Start Collecting Payments Free →](https://onepay.lk/register)[Talk to Our Team](https://onepay.lk/contact)

## The Bottom Line

Sri Lanka's tourism sector is growing faster than it has in years. **Two million tourists arrived in 2024, a 38% increase year on year, with 2.5 million projected for 2025.** Demand is not the problem. The gap is between a guest expressing interest on social media and money arriving in your account.

Every day without an online payment option is a day you are turning social conversations into hope rather than revenue. Hotels in Bali, Thailand, and the Maldives solved this years ago. They send a payment link in the same message as their availability reply. Guests pay immediately. Bookings are confirmed. Rooms fill up.

**OnePay gives every Sri Lankan hotel, villa, tour operator, surf camp, and guesthouse that same capability.** A payment link or invoice payment link that works on any phone, accepts Visa, Mastercard, and American Express, and turns a social media chat into a confirmed, paid booking. No website needed. No developer needed. No paperwork required.

Payment is not a step that comes after the booking. It is the booking. The moment a guest pays is the moment the booking becomes real.

---

## Do Not Honour (Code 05) Explained

**Category**: Blog / Technical Articles  
**Source URL**: https://docs.onepay.lk/blogs/do-not-honour

# "Do Not Honour" Explained: Response Code 05

"Do Not Honour" is the most common card decline code your customers will ever see and the most misunderstood. Here's what it actually means, why it happens, and how OnePay merchants can recover the sale.

## What does "Do Not Honour" mean?

When a card payment fails, your payment gateway receives a two-digit response code from the customer's issuing bank. Response code 05 "Do Not Honour" is a general-purpose decline that means the bank has refused the transaction without giving a specific reason why.

It is the most common single decline code processed through OnePay's gateway. Across Sri Lanka's payment network, it accounts for a significant share of all failed card transactions affecting Visa, Mastercard, and domestic cards alike.

## Why banks send vague codes

Banks deliberately use generic codes like 05 to protect cardholders. If a bank returned a specific reason "transaction flagged as fraudulent" or "card reported stolen" fraudsters could use that information to refine their attacks. Ambiguity is by design.

##### The critical thing to understand

"Do Not Honour" is a statement about the cardholder's account, not about OnePay, your merchant account, or your website. The payment request reached the bank successfully and the bank simply chose to decline it.

## How a "Do Not Honour" reaches your checkout

1

### Customer enters card details

Checkout form on your website or app captures card number, expiry, CVV.

2

### OnePay sends authorisation request

Encrypted transaction data is routed through the card network (Visa/Mastercard/Amex/UnionPay) to the issuing bank.

3

### Issuing bank evaluates the request

The bank checks balance, fraud scores, velocity rules, card status, and spending patterns — all in under 2 seconds.

4

### Bank returns code 05 — Do Not Honour

The bank refuses without explanation. The refusal is passed back through the network to OnePay.

5

### Customer sees a decline message

OnePay surfaces a customer-friendly message. The underlying code 05 is visible in your OnePay merchant dashboard.

## Why does "Do Not Honour" happen?

Because code 05 is generic, it can stem from a wide range of issuing bank decisions. The most common causes in context include:

### 1. Fraud scoring / risk rules triggered

Banks maintain real-time fraud models. If a transaction looks unusual a large amount, an unfamiliar merchant category, a first-time international purchase, or activity that doesn't match the cardholder's typical behaviour the bank's risk engine may decline automatically. This is the most common cause of code 05 in Sri Lanka, especially for first-time online transactions on cards primarily used at physical POS terminals.

### 2. Daily spending or transaction limits exceeded

Many Sri Lankan bank accounts have daily online transaction limits set by default often as low as LKR 50,000–100,000 for standard debit cards. A customer attempting a larger purchase will receive code 05 even if funds are available. The fix: the customer must increase their online limit through their bank's mobile app or branch.

### 3. Online / E-commerce Transactions Not Enabled

This is a common issue with Sri Lankan debit cards. Many banks issue cards with e-commerce transactions disabled by default as a security precaution. As a result, online payments may fail unless the cardholder has explicitly enabled this feature.

##### Sri Lanka-specific: debit cards with online payments disabled

Unlike credit cards, most Sri Lankan debit cards require customers to manually enable "e-commerce transactions" or "online purchases" in their banking app. If your customers are predominantly using debit cards, this is likely the #1 cause of your Do Not Honour declines. Instruct customers to check this setting first.

### 4. Insufficient funds (masked as Do Not Honour)

While insufficient funds typically returns its own code (51), some banks route insufficient balance declines through code 05 — particularly for credit cards where the bank does not wish to reveal the credit limit situation. If the customer is confident their card is fine in other respects, checking available balance is worth trying.

### 5. Transaction velocity limits

Banks set rules on how many transactions a card can attempt in a given time window. If a customer's card was recently used multiple times or if there were multiple failed attempts, the bank may temporarily block further authorisations and return code 05. This often resolves itself within a few hours.

### 6. 3D Secure / OTP failure upstream

In Sri Lanka, most card-not-present transactions require 3D Secure authentication (the OTP step). If the OTP is entered incorrectly or the bank's authentication server has an issue, the transaction may still return code 05 after the OTP flow. This is a bank-side issue, OnePay passes the 3DS result faithfully.

### 7. International merchant or currency restrictions

Some Sri Lankan bank accounts have foreign currency or international merchant restrictions. Even for domestic payments, if the merchant is categorised under a restricted MCC (Merchant Category Code) gambling, crypto, certain digital goods the bank may return code 05 based on account-level category restrictions.

~60%

Of Do Not Honour declines are resolved when the customer retries with correct settings

~25%

Caused by online payments being disabled on the card

72 hrs

Typical window before bank auto-lifts velocity blocks

## What should the customer do?

A "Do Not Honour" decline is almost always resolvable. Here is the recommended flow to give your customers either in your checkout error message, your order failure email, or your customer support script.

1

Contact your bank first

Call the number on the back of your card or message through your banking app. Ask why the transaction was declined and request that the block be lifted. Do not assume the problem is with the merchant's website or Onepay.

2

Enable online / e-commerce transactions

If you are using a Sri Lankan debit card, you can enable online transactions by contacting your card-issuing bank (via hotline or branch). The relevant contact details are typically available on the back of the card.

3

Increase your daily online transaction limit

Some banks in Sri Lanka require customers to manually request an increase to their daily online or e-commerce transaction limit. If your purchase exceeds the current limit, the transaction may fail even if sufficient funds are available.

4

Try a different card or payment method

If the issue persists, try a credit card from a different bank, or use an alternative payment method such as FriMi, Qplus or Helapay.

5

Wait and retry if velocity-blocked

If you made multiple failed attempts recently, wait 2–4 hours before trying again. The bank's velocity rule will typically be clear.

## What should merchants do?

While code 05 is issued by the cardholder's bank not by OnePay there are meaningful steps merchants can take to reduce the frequency of these declines and recover more revenue.

### Check your Merchant Category Code (MCC)

If your business was assigned an MCC that certain banks restrict (e.g., digital goods, software, subscriptions), you may see elevated code 05 rates from certain issuing banks. Contact OnePay support to review your MCC and determine if a reclassification is appropriate. Correct categorisation can meaningfully reduce friction.

## Card Decline Codes: Full Reference

Code 05 is the most common, but it's far from the only declining code you'll see in your OnePay dashboard. Here is a reference for the codes most frequently encountered in the Sri Lankan market:

| Code | Message | Meaning | Action |
| --- | --- | --- | --- |
| 05 | Do Not Honour | Generic bank decline fraud score, limits, e-commerce disabled, or velocity | Contact bank |
| 51 | Insufficient Funds | Card balance or credit limit too low for the transaction amount | Don't retry |
| 14 | Invalid Card Number | Card number entered incorrectly or card does not exist | Re-enter details |
| 54 | Expired Card | Card's expiry date has passed | Use new card |
| 41 | Lost Card — Pick Up | Card has been reported lost by the cardholder | Do not retry |
| 43 | Stolen Card — Pick Up | Card has been reported stolen | Flag for review |
| 57 | Transaction Not Permitted | This card type is not allowed to make this transaction (e.g., e-commerce blocked at card level) | Enable online payments |
| 61 | Exceeds Withdrawal Limit | Daily or per-transaction limit exceeded | Increase limit |
| 65 | Exceeds Frequency Limit | Too many transactions attempted in a short period | Retry after 2–4 hours |
| 91 | Issuer Not Available | The cardholder's bank is temporarily unreachable | Retry later |
| 96 | System Malfunction | Technical issue at the network or bank level — not a card problem | Retry later |
| 12 | Invalid Transaction | Transaction type or format not supported by the issuing bank | Contact OnePay support |
| 82 | CVV Incorrect | The 3-digit security code does not match bank records | Re-enter CVV |
| N7 | CVV2 Failure | Specific CVV2 mismatch — common with cards newly issued in Sri Lanka | Re-enter CVV |

##### Never retry codes 41 and 43

If you receive a "Lost Card" (41) or "Stolen Card" (43) response, **do not retry the transaction and do not fulfil the order**. These codes indicate the card is flagged as compromised. Log the attempt and if you suspect fraud, contact OnePay's risk team. Retrying these transactions can result in your merchant account being flagged by card networks.

## Frequently Asked Questions

### Is "Do Not Honour" always fraud-related?

No, and this is one of the most important points to communicate to your customers. A "Do Not Honour" response does not mean the transaction was flagged as fraudulent. It does not mean the customer's card has been compromised. It does not mean anything suspicious occurred.

In Sri Lanka's context, the overwhelming majority of code 05 declines are caused by routine card settings that haven't been configured for online use, not fraud. Banks simply default to the most restrictive setting to protect customers who might not know that online payment settings need to be manually enabled.

### Can I force a "Do Not Honour" transaction through?

No. When a bank returns code 05, the authorisation is definitively declined. There is no mechanism for a merchant or payment gateway to override a bank's decline decision.

### Will retrying a "Do Not Honour" cause problems?

Retrying once or twice after a customer has taken corrective action is perfectly fine. However, repeatedly retrying without addressing the underlying cause can trigger velocity blocks.

### Why does my customer see "Do Not Honour" on a brand-new card?

New cards from Sri Lankan banks are often issued with e-commerce transactions disabled as a default security measure. The customer simply needs to activate online payments in their banking app.

### Does OnePay charge for declined transactions?

OnePay does not charge transaction fees for failed or declined payments. You are only charged on successful transactions. Declined authorisations incur no cost.

### Does "Do Not Honour" affect my merchant account standing?

Code 05 declines initiated by the issuing bank do not negatively affect your OnePay merchant account or your standing with card networks. However, if your overall decline rate is unusually high, it may indicate a configuration issue worth reviewing with OnePay support.

---

## OnePay Learning Center Basics

**Category**: Blog / Technical Articles  
**Source URL**: https://docs.onepay.lk/blogs/learning-center

# Welcome to the Onepay Learning Center | Blogs

## The Basics Guide

### Initial onetime setup fee

Click the Proceed to Pay button to pay the one-time setup fee of LKR 1500. Your portal will be activated for integration once the payment is completed. . Once you make the payment, you will receive a confirmation email. To download a PDF receipt, please access https://app.oneid.ink/login

### Password reset

You would have received an email from noreply@onepay.lk to change the password. Please check your spam folder if you cannot find it in your inbox.

Click the "Click here" button to enter your first-time password reset.

You will see this window where you can set up your new password. Please follow the password requirements shown in the tips below.

### Onepay Merchant Portal Configuration

Login to the Onepay website to access the merchant portal for one-time configuration to enable payment acceptance and package updates.

Visit https://www.onepay.lk/

Click "login as a merchant" in the right corner of the onepay website and you will open a new popup with following URL https://merchant.onepay.lk/authentication/login for the portal login.

Enter your registered email address and password to login to the portal for the configuration

### Onepay Developer Configurations (Sandbox Create)

In the sidebar, navigate to "Developer Configurations" and select "IPG Apps"

1. ### Click the "Update" button after entering your developer name, phone number, and email address to begin the configuration process.
2. ### Click the green "Add New App" button located on the right side of the view

   A popup window will appear where you need to enter the following required information:

   App Name\*: Your business name

   Status Callback Configuration: Add your callback URL to capture transaction response data. This should be a GET request that processes a JSON file. For more information, please check our API documentation: https://docs.onepay.lk/#introduction

   For additional security, you may also configure a callback token.

   Click the "Add" button. After submitting the initial information.

### Developer Testing

Now you can see your developed app below. Click on it to view the app details for testing.

URL: https://merchant.onepay.lk/pages/developer-configurations/ipg-apps Click the three-dot menu icon to view the developer configuration details.

Now you can see the developer details needed to connect with your platform. Copy the APP ID, App Token, and Hash salt to properly connect Onepay with your platform. This requires technical expertise to implement, so please share our API documentation and configuration files with your technical team.

Click here

Request to Go Live (Sandbox Mode to Live Mode)

### Request to Go Live (Sandbox Mode to Live Mode)

Once you have completed the integration and testing, you can request to go live. Click the three-dot menu icon to view the developer configuration details, then click "Request to Go Live"

Click the star (\*) symbol in the box below to verify the CAPTCHA, check the terms and conditions checkbox, and click the "Request to Go Live" button. Review our Terms and Conditions: https://www.onepay.lk/agreement.html (v2.2)

Contact us if you need additional support or have suggestions for improvement. Your valuable feedback helps us enhance our services.

---

