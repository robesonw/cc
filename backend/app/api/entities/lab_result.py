from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models.lab_result import LabResultCreate, LabResultUpdate, LabResultOut
from app.repos.postgres_repo import PostgresRepo

router = APIRouter()

repo = PostgresRepo("lab_result", [{"name": "upload_date", "type": "string", "required": True, "nullable": False}, {"name": "file_url", "type": "string", "required": False, "nullable": False}, {"name": "biomarkers", "type": "object", "required": False, "nullable": False}, {"name": "notes", "type": "string", "required": False, "nullable": False}])

@router.get("", response_model=dict)
async def list_lab_result(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0), q: Optional[str] = Query(None)):
    result = await repo.list(limit=limit, offset=offset, q=q)
    return {"items": result["items"], "total": result["total"]}

@router.post("", response_model=LabResultOut, status_code=201)
async def create_lab_result(data: LabResultCreate):
    result = await repo.create(data.model_dump())
    return LabResultOut(**result)

@router.get("/{id}", response_model=LabResultOut)
async def get_lab_result(id: str):
    result = await repo.get(id)
    if not result:
        raise HTTPException(status_code=404, detail=f"LabResult with id {id} not found")
    return LabResultOut(**result)

@router.put("/{id}", response_model=LabResultOut)
async def replace_lab_result(id: str, data: LabResultCreate):
    try:
        result = await repo.replace(id, data.model_dump())
        return LabResultOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=LabResultOut)
async def patch_lab_result(id: str, data: LabResultUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    try:
        result = await repo.patch(id, update_data)
        return LabResultOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=204)
async def delete_lab_result(id: str):
    success = await repo.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail=f"LabResult with id {id} not found")
    return None