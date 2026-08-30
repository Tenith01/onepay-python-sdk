"""Customer models for Card on File / Tokenizer API."""

from __future__ import annotations

from typing import Any, List, Optional

from onepay.models.card import CardData

from pydantic import BaseModel, Field


class CreateCustomerRequest(BaseModel):
    """Parameters for creating a new customer and requesting a card token."""

    app_id: str = Field(..., description="Your application identifier")
    first_name: str = Field(..., description="Customer's first name")
    last_name: str = Field(..., description="Customer's last name")
    email: str = Field(..., description="Customer's email address")
    phone_number: str = Field(
        ..., description="Phone number with country code, e.g. +94771234567"
    )
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
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    redirect_url: Optional[str] = None
    cards: Optional[List[CardData]] = None
    transactions: Optional[List[CustomerTransactionData]] = None


class CreateCustomerResponse(BaseModel):
    """Response from creating a customer."""

    status: int = 200
    data: Optional[CustomerData] = None


class ListCustomersResponse(BaseModel):
    """Response from listing all customers."""

    status: int = 200
    data: Optional[List[CustomerData]] = None


class GetCustomerResponse(BaseModel):
    """Response from retrieving a single customer."""

    status: int = 200
    data: Optional[CustomerData] = None


class CustomerTransactionData(BaseModel):
    """Representation of a customer transaction."""

    transaction_id: Optional[str] = None
    amount: Optional[str] = None
    currency: Optional[str] = None
    status: Optional[bool] = None
    token_id: Optional[str] = None
    created_at: Optional[str] = None


class ListCustomerTransactionsResponse(BaseModel):
    """Response from listing a customer's transactions."""

    status: int = 200
    data: Optional[List[CustomerTransactionData]] = None
