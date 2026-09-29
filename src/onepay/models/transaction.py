"""Transaction status models."""

from __future__ import annotations

from pydantic import BaseModel, Field


class TransactionStatusRequest(BaseModel):
    """Parameters for querying transaction status."""

    app_id: str = Field(..., description="Your application identifier")
    onepay_transaction_id: str = Field(
        ..., description="The transaction ID returned when the transaction was created"
    )


class TransactionStatusData(BaseModel):
    """Transaction status data from the API response."""

    status: int | bool = Field(..., description="True or HTTP 200 if the payment was successful")
    ipg_transaction_id: str = Field(..., description="OnePay's internal transaction identifier")
    amount: float | str | None = Field(None, description="The amount charged")
    currency: str | None = Field(None, description="Currency of the transaction")
    paid_on: str | None = Field(
        None, description="Timestamp of payment in YYYY-MM-DD HH:mm:ss format"
    )


class TransactionStatusResponse(BaseModel):
    """Parsed response from the transaction status API."""

    status: int | bool = Field(..., description="True or HTTP 200 if the payment was successful")
    data: TransactionStatusData | None = None
