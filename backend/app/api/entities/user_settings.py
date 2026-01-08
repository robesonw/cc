from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models.user_settings import UserSettingsCreate, UserSettingsUpdate, UserSettingsOut
from app.repos.postgres_repo import PostgresRepo

router = APIRouter()

repo = PostgresRepo("user_settings", [{"name": "email_notifications", "type": "boolean", "required": False, "nullable": False}, {"name": "recipe_approved_notifications", "type": "boolean", "required": False, "nullable": False}, {"name": "recipe_rejected_notifications", "type": "boolean", "required": False, "nullable": False}, {"name": "new_follower_notifications", "type": "boolean", "required": False, "nullable": False}, {"name": "comment_notifications", "type": "boolean", "required": False, "nullable": False}, {"name": "like_notifications", "type": "boolean", "required": False, "nullable": False}, {"name": "weekly_summary", "type": "boolean", "required": False, "nullable": False}])

@router.get("", response_model=dict)
async def list_user_settings(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0), q: Optional[str] = Query(None)):
    result = await repo.list(limit=limit, offset=offset, q=q)
    return {"items": result["items"], "total": result["total"]}

@router.post("", response_model=UserSettingsOut, status_code=201)
async def create_user_settings(data: UserSettingsCreate):
    result = await repo.create(data.model_dump())
    return UserSettingsOut(**result)

@router.get("/{id}", response_model=UserSettingsOut)
async def get_user_settings(id: str):
    result = await repo.get(id)
    if not result:
        raise HTTPException(status_code=404, detail=f"UserSettings with id {id} not found")
    return UserSettingsOut(**result)

@router.put("/{id}", response_model=UserSettingsOut)
async def replace_user_settings(id: str, data: UserSettingsCreate):
    try:
        result = await repo.replace(id, data.model_dump())
        return UserSettingsOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=UserSettingsOut)
async def patch_user_settings(id: str, data: UserSettingsUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    try:
        result = await repo.patch(id, update_data)
        return UserSettingsOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=204)
async def delete_user_settings(id: str):
    success = await repo.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail=f"UserSettings with id {id} not found")
    return None