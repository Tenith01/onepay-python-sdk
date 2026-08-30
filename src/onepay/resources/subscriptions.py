"""Subscriptions resource — experimental/beta.

The subscription endpoint (POST /v3/subscription/) is used by the JS SDK
but is not fully documented in the OnePay API docs. This resource exposes
it for completeness.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from onepay._auth import build_auth_header, generate_hash

if TYPE_CHECKING:
    from onepay._config import OnePayConfig
    from onepay._http import AsyncHttpClient, SyncHttpClient


class SubscriptionResource:
    """Sync subscription operations (experimental)."""

    def __init__(self, http: SyncHttpClient, config: OnePayConfig) -> None:
        self._http = http
        self._config = config

    def create(
        self,
        *,
        name: str,
        amount: float,
        currency: str,
        interval: str,
        interval_count: int,
        days_until_due: int,
        customer_first_name: str,
        customer_last_name: str,
        customer_email: str,
        customer_phone: str | None = None,
        trial_period_days: int | None = None,
    ) -> dict[str, Any]:
        """Create a subscription (experimental).

        Args:
            name: Subscription plan name.
            amount: Amount per billing cycle.
            currency: Currency code.
            interval: Billing interval (``day``, ``week``, ``month``, ``year``).
            interval_count: Number of intervals between charges.
            days_until_due: Grace period before overdue.
            customer_first_name: Customer's first name.
            customer_last_name: Customer's last name.
            customer_email: Customer's email.
            customer_phone: Customer's phone number.
            trial_period_days: Free trial days before first charge.

        Returns:
            Raw API response as a dictionary.
        """
        app_id = self._config.get_app_id_or_raise()
        app_token = self._config.get_app_token_or_raise()

        amount_str = f"{amount:.2f}"

        payload: dict[str, Any] = {
            "app_id": app_id,
            "name": name,
            "amount": float(amount_str),
            "currency": currency,
            "interval": interval,
            "interval_count": interval_count,
            "days_until_due": days_until_due,
            "customer_details": {
                "first_name": customer_first_name,
                "last_name": customer_last_name,
                "email": customer_email,
            },
        }

        if customer_phone:
            payload["customer_details"]["phone_number"] = customer_phone
        if trial_period_days is not None:
            payload["trial_period_days"] = trial_period_days

        # Hash uses app_token as salt for subscriptions (matching JS SDK behavior)
        hash_value = generate_hash(app_id, currency, amount_str, app_token)
        payload["hash"] = hash_value

        headers = build_auth_header(app_token)

        return self._http.request(
            "POST",
            "/v3/subscription/",
            json=payload,
            headers=headers,
        )


class AsyncSubscriptionResource:
    """Async subscription operations (experimental)."""

    def __init__(self, http: AsyncHttpClient, config: OnePayConfig) -> None:
        self._http = http
        self._config = config

    async def create(
        self,
        *,
        name: str,
        amount: float,
        currency: str,
        interval: str,
        interval_count: int,
        days_until_due: int,
        customer_first_name: str,
        customer_last_name: str,
        customer_email: str,
        customer_phone: str | None = None,
        trial_period_days: int | None = None,
    ) -> dict[str, Any]:
        """Async version of :meth:`SubscriptionResource.create`."""
        app_id = self._config.get_app_id_or_raise()
        app_token = self._config.get_app_token_or_raise()

        amount_str = f"{amount:.2f}"

        payload: dict[str, Any] = {
            "app_id": app_id,
            "name": name,
            "amount": float(amount_str),
            "currency": currency,
            "interval": interval,
            "interval_count": interval_count,
            "days_until_due": days_until_due,
            "customer_details": {
                "first_name": customer_first_name,
                "last_name": customer_last_name,
                "email": customer_email,
            },
        }

        if customer_phone:
            payload["customer_details"]["phone_number"] = customer_phone
        if trial_period_days is not None:
            payload["trial_period_days"] = trial_period_days

        hash_value = generate_hash(app_id, currency, amount_str, app_token)
        payload["hash"] = hash_value

        headers = build_auth_header(app_token)

        return await self._http.request(
            "POST",
            "/v3/subscription/",
            json=payload,
            headers=headers,
        )
