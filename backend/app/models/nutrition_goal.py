from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class NutritionGoalBase(BaseModel):
    goal_type: str
    target_calories: Optional[float]
    target_protein: Optional[float]
    target_carbs: Optional[float]
    target_fat: Optional[float]
    target_micronutrients: Optional[Dict[str, Any]]
    is_active: Optional[bool]

class NutritionGoalCreate(BaseModel):
    goal_type: str
    target_calories: Optional[float] = None
    target_protein: Optional[float] = None
    target_carbs: Optional[float] = None
    target_fat: Optional[float] = None
    target_micronutrients: Optional[Dict[str, Any]] = None
    is_active: Optional[bool] = None

class NutritionGoalUpdate(BaseModel):
    goal_type: Optional[str] = None
    target_calories: Optional[float] = None
    target_protein: Optional[float] = None
    target_carbs: Optional[float] = None
    target_fat: Optional[float] = None
    target_micronutrients: Optional[Dict[str, Any]] = None
    is_active: Optional[bool] = None

class NutritionGoalOut(BaseModel):
    id: str
    goal_type: str
    target_calories: Optional[float]
    target_protein: Optional[float]
    target_carbs: Optional[float]
    target_fat: Optional[float]
    target_micronutrients: Optional[Dict[str, Any]]
    is_active: Optional[bool]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None