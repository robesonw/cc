from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class MealPlanBase(BaseModel):
    name: str
    diet_type: str
    cultural_style: Optional[str]
    life_stage: Optional[str]
    days: List[Any]
    preferences: Optional[Dict[str, Any]]
    macros: Optional[Dict[str, Any]]
    estimated_cost: Optional[float]
    grocery_list: Optional[Dict[str, Any]]
    current_total_cost: Optional[float]
    hero_image_url: Optional[str]

class MealPlanCreate(BaseModel):
    name: str
    diet_type: str
    cultural_style: Optional[str] = None
    life_stage: Optional[str] = None
    days: List[Any]
    preferences: Optional[Dict[str, Any]] = None
    macros: Optional[Dict[str, Any]] = None
    estimated_cost: Optional[float] = None
    grocery_list: Optional[Dict[str, Any]] = None
    current_total_cost: Optional[float] = None
    hero_image_url: Optional[str] = None

class MealPlanUpdate(BaseModel):
    name: Optional[str] = None
    diet_type: Optional[str] = None
    cultural_style: Optional[str] = None
    life_stage: Optional[str] = None
    days: Optional[List[Any]] = None
    preferences: Optional[Dict[str, Any]] = None
    macros: Optional[Dict[str, Any]] = None
    estimated_cost: Optional[float] = None
    grocery_list: Optional[Dict[str, Any]] = None
    current_total_cost: Optional[float] = None
    hero_image_url: Optional[str] = None

class MealPlanOut(BaseModel):
    id: str
    name: str
    diet_type: str
    cultural_style: Optional[str]
    life_stage: Optional[str]
    days: List[Any]
    preferences: Optional[Dict[str, Any]]
    macros: Optional[Dict[str, Any]]
    estimated_cost: Optional[float]
    grocery_list: Optional[Dict[str, Any]]
    current_total_cost: Optional[float]
    hero_image_url: Optional[str]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None