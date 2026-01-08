from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models.nutrition_goal import NutritionGoalCreate, NutritionGoalUpdate, NutritionGoalOut
from app.repos.postgres_repo import PostgresRepo

router = APIRouter()

repo = PostgresRepo("nutrition_goal", [{"name": "goal_type", "type": "string", "required": True, "nullable": False}, {"name": "target_calories", "type": "number", "required": False, "nullable": False}, {"name": "target_protein", "type": "number", "required": False, "nullable": False}, {"name": "target_carbs", "type": "number", "required": False, "nullable": False}, {"name": "target_fat", "type": "number", "required": False, "nullable": False}, {"name": "target_micronutrients", "type": "object", "required": False, "nullable": False}, {"name": "is_active", "type": "boolean", "required": False, "nullable": False}])

@router.get("", response_model=dict)
async def list_nutrition_goal(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0), q: Optional[str] = Query(None)):
    result = await repo.list(limit=limit, offset=offset, q=q)
    return {"items": result["items"], "total": result["total"]}

@router.post("", response_model=NutritionGoalOut, status_code=201)
async def create_nutrition_goal(data: NutritionGoalCreate):
    result = await repo.create(data.model_dump())
    return NutritionGoalOut(**result)

@router.get("/{id}", response_model=NutritionGoalOut)
async def get_nutrition_goal(id: str):
    result = await repo.get(id)
    if not result:
        raise HTTPException(status_code=404, detail=f"NutritionGoal with id {id} not found")
    return NutritionGoalOut(**result)

@router.put("/{id}", response_model=NutritionGoalOut)
async def replace_nutrition_goal(id: str, data: NutritionGoalCreate):
    try:
        result = await repo.replace(id, data.model_dump())
        return NutritionGoalOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=NutritionGoalOut)
async def patch_nutrition_goal(id: str, data: NutritionGoalUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    try:
        result = await repo.patch(id, update_data)
        return NutritionGoalOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=204)
async def delete_nutrition_goal(id: str):
    success = await repo.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail=f"NutritionGoal with id {id} not found")
    return None