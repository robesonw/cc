from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models.recipe_comment import RecipeCommentCreate, RecipeCommentUpdate, RecipeCommentOut
from app.repos.postgres_repo import PostgresRepo

router = APIRouter()

repo = PostgresRepo("recipe_comment", [{"name": "recipe_id", "type": "string", "required": True, "nullable": False}, {"name": "comment", "type": "string", "required": True, "nullable": False}, {"name": "author_name", "type": "string", "required": False, "nullable": False}])

@router.get("", response_model=dict)
async def list_recipe_comment(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0), q: Optional[str] = Query(None)):
    result = await repo.list(limit=limit, offset=offset, q=q)
    return {"items": result["items"], "total": result["total"]}

@router.post("", response_model=RecipeCommentOut, status_code=201)
async def create_recipe_comment(data: RecipeCommentCreate):
    result = await repo.create(data.model_dump())
    return RecipeCommentOut(**result)

@router.get("/{id}", response_model=RecipeCommentOut)
async def get_recipe_comment(id: str):
    result = await repo.get(id)
    if not result:
        raise HTTPException(status_code=404, detail=f"RecipeComment with id {id} not found")
    return RecipeCommentOut(**result)

@router.put("/{id}", response_model=RecipeCommentOut)
async def replace_recipe_comment(id: str, data: RecipeCommentCreate):
    try:
        result = await repo.replace(id, data.model_dump())
        return RecipeCommentOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=RecipeCommentOut)
async def patch_recipe_comment(id: str, data: RecipeCommentUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    try:
        result = await repo.patch(id, update_data)
        return RecipeCommentOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=204)
async def delete_recipe_comment(id: str):
    success = await repo.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail=f"RecipeComment with id {id} not found")
    return None