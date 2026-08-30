"""Payment link models."""

from __future__ import annotations

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
    description: str | None = Field(None, description="Description of the payment")
    expiration_date: str | None = Field(None, description="Expiry date in YYYY-MM-DD format")
    allow_partial_payment: bool = Field(False, description="Allow partial payments")
    minimum_partial_amount: str | None = Field(None, description="Minimum partial payment amount")


class PaymentLinkData(BaseModel):
    """Representation of a payment link from the API."""

    link_id: str | None = None
    link_url: str | None = None
    amount: str | None = None
    currency: str | None = None
    reference_number: str | None = None
    description: str | None = None
    customer_first_name: str | None = None
    customer_last_name: str | None = None
    customer_email: str | None = None
    customer_phone_number: str | None = None
    expiration_date: str | None = None
    is_complete: bool = False
    is_delete: bool = False
    created_at: str | None = None
    updated_at: str | None = None


class CreatePaymentLinkResponse(BaseModel):
    """Response from creating a payment link."""

    status: int = 200
    message: str = ""
    data: PaymentLinkData | None = None


class GetPaymentLinkResponse(BaseModel):
    """Response from retrieving a payment link."""

    status: int = 200
    message: str = ""
    data: PaymentLinkData | None = None


class UpdatePaymentLinkResponse(BaseModel):
    """Response from updating a payment link."""

    status: int = 200
    message: str = ""
    data: PaymentLinkData | None = None


class DeletePaymentLinkResponse(BaseModel):
    """Response from deleting a payment link."""

    status: int = 200
    message: str = ""
