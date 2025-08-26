from typing import Type, Generic, TypeVar, Optional, Dict, Any, List
from app.dao.base_dao import BaseDAO

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType")
UpdateSchemaType = TypeVar("UpdateSchemaType")

class BaseService(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, dao: BaseDAO):
        self.dao = dao

    def get(self, id: Any) -> Optional[ModelType]:
        return self.dao.get(id)

    def get_all(
        self, 
        skip: int = 0, 
        limit: int = 100,
        filters: Optional[Dict] = None
    ) -> List[ModelType]:
        return self.dao.get_all(skip=skip, limit=limit, filters=filters)

    def create(self, obj_in: CreateSchemaType) -> ModelType:
        return self.dao.create(obj_in.dict())

    def update(self, id: Any, obj_in: UpdateSchemaType) -> Optional[ModelType]:
        return self.dao.update(id, obj_in.dict(exclude_unset=True))

    def delete(self, id: Any) -> Optional[ModelType]:
        return self.dao.delete(id)
