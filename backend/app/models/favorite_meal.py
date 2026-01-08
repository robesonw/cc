from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class FavoriteMealBase(BaseModel):
    name: str
    meal_type: str
    calories: Optional[str]
    protein: Optional[float]
    carbs: Optional[float]
    fat: Optional[float]
    nutrients: Optional[str]
    prepTip: Optional[str]
    prepTime: Optional[str]
    prepSteps: Optional[List[Any]]
    difficulty: Optional[str]
    equipment: Optional[List[Any]]
    healthBenefit: Optional[str]
    imageUrl: Optional[str]
    cuisine: Optional[str]
    cooking_time: Optional[str]
    tags: Optional[List[Any]]
    source_type: Optional[str]
    source_meal_plan_id: Optional[str]
    source_meal_plan_name: Optional[str]
    source_recipe_id: Optional[str]
    ingredients: Optional[List[Any]]
    grocery_list: Optional[Dict[str, Any]]
    estimated_cost: Optional[float]

class FavoriteMealCreate(BaseModel):
    name: str
    meal_type: str
    calories: Optional[str] = None
    protein: Optional[float] = None
    carbs: Optional[float] = None
    fat: Optional[float] = None
    nutrients: Optional[str] = None
    prepTip: Optional[str] = None
    prepTime: Optional[str] = None
    prepSteps: Optional[List[Any]] = None
    difficulty: Optional[str] = None
    equipment: Optional[List[Any]] = None
    healthBenefit: Optional[str] = None
    imageUrl: Optional[str] = None
    cuisine: Optional[str] = None
    cooking_time: Optional[str] = None
    tags: Optional[List[Any]] = None
    source_type: Optional[str] = None
    source_meal_plan_id: Optional[str] = None
    source_meal_plan_name: Optional[str] = None
    source_recipe_id: Optional[str] = None
    ingredients: Optional[List[Any]] = None
    grocery_list: Optional[Dict[str, Any]] = None
    estimated_cost: Optional[float] = None

class FavoriteMealUpdate(BaseModel):
    name: Optional[str] = None
    meal_type: Optional[str] = None
    calories: Optional[str] = None
    protein: Optional[float] = None
    carbs: Optional[float] = None
    fat: Optional[float] = None
    nutrients: Optional[str] = None
    prepTip: Optional[str] = None
    prepTime: Optional[str] = None
    prepSteps: Optional[List[Any]] = None
    difficulty: Optional[str] = None
    equipment: Optional[List[Any]] = None
    healthBenefit: Optional[str] = None
    imageUrl: Optional[str] = None
    cuisine: Optional[str] = None
    cooking_time: Optional[str] = None
    tags: Optional[List[Any]] = None
    source_type: Optional[str] = None
    source_meal_plan_id: Optional[str] = None
    source_meal_plan_name: Optional[str] = None
    source_recipe_id: Optional[str] = None
    ingredients: Optional[List[Any]] = None
    grocery_list: Optional[Dict[str, Any]] = None
    estimated_cost: Optional[float] = None

class FavoriteMealOut(BaseModel):
    id: str
    name: str
    meal_type: str
    calories: Optional[str]
    protein: Optional[float]
    carbs: Optional[float]
    fat: Optional[float]
    nutrients: Optional[str]
    prepTip: Optional[str]
    prepTime: Optional[str]
    prepSteps: Optional[List[Any]]
    difficulty: Optional[str]
    equipment: Optional[List[Any]]
    healthBenefit: Optional[str]
    imageUrl: Optional[str]
    cuisine: Optional[str]
    cooking_time: Optional[str]
    tags: Optional[List[Any]]
    source_type: Optional[str]
    source_meal_plan_id: Optional[str]
    source_meal_plan_name: Optional[str]
    source_recipe_id: Optional[str]
    ingredients: Optional[List[Any]]
    grocery_list: Optional[Dict[str, Any]]
    estimated_cost: Optional[float]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None