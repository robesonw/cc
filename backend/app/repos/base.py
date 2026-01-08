from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from uuid import UUID

class CRUDRepository(ABC):
    @abstractmethod
    async def list(self, limit: int = 100, offset: int = 0, q: Optional[str] = None) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def get(self, id: str) -> Optional[Dict[str, Any]]:
        pass
    
    @abstractmethod
    async def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def replace(self, id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def patch(self, id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def delete(self, id: str) -> bool:
        pass
