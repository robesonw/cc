from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models.favorite_meal import FavoriteMealCreate, FavoriteMealUpdate, FavoriteMealOut
from app.repos.postgres_repo import PostgresRepo

router = APIRouter()

repo = PostgresRepo("favorite_meal", [{"name": "name", "type": "string", "required": True, "nullable": False}, {"name": "meal_type", "type": "string", "required": True, "nullable": False}, {"name": "calories", "type": "string", "required": False, "nullable": False}, {"name": "protein", "type": "number", "required": False, "nullable": False}, {"name": "carbs", "type": "number", "required": False, "nullable": False}, {"name": "fat", "type": "number", "required": False, "nullable": False}, {"name": "nutrients", "type": "string", "required": False, "nullable": False}, {"name": "prepTip", "type": "string", "required": False, "nullable": False}, {"name": "prepTime", "type": "string", "required": False, "nullable": False}, {"name": "prepSteps", "type": "array", "required": False, "nullable": False}, {"name": "difficulty", "type": "string", "required": False, "nullable": False}, {"name": "equipment", "type": "array", "required": False, "nullable": False}, {"name": "healthBenefit", "type": "string", "required": False, "nullable": False}, {"name": "imageUrl", "type": "string", "required": False, "nullable": False}, {"name": "cuisine", "type": "string", "required": False, "nullable": False}, {"name": "cooking_time", "type": "string", "required": False, "nullable": False}, {"name": "tags", "type": "array", "required": False, "nullable": False}, {"name": "source_type", "type": "string", "required": False, "nullable": False}, {"name": "source_meal_plan_id", "type": "string", "required": False, "nullable": False}, {"name": "source_meal_plan_name", "type": "string", "required": False, "nullable": False}, {"name": "source_recipe_id", "type": "string", "required": False, "nullable": False}, {"name": "ingredients", "type": "array", "required": False, "nullable": False}, {"name": "grocery_list", "type": "object", "required": False, "nullable": False}, {"name": "estimated_cost", "type": "number", "required": False, "nullable": False}])

@router.get("", response_model=dict)
async def list_favorite_meal(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0), q: Optional[str] = Query(None)):
    result = await repo.list(limit=limit, offset=offset, q=q)
    return {"items": result["items"], "total": result["total"]}

@router.post("", response_model=FavoriteMealOut, status_code=201)
async def create_favorite_meal(data: FavoriteMealCreate):
    result = await repo.create(data.model_dump())
    return FavoriteMealOut(**result)

@router.get("/{id}", response_model=FavoriteMealOut)
async def get_favorite_meal(id: str):
    result = await repo.get(id)
    if not result:
        raise HTTPException(status_code=404, detail=f"FavoriteMeal with id {id} not found")
    return FavoriteMealOut(**result)

@router.put("/{id}", response_model=FavoriteMealOut)
async def replace_favorite_meal(id: str, data: FavoriteMealCreate):
    try:
        result = await repo.replace(id, data.model_dump())
        return FavoriteMealOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=FavoriteMealOut)
async def patch_favorite_meal(id: str, data: FavoriteMealUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    try:
        result = await repo.patch(id, update_data)
        return FavoriteMealOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=204)
async def delete_favorite_meal(id: str):
    success = await repo.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail=f"FavoriteMeal with id {id} not found")
    return None