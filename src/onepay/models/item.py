"""Item management models."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

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
    image_url: Optional[str] = Field(None, description="Public URL of a product image")
    metadata: Optional[Dict[str, Any]] = Field(
        None, description="Arbitrary key-value pairs for internal cataloguing"
    )


class UpdateItemRequest(BaseModel):
    """Parameters for updating an existing item. Only provided fields are updated."""

    app_id: str = Field(..., description="Your application identifier")
    name: Optional[str] = Field(None, description="Updated item name")
    price: Optional[float] = Field(None, description="Updated unit price")
    description: Optional[str] = Field(None, description="Updated description")
    image_url: Optional[str] = Field(None, description="Updated product image URL")
    metadata: Optional[List[Dict[str, Any]]] = Field(
        None, description="Updated metadata array (replaces existing)"
    )


class ItemData(BaseModel):
    """Representation of a single item from the API."""

    item_id: str = Field(..., description="Unique identifier for the item")
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None
    currency: Optional[str] = None
    image_url: Optional[str] = None
    is_deleted: bool = False
    metadata: Optional[List[ItemMetadata]] = None


class CreateItemResponse(BaseModel):
    """Response from creating an item."""

    status: int = 200
    message: str = ""
    data: Optional[Dict[str, str]] = None

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
    data: Optional[List[ItemData]] = None


class UpdateItemResponse(BaseModel):
    """Response from updating an item."""

    status: int = 200
    message: str = ""
    data: Optional[Dict[str, str]] = None


class DeleteItemResponse(BaseModel):
    """Response from deleting an item."""

    status: int = 200
    message: str = ""
