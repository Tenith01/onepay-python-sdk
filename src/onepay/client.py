"""OnePay SDK client — the main entry point.

Provides :class:`OnePay` (sync) and :class:`AsyncOnePay` (async) clients
that expose all API resources as namespaced attributes.
"""

from __future__ import annotations

from onepay._config import OnePayConfig
from onepay._http import AsyncHttpClient, SyncHttpClient
from onepay.resources.cards import AsyncCardResource, CardResource
from onepay.resources.checkout import AsyncCheckoutResource, CheckoutResource
from onepay.resources.customers import AsyncCustomerResource, CustomerResource
from onepay.resources.items import AsyncItemResource, ItemResource
from onepay.resources.payment_links import (
    AsyncPaymentLinkResource,
    PaymentLinkResource,
)
from onepay.resources.payouts import AsyncPayoutResource, PayoutResource
from onepay.resources.refunds import AsyncRefundResource, RefundResource
from onepay.resources.subscriptions import (
    AsyncSubscriptionResource,
    SubscriptionResource,
)
from onepay.resources.transactions import (
    AsyncTransactionResource,
    TransactionResource,
)


class OnePay:
    """Synchronous OnePay client.

    All API resources are available as attributes::

        from onepay import OnePay

        client = OnePay(
            app_id="...",
            hash_salt="...",
            app_token="...",
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
        print(result.redirect_url)
    """

    def __init__(
        self,
        *,
        app_id: str = "",
        hash_salt: str = "",
        app_token: str = "",
        api_key: str = "",
        access_token: str = "",
        base_url: str = "https://api.onepay.lk",
        timeout: float = 30.0,
        max_retries: int = 3,
        debug: bool = False,
    ) -> None:
        self._config = OnePayConfig(
            app_id=app_id,
            hash_salt=hash_salt,
            app_token=app_token,
            api_key=api_key,
            access_token=access_token,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            debug=debug,
        )
        self._http = SyncHttpClient(self._config)

        # Resource namespaces
        self.checkout = CheckoutResource(self._http, self._config)
        self.transactions = TransactionResource(self._http, self._config)
        self.items = ItemResource(self._http, self._config)
        self.payment_links = PaymentLinkResource(self._http, self._config)
        self.customers = CustomerResource(self._http, self._config)
        self.cards = CardResource(self._http, self._config)
        self.refunds = RefundResource(self._http, self._config)
        self.payouts = PayoutResource(self._http, self._config)
        self.subscriptions = SubscriptionResource(self._http, self._config)

    def close(self) -> None:
        """Close the underlying HTTP client and release connections."""
        self._http.close()

    def __enter__(self) -> OnePay:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    def __repr__(self) -> str:
        return self._config.redacted_repr()


class AsyncOnePay:
    """Asynchronous OnePay client.

    All API resources are available as attributes with ``await``::

        from onepay import AsyncOnePay

        client = AsyncOnePay(
            app_id="...",
            hash_salt="...",
            app_token="...",
        )

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
    """

    def __init__(
        self,
        *,
        app_id: str = "",
        hash_salt: str = "",
        app_token: str = "",
        api_key: str = "",
        access_token: str = "",
        base_url: str = "https://api.onepay.lk",
        timeout: float = 30.0,
        max_retries: int = 3,
        debug: bool = False,
    ) -> None:
        self._config = OnePayConfig(
            app_id=app_id,
            hash_salt=hash_salt,
            app_token=app_token,
            api_key=api_key,
            access_token=access_token,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            debug=debug,
        )
        self._http = AsyncHttpClient(self._config)

        # Resource namespaces
        self.checkout = AsyncCheckoutResource(self._http, self._config)
        self.transactions = AsyncTransactionResource(self._http, self._config)
        self.items = AsyncItemResource(self._http, self._config)
        self.payment_links = AsyncPaymentLinkResource(self._http, self._config)
        self.customers = AsyncCustomerResource(self._http, self._config)
        self.cards = AsyncCardResource(self._http, self._config)
        self.refunds = AsyncRefundResource(self._http, self._config)
        self.payouts = AsyncPayoutResource(self._http, self._config)
        self.subscriptions = AsyncSubscriptionResource(self._http, self._config)

    async def close(self) -> None:
        """Close the underlying async HTTP client."""
        await self._http.close()

    async def __aenter__(self) -> AsyncOnePay:
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.close()

    def __repr__(self) -> str:
        return self._config.redacted_repr()
