from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class NotificationBase(BaseModel):
    recipient_email: str
    type: str
    title: str
    message: str
    link: Optional[str]
    is_read: Optional[bool]
    actor_name: Optional[str]

class NotificationCreate(BaseModel):
    recipient_email: str
    type: str
    title: str
    message: str
    link: Optional[str] = None
    is_read: Optional[bool] = None
    actor_name: Optional[str] = None

class NotificationUpdate(BaseModel):
    recipient_email: Optional[str] = None
    type: Optional[str] = None
    title: Optional[str] = None
    message: Optional[str] = None
    link: Optional[str] = None
    is_read: Optional[bool] = None
    actor_name: Optional[str] = None

class NotificationOut(BaseModel):
    id: str
    recipient_email: str
    type: str
    title: str
    message: str
    link: Optional[str]
    is_read: Optional[bool]
    actor_name: Optional[str]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None