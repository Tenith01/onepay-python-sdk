"""Customer models for Card on File / Tokenizer API."""

from __future__ import annotations

from pydantic import BaseModel, Field

from onepay.models.card import CardData  # noqa: TCH001


class CreateCustomerRequest(BaseModel):
    """Parameters for creating a new customer and requesting a card token."""

    app_id: str = Field(..., description="Your application identifier")
    first_name: str = Field(..., description="Customer's first name")
    last_name: str = Field(..., description="Customer's last name")
    email: str = Field(..., description="Customer's email address")
    phone_number: str = Field(..., description="Phone number with country code, e.g. +94771234567")
    address: str = Field(..., description="Customer's billing or physical address")
    redirect_url: str = Field(
        ...,
        description="URL the customer will be redirected to after adding their card",
    )


class RequestTokenRequest(BaseModel):
    """Parameters for requesting a new card token for an existing customer."""

    app_id: str = Field(..., description="Your application identifier")
    customer_id: str = Field(..., description="Existing customer identifier")
    redirect_url: str = Field(
        ...,
        description="URL the customer will be redirected to after adding their card",
    )


class CustomerData(BaseModel):
    """Representation of a customer from the API."""

    customer_id: str = Field(..., description="Unique customer identifier")
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    phone_number: str | None = None
    address: str | None = None
    redirect_url: str | None = None
    cards: list[CardData] | None = None
    transactions: list[CustomerTransactionData] | None = None


class CreateCustomerResponse(BaseModel):
    """Response from creating a customer."""

    status: int = 200
    data: CustomerData | None = None


class ListCustomersResponse(BaseModel):
    """Response from listing all customers."""

    status: int = 200
    data: list[CustomerData] | None = None


class GetCustomerResponse(BaseModel):
    """Response from retrieving a single customer."""

    status: int = 200
    data: CustomerData | None = None


class CustomerTransactionData(BaseModel):
    """Representation of a customer transaction."""

    transaction_id: str | None = None
    amount: str | None = None
    currency: str | None = None
    status: bool | None = None
    token_id: str | None = None
    created_at: str | None = None


class ListCustomerTransactionsResponse(BaseModel):
    """Response from listing a customer's transactions."""

    status: int = 200
    data: list[CustomerTransactionData] | None = None


CustomerData.model_rebuild()
CreateCustomerResponse.model_rebuild()
ListCustomersResponse.model_rebuild()
GetCustomerResponse.model_rebuild()
