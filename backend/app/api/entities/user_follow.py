from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models.user_follow import UserFollowCreate, UserFollowUpdate, UserFollowOut
from app.repos.postgres_repo import PostgresRepo

router = APIRouter()

repo = PostgresRepo("user_follow", [{"name": "following_user_email", "type": "string", "required": True, "nullable": False}, {"name": "following_user_name", "type": "string", "required": False, "nullable": False}])

@router.get("", response_model=dict)
async def list_user_follow(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0), q: Optional[str] = Query(None)):
    result = await repo.list(limit=limit, offset=offset, q=q)
    return {"items": result["items"], "total": result["total"]}

@router.post("", response_model=UserFollowOut, status_code=201)
async def create_user_follow(data: UserFollowCreate):
    result = await repo.create(data.model_dump())
    return UserFollowOut(**result)

@router.get("/{id}", response_model=UserFollowOut)
async def get_user_follow(id: str):
    result = await repo.get(id)
    if not result:
        raise HTTPException(status_code=404, detail=f"UserFollow with id {id} not found")
    return UserFollowOut(**result)

@router.put("/{id}", response_model=UserFollowOut)
async def replace_user_follow(id: str, data: UserFollowCreate):
    try:
        result = await repo.replace(id, data.model_dump())
        return UserFollowOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=UserFollowOut)
async def patch_user_follow(id: str, data: UserFollowUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    try:
        result = await repo.patch(id, update_data)
        return UserFollowOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=204)
async def delete_user_follow(id: str):
    success = await repo.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail=f"UserFollow with id {id} not found")
    return None