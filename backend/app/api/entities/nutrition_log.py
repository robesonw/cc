from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models.nutrition_log import NutritionLogCreate, NutritionLogUpdate, NutritionLogOut
from app.repos.postgres_repo import PostgresRepo

router = APIRouter()

repo = PostgresRepo("nutrition_log", [{"name": "recipe_name", "type": "string", "required": True, "nullable": False}, {"name": "meal_type", "type": "string", "required": False, "nullable": False}, {"name": "log_date", "type": "string", "required": True, "nullable": False}, {"name": "calories", "type": "number", "required": True, "nullable": False}, {"name": "protein", "type": "number", "required": False, "nullable": False}, {"name": "carbs", "type": "number", "required": False, "nullable": False}, {"name": "fat", "type": "number", "required": False, "nullable": False}, {"name": "micronutrients", "type": "object", "required": False, "nullable": False}, {"name": "servings", "type": "number", "required": False, "nullable": False}, {"name": "food_source", "type": "string", "required": False, "nullable": False}, {"name": "food_id", "type": "string", "required": False, "nullable": False}])

@router.get("", response_model=dict)
async def list_nutrition_log(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0), q: Optional[str] = Query(None)):
    result = await repo.list(limit=limit, offset=offset, q=q)
    return {"items": result["items"], "total": result["total"]}

@router.post("", response_model=NutritionLogOut, status_code=201)
async def create_nutrition_log(data: NutritionLogCreate):
    result = await repo.create(data.model_dump())
    return NutritionLogOut(**result)

@router.get("/{id}", response_model=NutritionLogOut)
async def get_nutrition_log(id: str):
    result = await repo.get(id)
    if not result:
        raise HTTPException(status_code=404, detail=f"NutritionLog with id {id} not found")
    return NutritionLogOut(**result)

@router.put("/{id}", response_model=NutritionLogOut)
async def replace_nutrition_log(id: str, data: NutritionLogCreate):
    try:
        result = await repo.replace(id, data.model_dump())
        return NutritionLogOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=NutritionLogOut)
async def patch_nutrition_log(id: str, data: NutritionLogUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    try:
        result = await repo.patch(id, update_data)
        return NutritionLogOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=204)
async def delete_nutrition_log(id: str):
    success = await repo.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail=f"NutritionLog with id {id} not found")
    return None