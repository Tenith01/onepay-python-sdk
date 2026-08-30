"""Refund models."""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field, model_validator


class RefundRequest(BaseModel):
    """Parameters for initiating a refund.

    For full refunds, set ``is_partially=False`` (the default) and omit ``amount``.
    For partial refunds, set ``is_partially=True`` and provide ``amount``.
    """

    onepay_transaction_id: str = Field(
        ..., description="The OnePay transaction ID to refund"
    )
    refund_reason: str = Field(
        ...,
        description=(
            "One of: DUPLICATED, FRAUDULENT, OUT_OF_ORDER, "
            "REQUESTED_BY_CUSTOMER, OTHER"
        ),
    )
    is_partially: bool = Field(False, description="True for partial refund")
    amount: Optional[float] = Field(
        None, description="Partial refund amount (required if is_partially=True)"
    )
    refund_note: Optional[str] = Field(
        None, description="Free-text note for this refund"
    )

    @model_validator(mode="after")
    def _validate_partial_amount(self) -> RefundRequest:
        if self.is_partially and self.amount is None:
            raise ValueError("amount is required when is_partially is True")
        return self


class RefundResponseData(BaseModel):
    """Data from a successful refund response."""

    ipg_transaction_id: Optional[str] = None
    refund_id: Optional[int] = None
    status: Optional[str] = None
    is_partially: Optional[bool] = None
    requested_amount: Optional[str] = None
    refund_reason: Optional[str] = None


class RefundResponse(BaseModel):
    """Parsed response from the refund API."""

    status: int = 200
    message: str = ""
    data: Optional[RefundResponseData] = None
