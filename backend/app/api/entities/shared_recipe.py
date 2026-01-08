from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models.shared_recipe import SharedRecipeCreate, SharedRecipeUpdate, SharedRecipeOut
from app.repos.postgres_repo import PostgresRepo

router = APIRouter()

repo = PostgresRepo("shared_recipe", [{"name": "name", "type": "string", "required": True, "nullable": False}, {"name": "meal_type", "type": "string", "required": True, "nullable": False}, {"name": "description", "type": "string", "required": False, "nullable": False}, {"name": "meal_data", "type": "object", "required": True, "nullable": False}, {"name": "calories", "type": "string", "required": False, "nullable": False}, {"name": "protein", "type": "number", "required": False, "nullable": False}, {"name": "carbs", "type": "number", "required": False, "nullable": False}, {"name": "fat", "type": "number", "required": False, "nullable": False}, {"name": "image_url", "type": "string", "required": False, "nullable": False}, {"name": "tags", "type": "array", "required": False, "nullable": False}, {"name": "views_count", "type": "number", "required": False, "nullable": False}, {"name": "likes_count", "type": "number", "required": False, "nullable": False}, {"name": "saves_count", "type": "number", "required": False, "nullable": False}, {"name": "average_rating", "type": "number", "required": False, "nullable": False}, {"name": "author_name", "type": "string", "required": False, "nullable": False}, {"name": "status", "type": "string", "required": False, "nullable": False}, {"name": "moderation_notes", "type": "string", "required": False, "nullable": False}, {"name": "cuisine", "type": "string", "required": False, "nullable": False}, {"name": "difficulty", "type": "string", "required": False, "nullable": False}, {"name": "prep_time", "type": "string", "required": False, "nullable": False}, {"name": "cooking_time", "type": "string", "required": False, "nullable": False}, {"name": "servings", "type": "number", "required": False, "nullable": False}, {"name": "ingredients", "type": "array", "required": False, "nullable": False}, {"name": "prep_steps", "type": "array", "required": False, "nullable": False}])

@router.get("", response_model=dict)
async def list_shared_recipe(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0), q: Optional[str] = Query(None)):
    result = await repo.list(limit=limit, offset=offset, q=q)
    return {"items": result["items"], "total": result["total"]}

@router.post("", response_model=SharedRecipeOut, status_code=201)
async def create_shared_recipe(data: SharedRecipeCreate):
    result = await repo.create(data.model_dump())
    return SharedRecipeOut(**result)

@router.get("/{id}", response_model=SharedRecipeOut)
async def get_shared_recipe(id: str):
    result = await repo.get(id)
    if not result:
        raise HTTPException(status_code=404, detail=f"SharedRecipe with id {id} not found")
    return SharedRecipeOut(**result)

@router.put("/{id}", response_model=SharedRecipeOut)
async def replace_shared_recipe(id: str, data: SharedRecipeCreate):
    try:
        result = await repo.replace(id, data.model_dump())
        return SharedRecipeOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=SharedRecipeOut)
async def patch_shared_recipe(id: str, data: SharedRecipeUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    try:
        result = await repo.patch(id, update_data)
        return SharedRecipeOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=204)
async def delete_shared_recipe(id: str):
    success = await repo.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail=f"SharedRecipe with id {id} not found")
    return None