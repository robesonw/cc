from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models.grocery_list import GroceryListCreate, GroceryListUpdate, GroceryListOut
from app.repos.postgres_repo import PostgresRepo

router = APIRouter()

repo = PostgresRepo("grocery_list", [{"name": "name", "type": "string", "required": True, "nullable": False}, {"name": "items", "type": "object", "required": False, "nullable": False}, {"name": "total_cost", "type": "number", "required": False, "nullable": False}, {"name": "notes", "type": "string", "required": False, "nullable": False}])

@router.get("", response_model=dict)
async def list_grocery_list(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0), q: Optional[str] = Query(None)):
    result = await repo.list(limit=limit, offset=offset, q=q)
    return {"items": result["items"], "total": result["total"]}

@router.post("", response_model=GroceryListOut, status_code=201)
async def create_grocery_list(data: GroceryListCreate):
    result = await repo.create(data.model_dump())
    return GroceryListOut(**result)

@router.get("/{id}", response_model=GroceryListOut)
async def get_grocery_list(id: str):
    result = await repo.get(id)
    if not result:
        raise HTTPException(status_code=404, detail=f"GroceryList with id {id} not found")
    return GroceryListOut(**result)

@router.put("/{id}", response_model=GroceryListOut)
async def replace_grocery_list(id: str, data: GroceryListCreate):
    try:
        result = await repo.replace(id, data.model_dump())
        return GroceryListOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=GroceryListOut)
async def patch_grocery_list(id: str, data: GroceryListUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    try:
        result = await repo.patch(id, update_data)
        return GroceryListOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=204)
async def delete_grocery_list(id: str):
    success = await repo.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail=f"GroceryList with id {id} not found")
    return None