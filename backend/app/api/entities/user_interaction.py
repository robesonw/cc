from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models.user_interaction import UserInteractionCreate, UserInteractionUpdate, UserInteractionOut
from app.repos.postgres_repo import PostgresRepo

router = APIRouter()

repo = PostgresRepo("user_interaction", [{"name": "target_id", "type": "string", "required": True, "nullable": False}, {"name": "target_type", "type": "string", "required": True, "nullable": False}, {"name": "interaction_type", "type": "string", "required": True, "nullable": False}])

@router.get("", response_model=dict)
async def list_user_interaction(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0), q: Optional[str] = Query(None)):
    result = await repo.list(limit=limit, offset=offset, q=q)
    return {"items": result["items"], "total": result["total"]}

@router.post("", response_model=UserInteractionOut, status_code=201)
async def create_user_interaction(data: UserInteractionCreate):
    result = await repo.create(data.model_dump())
    return UserInteractionOut(**result)

@router.get("/{id}", response_model=UserInteractionOut)
async def get_user_interaction(id: str):
    result = await repo.get(id)
    if not result:
        raise HTTPException(status_code=404, detail=f"UserInteraction with id {id} not found")
    return UserInteractionOut(**result)

@router.put("/{id}", response_model=UserInteractionOut)
async def replace_user_interaction(id: str, data: UserInteractionCreate):
    try:
        result = await repo.replace(id, data.model_dump())
        return UserInteractionOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=UserInteractionOut)
async def patch_user_interaction(id: str, data: UserInteractionUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    try:
        result = await repo.patch(id, update_data)
        return UserInteractionOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=204)
async def delete_user_interaction(id: str):
    success = await repo.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail=f"UserInteraction with id {id} not found")
    return None