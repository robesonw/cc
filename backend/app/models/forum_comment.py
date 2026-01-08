from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class ForumCommentBase(BaseModel):
    post_id: str
    content: str
    likes_count: Optional[float]
    author_name: Optional[str]
    reactions: Optional[Dict[str, Any]]

class ForumCommentCreate(BaseModel):
    post_id: str
    content: str
    likes_count: Optional[float] = None
    author_name: Optional[str] = None
    reactions: Optional[Dict[str, Any]] = None

class ForumCommentUpdate(BaseModel):
    post_id: Optional[str] = None
    content: Optional[str] = None
    likes_count: Optional[float] = None
    author_name: Optional[str] = None
    reactions: Optional[Dict[str, Any]] = None

class ForumCommentOut(BaseModel):
    id: str
    post_id: str
    content: str
    likes_count: Optional[float]
    author_name: Optional[str]
    reactions: Optional[Dict[str, Any]]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None