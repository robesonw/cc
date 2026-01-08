from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class ForumPostBase(BaseModel):
    title: str
    content: str
    category: str
    tags: Optional[List[Any]]
    likes_count: Optional[float]
    views_count: Optional[float]
    comments_count: Optional[float]
    is_pinned: Optional[bool]
    author_name: Optional[str]

class ForumPostCreate(BaseModel):
    title: str
    content: str
    category: str
    tags: Optional[List[Any]] = None
    likes_count: Optional[float] = None
    views_count: Optional[float] = None
    comments_count: Optional[float] = None
    is_pinned: Optional[bool] = None
    author_name: Optional[str] = None

class ForumPostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[List[Any]] = None
    likes_count: Optional[float] = None
    views_count: Optional[float] = None
    comments_count: Optional[float] = None
    is_pinned: Optional[bool] = None
    author_name: Optional[str] = None

class ForumPostOut(BaseModel):
    id: str
    title: str
    content: str
    category: str
    tags: Optional[List[Any]]
    likes_count: Optional[float]
    views_count: Optional[float]
    comments_count: Optional[float]
    is_pinned: Optional[bool]
    author_name: Optional[str]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None