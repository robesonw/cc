from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models.forum_post import ForumPostCreate, ForumPostUpdate, ForumPostOut
from app.repos.postgres_repo import PostgresRepo

router = APIRouter()

repo = PostgresRepo("forum_post", [{"name": "title", "type": "string", "required": True, "nullable": False}, {"name": "content", "type": "string", "required": True, "nullable": False}, {"name": "category", "type": "string", "required": True, "nullable": False}, {"name": "tags", "type": "array", "required": False, "nullable": False}, {"name": "likes_count", "type": "number", "required": False, "nullable": False}, {"name": "views_count", "type": "number", "required": False, "nullable": False}, {"name": "comments_count", "type": "number", "required": False, "nullable": False}, {"name": "is_pinned", "type": "boolean", "required": False, "nullable": False}, {"name": "author_name", "type": "string", "required": False, "nullable": False}])

@router.get("", response_model=dict)
async def list_forum_post(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0), q: Optional[str] = Query(None)):
    result = await repo.list(limit=limit, offset=offset, q=q)
    return {"items": result["items"], "total": result["total"]}

@router.post("", response_model=ForumPostOut, status_code=201)
async def create_forum_post(data: ForumPostCreate):
    result = await repo.create(data.model_dump())
    return ForumPostOut(**result)

@router.get("/{id}", response_model=ForumPostOut)
async def get_forum_post(id: str):
    result = await repo.get(id)
    if not result:
        raise HTTPException(status_code=404, detail=f"ForumPost with id {id} not found")
    return ForumPostOut(**result)

@router.put("/{id}", response_model=ForumPostOut)
async def replace_forum_post(id: str, data: ForumPostCreate):
    try:
        result = await repo.replace(id, data.model_dump())
        return ForumPostOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=ForumPostOut)
async def patch_forum_post(id: str, data: ForumPostUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    try:
        result = await repo.patch(id, update_data)
        return ForumPostOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=204)
async def delete_forum_post(id: str):
    success = await repo.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail=f"ForumPost with id {id} not found")
    return None