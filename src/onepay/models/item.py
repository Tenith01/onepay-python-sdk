"""Item management models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class ItemMetadata(BaseModel):
    """A single metadata key-value pair on an item."""

    key: str
    value: str
    is_deleted: bool = False


class CreateItemRequest(BaseModel):
    """Parameters for creating a new item."""

    name: str = Field(..., description="Product or service name")
    description: str = Field(..., description="Short description of the item")
    price: float = Field(..., description="Unit price, e.g. 1400.99")
    currency: str = Field(..., description="Currency code: LKR or USD")
    image_url: str | None = Field(None, description="Public URL of a product image")
    metadata: dict[str, Any] | None = Field(
        None, description="Arbitrary key-value pairs for internal cataloguing"
    )


class UpdateItemRequest(BaseModel):
    """Parameters for updating an existing item. Only provided fields are updated."""

    app_id: str = Field(..., description="Your application identifier")
    name: str | None = Field(None, description="Updated item name")
    price: float | None = Field(None, description="Updated unit price")
    description: str | None = Field(None, description="Updated description")
    image_url: str | None = Field(None, description="Updated product image URL")
    metadata: list[dict[str, Any]] | None = Field(
        None, description="Updated metadata array (replaces existing)"
    )


class ItemData(BaseModel):
    """Representation of a single item from the API."""

    item_id: str = Field(..., description="Unique identifier for the item")
    name: str | None = None
    description: str | None = None
    price: str | None = None
    currency: str | None = None
    image_url: str | None = None
    is_deleted: bool = False
    metadata: list[ItemMetadata] | None = None


class CreateItemResponse(BaseModel):
    """Response from creating an item."""

    status: int = 200
    message: str = ""
    data: dict[str, str] | None = None

    @property
    def item_id(self) -> str:
        """The ID of the newly created item."""
        if self.data and "item_id" in self.data:
            return self.data["item_id"]
        return ""


class ListItemsResponse(BaseModel):
    """Response from listing all items."""

    status: int = 200
    message: str = ""
    data: list[ItemData] | None = None


class UpdateItemResponse(BaseModel):
    """Response from updating an item."""

    status: int = 200
    message: str = ""
    data: dict[str, str] | None = None


class DeleteItemResponse(BaseModel):
    """Response from deleting an item."""

    status: int = 200
    message: str = ""
