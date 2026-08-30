"""Payment link models."""

from __future__ import annotations

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class CreatePaymentLinkRequest(BaseModel):
    """Parameters for creating a payment link."""

    amount: str = Field(..., description="Payment amount as string")
    currency: str = Field(..., description="Currency code")
    reference_number: str = Field(..., description="Your internal reference number")
    customer_first_name: str = Field(..., description="Customer's first name")
    customer_last_name: str = Field(..., description="Customer's last name")
    customer_email: str = Field(..., description="Customer's email address")
    customer_phone_number: str = Field(..., description="Customer's phone number")
    description: Optional[str] = Field(None, description="Description of the payment")
    expiration_date: Optional[str] = Field(
        None, description="Expiry date in YYYY-MM-DD format"
    )
    allow_partial_payment: bool = Field(
        False, description="Allow partial payments"
    )
    minimum_partial_amount: Optional[str] = Field(
        None, description="Minimum partial payment amount"
    )


class PaymentLinkData(BaseModel):
    """Representation of a payment link from the API."""

    link_id: Optional[str] = None
    link_url: Optional[str] = None
    amount: Optional[str] = None
    currency: Optional[str] = None
    reference_number: Optional[str] = None
    description: Optional[str] = None
    customer_first_name: Optional[str] = None
    customer_last_name: Optional[str] = None
    customer_email: Optional[str] = None
    customer_phone_number: Optional[str] = None
    expiration_date: Optional[str] = None
    is_complete: bool = False
    is_delete: bool = False
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class CreatePaymentLinkResponse(BaseModel):
    """Response from creating a payment link."""

    status: int = 200
    message: str = ""
    data: Optional[PaymentLinkData] = None


class GetPaymentLinkResponse(BaseModel):
    """Response from retrieving a payment link."""

    status: int = 200
    message: str = ""
    data: Optional[PaymentLinkData] = None


class UpdatePaymentLinkResponse(BaseModel):
    """Response from updating a payment link."""

    status: int = 200
    message: str = ""
    data: Optional[PaymentLinkData] = None


class DeletePaymentLinkResponse(BaseModel):
    """Response from deleting a payment link."""

    status: int = 200
    message: str = ""
