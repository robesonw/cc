from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class SharedProgressBase(BaseModel):
    title: str
    description: Optional[str]
    progress_type: str
    stats: Optional[Dict[str, Any]]
    date_range: Optional[Dict[str, Any]]
    likes_count: Optional[float]
    comments_count: Optional[float]
    author_name: Optional[str]

class SharedProgressCreate(BaseModel):
    title: str
    description: Optional[str] = None
    progress_type: str
    stats: Optional[Dict[str, Any]] = None
    date_range: Optional[Dict[str, Any]] = None
    likes_count: Optional[float] = None
    comments_count: Optional[float] = None
    author_name: Optional[str] = None

class SharedProgressUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    progress_type: Optional[str] = None
    stats: Optional[Dict[str, Any]] = None
    date_range: Optional[Dict[str, Any]] = None
    likes_count: Optional[float] = None
    comments_count: Optional[float] = None
    author_name: Optional[str] = None

class SharedProgressOut(BaseModel):
    id: str
    title: str
    description: Optional[str]
    progress_type: str
    stats: Optional[Dict[str, Any]]
    date_range: Optional[Dict[str, Any]]
    likes_count: Optional[float]
    comments_count: Optional[float]
    author_name: Optional[str]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None