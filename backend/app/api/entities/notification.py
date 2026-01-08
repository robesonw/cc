from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models.notification import NotificationCreate, NotificationUpdate, NotificationOut
from app.repos.postgres_repo import PostgresRepo

router = APIRouter()

repo = PostgresRepo("notification", [{"name": "recipient_email", "type": "string", "required": True, "nullable": False}, {"name": "type", "type": "string", "required": True, "nullable": False}, {"name": "title", "type": "string", "required": True, "nullable": False}, {"name": "message", "type": "string", "required": True, "nullable": False}, {"name": "link", "type": "string", "required": False, "nullable": False}, {"name": "is_read", "type": "boolean", "required": False, "nullable": False}, {"name": "actor_name", "type": "string", "required": False, "nullable": False}])

@router.get("", response_model=dict)
async def list_notification(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0), q: Optional[str] = Query(None)):
    result = await repo.list(limit=limit, offset=offset, q=q)
    return {"items": result["items"], "total": result["total"]}

@router.post("", response_model=NotificationOut, status_code=201)
async def create_notification(data: NotificationCreate):
    result = await repo.create(data.model_dump())
    return NotificationOut(**result)

@router.get("/{id}", response_model=NotificationOut)
async def get_notification(id: str):
    result = await repo.get(id)
    if not result:
        raise HTTPException(status_code=404, detail=f"Notification with id {id} not found")
    return NotificationOut(**result)

@router.put("/{id}", response_model=NotificationOut)
async def replace_notification(id: str, data: NotificationCreate):
    try:
        result = await repo.replace(id, data.model_dump())
        return NotificationOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=NotificationOut)
async def patch_notification(id: str, data: NotificationUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    try:
        result = await repo.patch(id, update_data)
        return NotificationOut(**result)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=204)
async def delete_notification(id: str):
    success = await repo.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Notification with id {id} not found")
    return None