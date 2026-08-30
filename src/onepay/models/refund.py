"""Refund models."""

from __future__ import annotations

from pydantic import BaseModel, Field, model_validator


class RefundRequest(BaseModel):
    """Parameters for initiating a refund.

    For full refunds, set ``is_partially=False`` (the default) and omit ``amount``.
    For partial refunds, set ``is_partially=True`` and provide ``amount``.
    """

    onepay_transaction_id: str = Field(..., description="The OnePay transaction ID to refund")
    refund_reason: str = Field(
        ...,
        description=("One of: DUPLICATED, FRAUDULENT, OUT_OF_ORDER, REQUESTED_BY_CUSTOMER, OTHER"),
    )
    is_partially: bool = Field(False, description="True for partial refund")
    amount: float | None = Field(
        None, description="Partial refund amount (required if is_partially=True)"
    )
    refund_note: str | None = Field(None, description="Free-text note for this refund")

    @model_validator(mode="after")
    def _validate_partial_amount(self) -> RefundRequest:
        if self.is_partially and self.amount is None:
            raise ValueError("amount is required when is_partially is True")
        return self


class RefundResponseData(BaseModel):
    """Data from a successful refund response."""

    ipg_transaction_id: str | None = None
    refund_id: int | None = None
    status: str | None = None
    is_partially: bool | None = None
    requested_amount: str | None = None
    refund_reason: str | None = None


class RefundResponse(BaseModel):
    """Parsed response from the refund API."""

    status: int = 200
    message: str = ""
    data: RefundResponseData | None = None
