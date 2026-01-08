from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models.feedback import FeedbackCreate, FeedbackUpdate, FeedbackOut
from app.repos.postgres_repo import PostgresRepo

router = APIRouter()

repo = PostgresRepo("feedback", [{"name": "user_name", "type": "string", "required": False, "nullable": False}, {"name": "user_email", "type": "string", "required": False, "nullable": False}, {"name": "page", "type": "string", "required": False, "nullable": False}, {"name": "rating", "type": "number", "required": False, "nullable": False}, {"name": "feedback_type", "type": "string", "required": True, "nullable": False}, {"name": "message", "type": "string", "required": True, "nullable": False}, {"name": "status", "type": "string", "required": False, "nullable": False}])

@router.get("", response_model=dict)
async def list_feedback(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0), q: Optional[str] = Query(None)):
    result = await repo.list(limit=limit, offset=offset, q=q)
    return {"items": result["items"], "total": result["total"]}

@router.post("", response_model=FeedbackOut, status_code=201)
async def create_feedback(data: FeedbackCreate):
    result = await repo.create(data.model_dump())
    return FeedbackOut(**result)

@router.get("/{id}", response_model=FeedbackOut)
async def get_feedback(id: str):
    result = await repo.get(id)
    if not result:
        raise HTTPException(status_code=404, detail=f"Feedback with id {id} not found")
    return FeedbackOut(**result)

@router.put("/{id}", response_model=FeedbackOut)
async def replace_feedback(id: str, data: FeedbackCreate):
    try:
        result = await repo.replace(id, data.model_dump())
        return FeedbackOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=FeedbackOut)
async def patch_feedback(id: str, data: FeedbackUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    try:
        result = await repo.patch(id, update_data)
        return FeedbackOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=204)
async def delete_feedback(id: str):
    success = await repo.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Feedback with id {id} not found")
    return None