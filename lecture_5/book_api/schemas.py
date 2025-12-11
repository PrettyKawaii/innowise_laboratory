from pydantic import BaseModel
from typing import Optional


class BookCreate(BaseModel):
    """Schema for creating a new book."""
    title: str  # required
    author: str  # required
    year: Optional[int] = None  # optional


class BookUpdate(BaseModel):
    """Schema for updating book fields (all optional)."""
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None


class BookResponse(BaseModel):
    """Schema for book response (what gets returned)."""
    id: int
    title: str
    author: str
    year: Optional[int] = None
    
    class Config:
        # allows conversion from SQLAlchemy model
        from_attributes = True