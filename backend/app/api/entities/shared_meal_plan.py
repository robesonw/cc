from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models.shared_meal_plan import SharedMealPlanCreate, SharedMealPlanUpdate, SharedMealPlanOut
from app.repos.postgres_repo import PostgresRepo

router = APIRouter()

repo = PostgresRepo("shared_meal_plan", [{"name": "original_plan_id", "type": "string", "required": False, "nullable": False}, {"name": "title", "type": "string", "required": True, "nullable": False}, {"name": "description", "type": "string", "required": False, "nullable": False}, {"name": "plan_data", "type": "object", "required": True, "nullable": False}, {"name": "diet_type", "type": "string", "required": False, "nullable": False}, {"name": "cultural_style", "type": "string", "required": False, "nullable": False}, {"name": "tags", "type": "array", "required": False, "nullable": False}, {"name": "views_count", "type": "number", "required": False, "nullable": False}, {"name": "likes_count", "type": "number", "required": False, "nullable": False}, {"name": "saves_count", "type": "number", "required": False, "nullable": False}, {"name": "average_rating", "type": "number", "required": False, "nullable": False}, {"name": "author_name", "type": "string", "required": False, "nullable": False}])

@router.get("", response_model=dict)
async def list_shared_meal_plan(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0), q: Optional[str] = Query(None)):
    result = await repo.list(limit=limit, offset=offset, q=q)
    return {"items": result["items"], "total": result["total"]}

@router.post("", response_model=SharedMealPlanOut, status_code=201)
async def create_shared_meal_plan(data: SharedMealPlanCreate):
    result = await repo.create(data.model_dump())
    return SharedMealPlanOut(**result)

@router.get("/{id}", response_model=SharedMealPlanOut)
async def get_shared_meal_plan(id: str):
    result = await repo.get(id)
    if not result:
        raise HTTPException(status_code=404, detail=f"SharedMealPlan with id {id} not found")
    return SharedMealPlanOut(**result)

@router.put("/{id}", response_model=SharedMealPlanOut)
async def replace_shared_meal_plan(id: str, data: SharedMealPlanCreate):
    try:
        result = await repo.replace(id, data.model_dump())
        return SharedMealPlanOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=SharedMealPlanOut)
async def patch_shared_meal_plan(id: str, data: SharedMealPlanUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    try:
        result = await repo.patch(id, update_data)
        return SharedMealPlanOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=204)
async def delete_shared_meal_plan(id: str):
    success = await repo.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail=f"SharedMealPlan with id {id} not found")
    return None