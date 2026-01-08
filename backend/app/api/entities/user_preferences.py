from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models.user_preferences import UserPreferencesCreate, UserPreferencesUpdate, UserPreferencesOut
from app.repos.postgres_repo import PostgresRepo

router = APIRouter()

repo = PostgresRepo("user_preferences", [{"name": "age", "type": "number", "required": False, "nullable": False}, {"name": "gender", "type": "string", "required": False, "nullable": False}, {"name": "height", "type": "number", "required": False, "nullable": False}, {"name": "weight", "type": "number", "required": False, "nullable": False}, {"name": "health_goal", "type": "string", "required": False, "nullable": False}, {"name": "dietary_restrictions", "type": "string", "required": False, "nullable": False}, {"name": "foods_liked", "type": "string", "required": False, "nullable": False}, {"name": "foods_avoided", "type": "string", "required": False, "nullable": False}, {"name": "allergens", "type": "array", "required": False, "nullable": False}, {"name": "cuisine_preferences", "type": "array", "required": False, "nullable": False}, {"name": "cooking_time", "type": "string", "required": False, "nullable": False}, {"name": "skill_level", "type": "string", "required": False, "nullable": False}, {"name": "num_people", "type": "number", "required": False, "nullable": False}, {"name": "weekly_budget", "type": "number", "required": False, "nullable": False}])

@router.get("", response_model=dict)
async def list_user_preferences(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0), q: Optional[str] = Query(None)):
    result = await repo.list(limit=limit, offset=offset, q=q)
    return {"items": result["items"], "total": result["total"]}

@router.post("", response_model=UserPreferencesOut, status_code=201)
async def create_user_preferences(data: UserPreferencesCreate):
    result = await repo.create(data.model_dump())
    return UserPreferencesOut(**result)

@router.get("/{id}", response_model=UserPreferencesOut)
async def get_user_preferences(id: str):
    result = await repo.get(id)
    if not result:
        raise HTTPException(status_code=404, detail=f"UserPreferences with id {id} not found")
    return UserPreferencesOut(**result)

@router.put("/{id}", response_model=UserPreferencesOut)
async def replace_user_preferences(id: str, data: UserPreferencesCreate):
    try:
        result = await repo.replace(id, data.model_dump())
        return UserPreferencesOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=UserPreferencesOut)
async def patch_user_preferences(id: str, data: UserPreferencesUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    try:
        result = await repo.patch(id, update_data)
        return UserPreferencesOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=204)
async def delete_user_preferences(id: str):
    success = await repo.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail=f"UserPreferences with id {id} not found")
    return None