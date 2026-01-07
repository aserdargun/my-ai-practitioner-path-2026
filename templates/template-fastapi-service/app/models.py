"""Pydantic models for request/response validation."""

from pydantic import BaseModel
from typing import Optional


class PredictRequest(BaseModel):
    """Request model for predictions."""
    text: str
    options: Optional[dict] = None

    class Config:
        json_schema_extra = {
            "example": {
                "text": "Sample input text",
                "options": {"threshold": 0.5}
            }
        }


class PredictResponse(BaseModel):
    """Response model for predictions."""
    result: float
    input_text: str
    success: bool
    error: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "result": 0.85,
                "input_text": "Sample input text",
                "success": True
            }
        }


class Item(BaseModel):
    """Item model."""
    id: int
    name: str
    description: Optional[str] = None
    price: float
    is_active: bool = True


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    app: str
    debug: bool
