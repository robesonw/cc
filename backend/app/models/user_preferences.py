from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class UserPreferencesBase(BaseModel):
    age: Optional[float]
    gender: Optional[str]
    height: Optional[float]
    weight: Optional[float]
    health_goal: Optional[str]
    dietary_restrictions: Optional[str]
    foods_liked: Optional[str]
    foods_avoided: Optional[str]
    allergens: Optional[List[Any]]
    cuisine_preferences: Optional[List[Any]]
    cooking_time: Optional[str]
    skill_level: Optional[str]
    num_people: Optional[float]
    weekly_budget: Optional[float]

class UserPreferencesCreate(BaseModel):
    age: Optional[float] = None
    gender: Optional[str] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    health_goal: Optional[str] = None
    dietary_restrictions: Optional[str] = None
    foods_liked: Optional[str] = None
    foods_avoided: Optional[str] = None
    allergens: Optional[List[Any]] = None
    cuisine_preferences: Optional[List[Any]] = None
    cooking_time: Optional[str] = None
    skill_level: Optional[str] = None
    num_people: Optional[float] = None
    weekly_budget: Optional[float] = None

class UserPreferencesUpdate(BaseModel):
    age: Optional[float] = None
    gender: Optional[str] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    health_goal: Optional[str] = None
    dietary_restrictions: Optional[str] = None
    foods_liked: Optional[str] = None
    foods_avoided: Optional[str] = None
    allergens: Optional[List[Any]] = None
    cuisine_preferences: Optional[List[Any]] = None
    cooking_time: Optional[str] = None
    skill_level: Optional[str] = None
    num_people: Optional[float] = None
    weekly_budget: Optional[float] = None

class UserPreferencesOut(BaseModel):
    id: str
    age: Optional[float]
    gender: Optional[str]
    height: Optional[float]
    weight: Optional[float]
    health_goal: Optional[str]
    dietary_restrictions: Optional[str]
    foods_liked: Optional[str]
    foods_avoided: Optional[str]
    allergens: Optional[List[Any]]
    cuisine_preferences: Optional[List[Any]]
    cooking_time: Optional[str]
    skill_level: Optional[str]
    num_people: Optional[float]
    weekly_budget: Optional[float]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None