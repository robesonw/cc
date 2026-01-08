from typing import List, Optional, Dict, Any
from datetime import datetime
from uuid import uuid4
from app.db.mongo import get_database, get_collection

class MongoRepo:
    def __init__(self, collection_name: str):
        self.collection_name = collection_name
    
    def _get_collection(self):
        db = get_database()
        return get_collection(db, self.collection_name)
    
    async def list(self, limit: int = 100, offset: int = 0, q: Optional[str] = None) -> Dict[str, Any]:
        collection = self._get_collection()
        query = {}
        if q:
            query = {"$or": [{"_id": {"$regex": q, "$options": "i"}}]}
        
        cursor = collection.find(query).skip(offset).limit(limit)
        items = await cursor.to_list(length=limit)
        total = await collection.count_documents(query)
        
        for item in items:
            item["id"] = item.pop("_id", str(uuid4()))
        
        return {"items": items, "total": total}
    
    async def get(self, id: str) -> Optional[Dict[str, Any]]:
        collection = self._get_collection()
        doc = await collection.find_one({"_id": id})
        if doc:
            doc["id"] = doc.pop("_id")
        return doc
    
    async def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        collection = self._get_collection()
        doc_id = data.get("id") or str(uuid4())
        data["_id"] = doc_id
        data.pop("id", None)
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        
        await collection.insert_one(data)
        data["id"] = data.pop("_id")
        return data
    
    async def replace(self, id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        collection = self._get_collection()
        data["_id"] = id
        data.pop("id", None)
        data["updated_at"] = datetime.utcnow()
        
        result = await collection.replace_one({"_id": id}, data, upsert=False)
        if result.matched_count == 0:
            raise ValueError(f"Entity with id {id} not found")
        
        data["id"] = data.pop("_id")
        return data
    
    async def patch(self, id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        collection = self._get_collection()
        data["updated_at"] = datetime.utcnow()
        
        result = await collection.update_one({"_id": id}, {"$set": data})
        if result.matched_count == 0:
            raise ValueError(f"Entity with id {id} not found")
        
        doc = await collection.find_one({"_id": id})
        if doc:
            doc["id"] = doc.pop("_id")
        return doc
    
    async def delete(self, id: str) -> bool:
        collection = self._get_collection()
        result = await collection.delete_one({"_id": id})
        return result.deleted_count > 0
