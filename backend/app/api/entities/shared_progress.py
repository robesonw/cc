from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models.shared_progress import SharedProgressCreate, SharedProgressUpdate, SharedProgressOut
from app.repos.postgres_repo import PostgresRepo

router = APIRouter()

repo = PostgresRepo("shared_progress", [{"name": "title", "type": "string", "required": True, "nullable": False}, {"name": "description", "type": "string", "required": False, "nullable": False}, {"name": "progress_type", "type": "string", "required": True, "nullable": False}, {"name": "stats", "type": "object", "required": False, "nullable": False}, {"name": "date_range", "type": "object", "required": False, "nullable": False}, {"name": "likes_count", "type": "number", "required": False, "nullable": False}, {"name": "comments_count", "type": "number", "required": False, "nullable": False}, {"name": "author_name", "type": "string", "required": False, "nullable": False}])

@router.get("", response_model=dict)
async def list_shared_progress(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0), q: Optional[str] = Query(None)):
    result = await repo.list(limit=limit, offset=offset, q=q)
    return {"items": result["items"], "total": result["total"]}

@router.post("", response_model=SharedProgressOut, status_code=201)
async def create_shared_progress(data: SharedProgressCreate):
    result = await repo.create(data.model_dump())
    return SharedProgressOut(**result)

@router.get("/{id}", response_model=SharedProgressOut)
async def get_shared_progress(id: str):
    result = await repo.get(id)
    if not result:
        raise HTTPException(status_code=404, detail=f"SharedProgress with id {id} not found")
    return SharedProgressOut(**result)

@router.put("/{id}", response_model=SharedProgressOut)
async def replace_shared_progress(id: str, data: SharedProgressCreate):
    try:
        result = await repo.replace(id, data.model_dump())
        return SharedProgressOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=SharedProgressOut)
async def patch_shared_progress(id: str, data: SharedProgressUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    try:
        result = await repo.patch(id, update_data)
        return SharedProgressOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=204)
async def delete_shared_progress(id: str):
    success = await repo.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail=f"SharedProgress with id {id} not found")
    return None