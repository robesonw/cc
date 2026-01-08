from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class SharedMealPlanBase(BaseModel):
    original_plan_id: Optional[str]
    title: str
    description: Optional[str]
    plan_data: Dict[str, Any]
    diet_type: Optional[str]
    cultural_style: Optional[str]
    tags: Optional[List[Any]]
    views_count: Optional[float]
    likes_count: Optional[float]
    saves_count: Optional[float]
    average_rating: Optional[float]
    author_name: Optional[str]

class SharedMealPlanCreate(BaseModel):
    original_plan_id: Optional[str] = None
    title: str
    description: Optional[str] = None
    plan_data: Dict[str, Any]
    diet_type: Optional[str] = None
    cultural_style: Optional[str] = None
    tags: Optional[List[Any]] = None
    views_count: Optional[float] = None
    likes_count: Optional[float] = None
    saves_count: Optional[float] = None
    average_rating: Optional[float] = None
    author_name: Optional[str] = None

class SharedMealPlanUpdate(BaseModel):
    original_plan_id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    plan_data: Optional[Dict[str, Any]] = None
    diet_type: Optional[str] = None
    cultural_style: Optional[str] = None
    tags: Optional[List[Any]] = None
    views_count: Optional[float] = None
    likes_count: Optional[float] = None
    saves_count: Optional[float] = None
    average_rating: Optional[float] = None
    author_name: Optional[str] = None

class SharedMealPlanOut(BaseModel):
    id: str
    original_plan_id: Optional[str]
    title: str
    description: Optional[str]
    plan_data: Dict[str, Any]
    diet_type: Optional[str]
    cultural_style: Optional[str]
    tags: Optional[List[Any]]
    views_count: Optional[float]
    likes_count: Optional[float]
    saves_count: Optional[float]
    average_rating: Optional[float]
    author_name: Optional[str]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None