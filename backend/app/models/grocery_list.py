from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class GroceryListBase(BaseModel):
    name: str
    items: Optional[Dict[str, Any]]
    total_cost: Optional[float]
    notes: Optional[str]

class GroceryListCreate(BaseModel):
    name: str
    items: Optional[Dict[str, Any]] = None
    total_cost: Optional[float] = None
    notes: Optional[str] = None

class GroceryListUpdate(BaseModel):
    name: Optional[str] = None
    items: Optional[Dict[str, Any]] = None
    total_cost: Optional[float] = None
    notes: Optional[str] = None

class GroceryListOut(BaseModel):
    id: str
    name: str
    items: Optional[Dict[str, Any]]
    total_cost: Optional[float]
    notes: Optional[str]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None