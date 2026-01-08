from typing import List, Optional, Dict, Any
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
import uuid
import json
from app.db.postgres import get_db

class PostgresRepo:
    def __init__(self, table_name: str, columns: List[Dict[str, Any]]):
        self.table_name = table_name
        self.columns = columns
    
    async def _ensure_table(self, session: AsyncSession):
        column_defs = ["id TEXT PRIMARY KEY", "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP", "updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP"]
        for col in self.columns:
            col_name = col["name"]
            if col_name == "id":
                continue
            col_type = self._map_type(col)
            if col.get("required", False) and not col.get("nullable", False):
                column_defs.append(f'"{col_name}" {col_type} NOT NULL')
            else:
                column_defs.append(f'"{col_name}" {col_type}')
        
        create_table_sql = f"""CREATE TABLE IF NOT EXISTS {self.table_name} (
            {', '.join(column_defs)}
        )"""
        await session.execute(text(create_table_sql))
        await session.commit()
    
    def _map_type(self, col: Dict[str, Any]) -> str:
        col_type = col.get("type", "string")
        if col_type in ("object", "array"):
            return "JSONB"
        elif col_type == "string":
            return "TEXT"
        elif col_type == "number":
            return "NUMERIC"
        elif col_type == "boolean":
            return "BOOLEAN"
        elif col_type == "datetime":
            return "TIMESTAMP"
        else:
            return "TEXT"
    
    async def list(self, limit: int = 100, offset: int = 0, q: Optional[str] = None) -> Dict[str, Any]:
        async for session in get_db():
            await self._ensure_table(session)
            params = {"limit": limit, "offset": offset}
            query = f'SELECT * FROM {self.table_name}'
            conditions = []
            if q:
                text_cols = [col["name"] for col in self.columns if col.get("type") == "string"]
                conditions = [f'"{col}" ILIKE :q' for col in text_cols]
                if conditions:
                    query += f' WHERE {" OR ".join(conditions)}'
                params["q"] = f"%{q}%"
            query += ' LIMIT :limit OFFSET :offset'
            result = await session.execute(text(query), params)
            rows = result.fetchall()
            items = [dict(row._mapping) for row in rows]
            
            count_query = f'SELECT COUNT(*) as count FROM {self.table_name}'
            if q and conditions:
                count_query += f' WHERE {" OR ".join(conditions)}'
                count_result = await session.execute(text(count_query), {"q": f"%{q}%"})
            else:
                count_result = await session.execute(text(count_query))
            total = count_result.scalar()
            return {"items": items, "total": total}
    
    async def get(self, id: str) -> Optional[Dict[str, Any]]:
        async for session in get_db():
            await self._ensure_table(session)
            query = text(f'SELECT * FROM {self.table_name} WHERE id = :id')
            result = await session.execute(query, {"id": id})
            row = result.fetchone()
            return dict(row._mapping) if row else None
    
    async def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        async for session in get_db():
            await self._ensure_table(session)
            data["id"] = data.get("id") or str(uuid.uuid4())
            data["created_at"] = datetime.utcnow()
            data["updated_at"] = datetime.utcnow()
            
            cols = list(data.keys())
            placeholders = ", ".join([f":{col}" for col in cols])
            col_names = ", ".join([f'"{col}"' for col in cols])
            query = text(f'INSERT INTO {self.table_name} ({col_names}) VALUES ({placeholders}) RETURNING *')
            result = await session.execute(query, data)
            await session.commit()
            row = result.fetchone()
            return dict(row._mapping)
    
    async def replace(self, id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        async for session in get_db():
            await self._ensure_table(session)
            data["id"] = id
            data["updated_at"] = datetime.utcnow()
            
            set_clause = ", ".join([f'"{k}" = :{k}' for k in data.keys() if k != "id"])
            query = text(f'UPDATE {self.table_name} SET {set_clause}, updated_at = CURRENT_TIMESTAMP WHERE id = :id RETURNING *')
            result = await session.execute(query, data)
            await session.commit()
            row = result.fetchone()
            if not row:
                raise ValueError(f"Entity with id {id} not found")
            return dict(row._mapping)
    
    async def patch(self, id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        async for session in get_db():
            await self._ensure_table(session)
            data["updated_at"] = datetime.utcnow()
            
            set_clause = ", ".join([f'"{k}" = :{k}' for k in data.keys() if k != "id"])
            query = text(f'UPDATE {self.table_name} SET {set_clause}, updated_at = CURRENT_TIMESTAMP WHERE id = :id RETURNING *')
            result = await session.execute(query, {**data, "id": id})
            await session.commit()
            row = result.fetchone()
            if not row:
                raise ValueError(f"Entity with id {id} not found")
            return dict(row._mapping)
    
    async def delete(self, id: str) -> bool:
        async for session in get_db():
            await self._ensure_table(session)
            query = text(f'DELETE FROM {self.table_name} WHERE id = :id')
            result = await session.execute(query, {"id": id})
            await session.commit()
            return result.rowcount > 0
