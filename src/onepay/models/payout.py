"""Payout / settlement models."""

from __future__ import annotations

from pydantic import BaseModel, Field


class PayoutTransactionData(BaseModel):
    """Settlement data for a single transaction."""

    onepay_transaction_id: str | None = None
    order_id: str | None = None
    currency: str | None = None
    net_amount: str | None = None
    commission_rate: str | None = None
    commission_amount: str | None = None
    settlement_amount: float | None = None
    settlement_date: str | None = None


class PayoutTransactionResponse(BaseModel):
    """Response from the single transaction payout lookup."""

    status: int = 200
    message: str = ""
    data: PayoutTransactionData | None = None


class PayoutTransactionListData(BaseModel):
    """Paginated payout transaction list data."""

    count: int = Field(0, description="Total number of matching transactions")
    page: int = Field(1, description="Current page number")
    page_size: int = Field(20, description="Number of results per page")
    results: list[PayoutTransactionData] = Field(default_factory=list)


class PayoutTransactionListResponse(BaseModel):
    """Response from the paginated payout transaction list."""

    status: int = 200
    message: str = ""
    data: PayoutTransactionListData | None = None
