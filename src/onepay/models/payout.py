"""Payout / settlement models."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class PayoutTransactionData(BaseModel):
    """Settlement data for a single transaction."""

    onepay_transaction_id: Optional[str] = None
    order_id: Optional[str] = None
    currency: Optional[str] = None
    net_amount: Optional[str] = None
    commission_rate: Optional[str] = None
    commission_amount: Optional[str] = None
    settlement_amount: Optional[float] = None
    settlement_date: Optional[str] = None


class PayoutTransactionResponse(BaseModel):
    """Response from the single transaction payout lookup."""

    status: int = 200
    message: str = ""
    data: Optional[PayoutTransactionData] = None


class PayoutTransactionListData(BaseModel):
    """Paginated payout transaction list data."""

    count: int = Field(0, description="Total number of matching transactions")
    page: int = Field(1, description="Current page number")
    page_size: int = Field(20, description="Number of results per page")
    results: List[PayoutTransactionData] = Field(default_factory=list)


class PayoutTransactionListResponse(BaseModel):
    """Response from the paginated payout transaction list."""

    status: int = 200
    message: str = ""
    data: Optional[PayoutTransactionListData] = None
