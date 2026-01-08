from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class ReviewBase(BaseModel):
    target_id: str
    target_type: str
    rating: float
    comment: Optional[str]
    helpful_count: Optional[float]
    author_name: Optional[str]

class ReviewCreate(BaseModel):
    target_id: str
    target_type: str
    rating: float
    comment: Optional[str] = None
    helpful_count: Optional[float] = None
    author_name: Optional[str] = None

class ReviewUpdate(BaseModel):
    target_id: Optional[str] = None
    target_type: Optional[str] = None
    rating: Optional[float] = None
    comment: Optional[str] = None
    helpful_count: Optional[float] = None
    author_name: Optional[str] = None

class ReviewOut(BaseModel):
    id: str
    target_id: str
    target_type: str
    rating: float
    comment: Optional[str]
    helpful_count: Optional[float]
    author_name: Optional[str]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None