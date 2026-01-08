from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class ProgressCommentBase(BaseModel):
    progress_id: str
    comment: str
    author_name: Optional[str]

class ProgressCommentCreate(BaseModel):
    progress_id: str
    comment: str
    author_name: Optional[str] = None

class ProgressCommentUpdate(BaseModel):
    progress_id: Optional[str] = None
    comment: Optional[str] = None
    author_name: Optional[str] = None

class ProgressCommentOut(BaseModel):
    id: str
    progress_id: str
    comment: str
    author_name: Optional[str]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None