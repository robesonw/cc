from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class UserFollowBase(BaseModel):
    following_user_email: str
    following_user_name: Optional[str]

class UserFollowCreate(BaseModel):
    following_user_email: str
    following_user_name: Optional[str] = None

class UserFollowUpdate(BaseModel):
    following_user_email: Optional[str] = None
    following_user_name: Optional[str] = None

class UserFollowOut(BaseModel):
    id: str
    following_user_email: str
    following_user_name: Optional[str]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None