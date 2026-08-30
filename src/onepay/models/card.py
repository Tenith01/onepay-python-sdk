"""Card (token) and charge models for Card on File API."""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class CardData(BaseModel):
    """Representation of a saved card token."""

    token_id: str = Field(..., description="Secure card token identifier")
    card_type: Optional[str] = Field(None, description="Card network, e.g. Visa, Mastercard")
    masked_number: Optional[str] = Field(
        None, description="Masked card number, e.g. **** **** **** 4242"
    )
    expiry: Optional[str] = Field(None, description="Card expiry in MM/YY format")
    is_deleted: bool = False


class ListCardsResponse(BaseModel):
    """Response from listing a customer's cards."""

    status: int = 200
    data: Optional[List[CardData]] = None


class GetCardResponse(BaseModel):
    """Response from retrieving a single card."""

    status: int = 200
    data: Optional[CardData] = None


class DeleteCardResponse(BaseModel):
    """Response from deleting (soft-delete) a card."""

    status: int = 200
    message: str = ""


class ChargeCardRequest(BaseModel):
    """Parameters for charging a saved card token."""

    app_id: str = Field(..., description="Your application identifier")
    token_id: str = Field(..., description="The saved card token to charge")
    amount: str = Field(..., description='Amount to charge as string, e.g. "1000.00"')
    currency: str = Field(..., description="Currency code, e.g. LKR or USD")


class ChargeCardResponseData(BaseModel):
    """Data from a successful card charge."""

    transaction_id: Optional[str] = None
    status: Optional[bool] = None
    amount: Optional[str] = None
    currency: Optional[str] = None
    token_id: Optional[str] = None


class ChargeCardResponse(BaseModel):
    """Response from charging a card token."""

    status: int = 200
    message: str = ""
    data: Optional[ChargeCardResponseData] = None
