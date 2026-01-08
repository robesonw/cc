from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class UserInteractionBase(BaseModel):
    target_id: str
    target_type: str
    interaction_type: str

class UserInteractionCreate(BaseModel):
    target_id: str
    target_type: str
    interaction_type: str

class UserInteractionUpdate(BaseModel):
    target_id: Optional[str] = None
    target_type: Optional[str] = None
    interaction_type: Optional[str] = None

class UserInteractionOut(BaseModel):
    id: str
    target_id: str
    target_type: str
    interaction_type: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None