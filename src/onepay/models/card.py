"""Card (token) and charge models for Card on File API."""

from __future__ import annotations

from pydantic import BaseModel, Field


class CardData(BaseModel):
    """Representation of a saved card token."""

    token_id: str = Field(..., description="Secure card token identifier")
    card_type: str | None = Field(None, description="Card network, e.g. Visa, Mastercard")
    masked_number: str | None = Field(
        None, description="Masked card number, e.g. **** **** **** 4242"
    )
    expiry: str | None = Field(None, description="Card expiry in MM/YY format")
    is_deleted: bool = False


class ListCardsResponse(BaseModel):
    """Response from listing a customer's cards."""

    status: int = 200
    data: list[CardData] | None = None


class GetCardResponse(BaseModel):
    """Response from retrieving a single card."""

    status: int = 200
    data: CardData | None = None


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

    transaction_id: str | None = None
    status: bool | None = None
    amount: str | None = None
    currency: str | None = None
    token_id: str | None = None


class ChargeCardResponse(BaseModel):
    """Response from charging a card token."""

    status: int = 200
    message: str = ""
    data: ChargeCardResponseData | None = None
