from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class NutritionLogBase(BaseModel):
    recipe_name: str
    meal_type: Optional[str]
    log_date: str
    calories: float
    protein: Optional[float]
    carbs: Optional[float]
    fat: Optional[float]
    micronutrients: Optional[Dict[str, Any]]
    servings: Optional[float]
    food_source: Optional[str]
    food_id: Optional[str]

class NutritionLogCreate(BaseModel):
    recipe_name: str
    meal_type: Optional[str] = None
    log_date: str
    calories: float
    protein: Optional[float] = None
    carbs: Optional[float] = None
    fat: Optional[float] = None
    micronutrients: Optional[Dict[str, Any]] = None
    servings: Optional[float] = None
    food_source: Optional[str] = None
    food_id: Optional[str] = None

class NutritionLogUpdate(BaseModel):
    recipe_name: Optional[str] = None
    meal_type: Optional[str] = None
    log_date: Optional[str] = None
    calories: Optional[float] = None
    protein: Optional[float] = None
    carbs: Optional[float] = None
    fat: Optional[float] = None
    micronutrients: Optional[Dict[str, Any]] = None
    servings: Optional[float] = None
    food_source: Optional[str] = None
    food_id: Optional[str] = None

class NutritionLogOut(BaseModel):
    id: str
    recipe_name: str
    meal_type: Optional[str]
    log_date: str
    calories: float
    protein: Optional[float]
    carbs: Optional[float]
    fat: Optional[float]
    micronutrients: Optional[Dict[str, Any]]
    servings: Optional[float]
    food_source: Optional[str]
    food_id: Optional[str]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None