"""Transaction status models."""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class TransactionStatusRequest(BaseModel):
    """Parameters for querying transaction status."""

    app_id: str = Field(..., description="Your application identifier")
    onepay_transaction_id: str = Field(
        ..., description="The transaction ID returned when the transaction was created"
    )


class TransactionStatusData(BaseModel):
    """Transaction status data from the API response."""

    status: bool = Field(..., description="True if the payment was successful")
    ipg_transaction_id: str = Field(
        ..., description="OnePay's internal transaction identifier"
    )
    amount: Optional[str] = Field(None, description="The amount charged")
    currency: Optional[str] = Field(None, description="Currency of the transaction")
    paid_on: Optional[str] = Field(
        None, description="Timestamp of payment in YYYY-MM-DD HH:mm:ss format"
    )


class TransactionStatusResponse(BaseModel):
    """Parsed response from the transaction status API."""

    status: bool = Field(..., description="True if the payment was successful")
    data: Optional[TransactionStatusData] = None
