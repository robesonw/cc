from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class SharedRecipeBase(BaseModel):
    name: str
    meal_type: str
    description: Optional[str]
    meal_data: Dict[str, Any]
    calories: Optional[str]
    protein: Optional[float]
    carbs: Optional[float]
    fat: Optional[float]
    image_url: Optional[str]
    tags: Optional[List[Any]]
    views_count: Optional[float]
    likes_count: Optional[float]
    saves_count: Optional[float]
    average_rating: Optional[float]
    author_name: Optional[str]
    status: Optional[str]
    moderation_notes: Optional[str]
    cuisine: Optional[str]
    difficulty: Optional[str]
    prep_time: Optional[str]
    cooking_time: Optional[str]
    servings: Optional[float]
    ingredients: Optional[List[Any]]
    prep_steps: Optional[List[Any]]

class SharedRecipeCreate(BaseModel):
    name: str
    meal_type: str
    description: Optional[str] = None
    meal_data: Dict[str, Any]
    calories: Optional[str] = None
    protein: Optional[float] = None
    carbs: Optional[float] = None
    fat: Optional[float] = None
    image_url: Optional[str] = None
    tags: Optional[List[Any]] = None
    views_count: Optional[float] = None
    likes_count: Optional[float] = None
    saves_count: Optional[float] = None
    average_rating: Optional[float] = None
    author_name: Optional[str] = None
    status: Optional[str] = None
    moderation_notes: Optional[str] = None
    cuisine: Optional[str] = None
    difficulty: Optional[str] = None
    prep_time: Optional[str] = None
    cooking_time: Optional[str] = None
    servings: Optional[float] = None
    ingredients: Optional[List[Any]] = None
    prep_steps: Optional[List[Any]] = None

class SharedRecipeUpdate(BaseModel):
    name: Optional[str] = None
    meal_type: Optional[str] = None
    description: Optional[str] = None
    meal_data: Optional[Dict[str, Any]] = None
    calories: Optional[str] = None
    protein: Optional[float] = None
    carbs: Optional[float] = None
    fat: Optional[float] = None
    image_url: Optional[str] = None
    tags: Optional[List[Any]] = None
    views_count: Optional[float] = None
    likes_count: Optional[float] = None
    saves_count: Optional[float] = None
    average_rating: Optional[float] = None
    author_name: Optional[str] = None
    status: Optional[str] = None
    moderation_notes: Optional[str] = None
    cuisine: Optional[str] = None
    difficulty: Optional[str] = None
    prep_time: Optional[str] = None
    cooking_time: Optional[str] = None
    servings: Optional[float] = None
    ingredients: Optional[List[Any]] = None
    prep_steps: Optional[List[Any]] = None

class SharedRecipeOut(BaseModel):
    id: str
    name: str
    meal_type: str
    description: Optional[str]
    meal_data: Dict[str, Any]
    calories: Optional[str]
    protein: Optional[float]
    carbs: Optional[float]
    fat: Optional[float]
    image_url: Optional[str]
    tags: Optional[List[Any]]
    views_count: Optional[float]
    likes_count: Optional[float]
    saves_count: Optional[float]
    average_rating: Optional[float]
    author_name: Optional[str]
    status: Optional[str]
    moderation_notes: Optional[str]
    cuisine: Optional[str]
    difficulty: Optional[str]
    prep_time: Optional[str]
    cooking_time: Optional[str]
    servings: Optional[float]
    ingredients: Optional[List[Any]]
    prep_steps: Optional[List[Any]]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None