from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class FeedbackBase(BaseModel):
    user_name: Optional[str]
    user_email: Optional[str]
    page: Optional[str]
    rating: Optional[float]
    feedback_type: str
    message: str
    status: Optional[str]

class FeedbackCreate(BaseModel):
    user_name: Optional[str] = None
    user_email: Optional[str] = None
    page: Optional[str] = None
    rating: Optional[float] = None
    feedback_type: str
    message: str
    status: Optional[str] = None

class FeedbackUpdate(BaseModel):
    user_name: Optional[str] = None
    user_email: Optional[str] = None
    page: Optional[str] = None
    rating: Optional[float] = None
    feedback_type: Optional[str] = None
    message: Optional[str] = None
    status: Optional[str] = None

class FeedbackOut(BaseModel):
    id: str
    user_name: Optional[str]
    user_email: Optional[str]
    page: Optional[str]
    rating: Optional[float]
    feedback_type: str
    message: str
    status: Optional[str]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None