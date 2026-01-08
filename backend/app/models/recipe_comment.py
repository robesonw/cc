from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class RecipeCommentBase(BaseModel):
    recipe_id: str
    comment: str
    author_name: Optional[str]

class RecipeCommentCreate(BaseModel):
    recipe_id: str
    comment: str
    author_name: Optional[str] = None

class RecipeCommentUpdate(BaseModel):
    recipe_id: Optional[str] = None
    comment: Optional[str] = None
    author_name: Optional[str] = None

class RecipeCommentOut(BaseModel):
    id: str
    recipe_id: str
    comment: str
    author_name: Optional[str]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None