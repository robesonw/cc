from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models.review import ReviewCreate, ReviewUpdate, ReviewOut
from app.repos.postgres_repo import PostgresRepo

router = APIRouter()

repo = PostgresRepo("review", [{"name": "target_id", "type": "string", "required": True, "nullable": False}, {"name": "target_type", "type": "string", "required": True, "nullable": False}, {"name": "rating", "type": "number", "required": True, "nullable": False}, {"name": "comment", "type": "string", "required": False, "nullable": False}, {"name": "helpful_count", "type": "number", "required": False, "nullable": False}, {"name": "author_name", "type": "string", "required": False, "nullable": False}])

@router.get("", response_model=dict)
async def list_review(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0), q: Optional[str] = Query(None)):
    result = await repo.list(limit=limit, offset=offset, q=q)
    return {"items": result["items"], "total": result["total"]}

@router.post("", response_model=ReviewOut, status_code=201)
async def create_review(data: ReviewCreate):
    result = await repo.create(data.model_dump())
    return ReviewOut(**result)

@router.get("/{id}", response_model=ReviewOut)
async def get_review(id: str):
    result = await repo.get(id)
    if not result:
        raise HTTPException(status_code=404, detail=f"Review with id {id} not found")
    return ReviewOut(**result)

@router.put("/{id}", response_model=ReviewOut)
async def replace_review(id: str, data: ReviewCreate):
    try:
        result = await repo.replace(id, data.model_dump())
        return ReviewOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=ReviewOut)
async def patch_review(id: str, data: ReviewUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    try:
        result = await repo.patch(id, update_data)
        return ReviewOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=204)
async def delete_review(id: str):
    success = await repo.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Review with id {id} not found")
    return None