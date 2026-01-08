from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models.forum_comment import ForumCommentCreate, ForumCommentUpdate, ForumCommentOut
from app.repos.postgres_repo import PostgresRepo

router = APIRouter()

repo = PostgresRepo("forum_comment", [{"name": "post_id", "type": "string", "required": True, "nullable": False}, {"name": "content", "type": "string", "required": True, "nullable": False}, {"name": "likes_count", "type": "number", "required": False, "nullable": False}, {"name": "author_name", "type": "string", "required": False, "nullable": False}, {"name": "reactions", "type": "object", "required": False, "nullable": False}])

@router.get("", response_model=dict)
async def list_forum_comment(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0), q: Optional[str] = Query(None)):
    result = await repo.list(limit=limit, offset=offset, q=q)
    return {"items": result["items"], "total": result["total"]}

@router.post("", response_model=ForumCommentOut, status_code=201)
async def create_forum_comment(data: ForumCommentCreate):
    result = await repo.create(data.model_dump())
    return ForumCommentOut(**result)

@router.get("/{id}", response_model=ForumCommentOut)
async def get_forum_comment(id: str):
    result = await repo.get(id)
    if not result:
        raise HTTPException(status_code=404, detail=f"ForumComment with id {id} not found")
    return ForumCommentOut(**result)

@router.put("/{id}", response_model=ForumCommentOut)
async def replace_forum_comment(id: str, data: ForumCommentCreate):
    try:
        result = await repo.replace(id, data.model_dump())
        return ForumCommentOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=ForumCommentOut)
async def patch_forum_comment(id: str, data: ForumCommentUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    try:
        result = await repo.patch(id, update_data)
        return ForumCommentOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=204)
async def delete_forum_comment(id: str):
    success = await repo.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail=f"ForumComment with id {id} not found")
    return None