from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models.meal_plan import MealPlanCreate, MealPlanUpdate, MealPlanOut
from app.repos.postgres_repo import PostgresRepo

router = APIRouter()

repo = PostgresRepo("meal_plan", [{"name": "name", "type": "string", "required": True, "nullable": False}, {"name": "diet_type", "type": "string", "required": True, "nullable": False}, {"name": "cultural_style", "type": "string", "required": False, "nullable": False}, {"name": "life_stage", "type": "string", "required": False, "nullable": False}, {"name": "days", "type": "array", "required": True, "nullable": False}, {"name": "preferences", "type": "object", "required": False, "nullable": False}, {"name": "macros", "type": "object", "required": False, "nullable": False}, {"name": "estimated_cost", "type": "number", "required": False, "nullable": False}, {"name": "grocery_list", "type": "object", "required": False, "nullable": False}, {"name": "current_total_cost", "type": "number", "required": False, "nullable": False}, {"name": "hero_image_url", "type": "string", "required": False, "nullable": False}])

@router.get("", response_model=dict)
async def list_meal_plan(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0), q: Optional[str] = Query(None)):
    result = await repo.list(limit=limit, offset=offset, q=q)
    return {"items": result["items"], "total": result["total"]}

@router.post("", response_model=MealPlanOut, status_code=201)
async def create_meal_plan(data: MealPlanCreate):
    result = await repo.create(data.model_dump())
    return MealPlanOut(**result)

@router.get("/{id}", response_model=MealPlanOut)
async def get_meal_plan(id: str):
    result = await repo.get(id)
    if not result:
        raise HTTPException(status_code=404, detail=f"MealPlan with id {id} not found")
    return MealPlanOut(**result)

@router.put("/{id}", response_model=MealPlanOut)
async def replace_meal_plan(id: str, data: MealPlanCreate):
    try:
        result = await repo.replace(id, data.model_dump())
        return MealPlanOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=MealPlanOut)
async def patch_meal_plan(id: str, data: MealPlanUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    try:
        result = await repo.patch(id, update_data)
        return MealPlanOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=204)
async def delete_meal_plan(id: str):
    success = await repo.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail=f"MealPlan with id {id} not found")
    return None