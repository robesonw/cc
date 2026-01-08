from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime, date


class LabResultBase(BaseModel):
    upload_date: str
    file_url: Optional[str]
    biomarkers: Optional[Dict[str, Any]]
    notes: Optional[str]

class LabResultCreate(BaseModel):
    upload_date: str
    file_url: Optional[str] = None
    biomarkers: Optional[Dict[str, Any]] = None
    notes: Optional[str] = None

class LabResultUpdate(BaseModel):
    upload_date: Optional[str] = None
    file_url: Optional[str] = None
    biomarkers: Optional[Dict[str, Any]] = None
    notes: Optional[str] = None

class LabResultOut(BaseModel):
    id: str
    upload_date: str
    file_url: Optional[str]
    biomarkers: Optional[Dict[str, Any]]
    notes: Optional[str]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None