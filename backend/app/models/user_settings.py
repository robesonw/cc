from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class UserSettingsBase(BaseModel):
    email_notifications: Optional[bool]
    recipe_approved_notifications: Optional[bool]
    recipe_rejected_notifications: Optional[bool]
    new_follower_notifications: Optional[bool]
    comment_notifications: Optional[bool]
    like_notifications: Optional[bool]
    weekly_summary: Optional[bool]

class UserSettingsCreate(BaseModel):
    email_notifications: Optional[bool] = None
    recipe_approved_notifications: Optional[bool] = None
    recipe_rejected_notifications: Optional[bool] = None
    new_follower_notifications: Optional[bool] = None
    comment_notifications: Optional[bool] = None
    like_notifications: Optional[bool] = None
    weekly_summary: Optional[bool] = None

class UserSettingsUpdate(BaseModel):
    email_notifications: Optional[bool] = None
    recipe_approved_notifications: Optional[bool] = None
    recipe_rejected_notifications: Optional[bool] = None
    new_follower_notifications: Optional[bool] = None
    comment_notifications: Optional[bool] = None
    like_notifications: Optional[bool] = None
    weekly_summary: Optional[bool] = None

class UserSettingsOut(BaseModel):
    id: str
    email_notifications: Optional[bool]
    recipe_approved_notifications: Optional[bool]
    recipe_rejected_notifications: Optional[bool]
    new_follower_notifications: Optional[bool]
    comment_notifications: Optional[bool]
    like_notifications: Optional[bool]
    weekly_summary: Optional[bool]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None