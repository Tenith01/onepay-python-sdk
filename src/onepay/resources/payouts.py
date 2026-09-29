"""Payouts resource — transaction lookup and paginated listing."""

from __future__ import annotations

import math
from typing import TYPE_CHECKING

from onepay._auth import build_auth_header
from onepay.models.payout import (
    PayoutTransactionData,
    PayoutTransactionListResponse,
    PayoutTransactionResponse,
)

if TYPE_CHECKING:
    from collections.abc import AsyncIterator, Iterator

    from onepay._config import OnePayConfig
    from onepay._http import AsyncHttpClient, SyncHttpClient


class PayoutResource:
    """Sync payout operations."""

    def __init__(self, http: SyncHttpClient, config: OnePayConfig) -> None:
        self._http = http
        self._config = config

    def get_transaction(self, *, onepay_transaction_id: str) -> PayoutTransactionResponse:
        """Look up settlement details for a single transaction.

        Args:
            onepay_transaction_id: The OnePay transaction ID.

        Returns:
            :class:`PayoutTransactionResponse` with settlement breakdown.
        """
        headers = build_auth_header(self._config.get_app_token_or_raise())

        response = self._http.request(
            "GET",
            "/v3/payout/transaction/",
            params={"onepay_transaction_id": onepay_transaction_id},
            headers=headers,
        )
        return PayoutTransactionResponse.model_validate(response)

    def list_transactions(
        self,
        *,
        start_date: str,
        end_date: str,
        page_size: int = 20,
    ) -> Iterator[PayoutTransactionData]:
        """Iterate over all payout transactions in a date range.

        Automatically handles pagination — yields one transaction at a time
        across all pages.

        Args:
            start_date: Start date in ``YYYY-MM-DD`` format (inclusive).
            end_date: End date in ``YYYY-MM-DD`` format (inclusive).
            page_size: Records per page (default 20, max recommended 100).

        Yields:
            :class:`PayoutTransactionData` objects.
        """
        headers = build_auth_header(self._config.get_app_token_or_raise())
        page = 1

        while True:
            response = self._http.request(
                "GET",
                "/v3/payout/transactions/",
                params={
                    "start_date": start_date,
                    "end_date": end_date,
                    "page": page,
                    "page_size": page_size,
                },
                headers=headers,
            )

            parsed = PayoutTransactionListResponse.model_validate(response)

            if parsed.data is None or not parsed.data.results:
                return

            yield from parsed.data.results

            total_pages = math.ceil(parsed.data.count / page_size) if parsed.data.count else 1
            if page >= total_pages:
                return

            page += 1

    def list_transactions_page(
        self,
        *,
        start_date: str,
        end_date: str,
        page: int = 1,
        page_size: int = 20,
    ) -> PayoutTransactionListResponse:
        """Fetch a single page of payout transactions.

        Args:
            start_date: Start date in ``YYYY-MM-DD`` format.
            end_date: End date in ``YYYY-MM-DD`` format.
            page: Page number (starting at 1).
            page_size: Records per page.

        Returns:
            :class:`PayoutTransactionListResponse` with paginated results.
        """
        headers = build_auth_header(self._config.get_app_token_or_raise())

        response = self._http.request(
            "GET",
            "/v3/payout/transactions/",
            params={
                "start_date": start_date,
                "end_date": end_date,
                "page": page,
                "page_size": page_size,
            },
            headers=headers,
        )
        return PayoutTransactionListResponse.model_validate(response)


class AsyncPayoutResource:
    """Async payout operations."""

    def __init__(self, http: AsyncHttpClient, config: OnePayConfig) -> None:
        self._http = http
        self._config = config

    async def get_transaction(self, *, onepay_transaction_id: str) -> PayoutTransactionResponse:
        """Async version of :meth:`PayoutResource.get_transaction`."""
        headers = build_auth_header(self._config.get_app_token_or_raise())

        response = await self._http.request(
            "GET",
            "/v3/payout/transaction/",
            params={"onepay_transaction_id": onepay_transaction_id},
            headers=headers,
        )
        return PayoutTransactionResponse.model_validate(response)

    async def list_transactions_page(
        self,
        *,
        start_date: str,
        end_date: str,
        page: int = 1,
        page_size: int = 20,
    ) -> PayoutTransactionListResponse:
        """Async version of :meth:`PayoutResource.list_transactions_page`."""
        headers = build_auth_header(self._config.get_app_token_or_raise())

        response = await self._http.request(
            "GET",
            "/v3/payout/transactions/",
            params={
                "start_date": start_date,
                "end_date": end_date,
                "page": page,
                "page_size": page_size,
            },
            headers=headers,
        )
        return PayoutTransactionListResponse.model_validate(response)

    async def list_transactions(
        self,
        *,
        start_date: str,
        end_date: str,
        page_size: int = 20,
    ) -> AsyncIterator[PayoutTransactionData]:
        """Async version of :meth:`PayoutResource.list_transactions`."""
        headers = build_auth_header(self._config.get_app_token_or_raise())
        page = 1

        while True:
            response = await self._http.request(
                "GET",
                "/v3/payout/transactions/",
                params={
                    "start_date": start_date,
                    "end_date": end_date,
                    "page": page,
                    "page_size": page_size,
                },
                headers=headers,
            )

            parsed = PayoutTransactionListResponse.model_validate(response)

            if parsed.data is None or not parsed.data.results:
                return

            for item in parsed.data.results:
                yield item

            total_pages = math.ceil(parsed.data.count / page_size) if parsed.data.count else 1
            if page >= total_pages:
                return

            page += 1
