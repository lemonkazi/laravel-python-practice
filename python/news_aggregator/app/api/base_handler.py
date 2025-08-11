from fastapi import APIRouter, Depends, HTTPException
from typing import Type, Generic, TypeVar
from pydantic import BaseModel
from app.dao.base_dao import BaseDAO
from app.services.base_service import BaseService
from app.db.deps import get_db
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class BaseHandler(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, dao: BaseDAO):
        self.router = APIRouter()
        self.dao = dao

    def get_all(self, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return self.dao.find_all(skip=skip, limit=limit)

    def get(self, id: int, db: Session = Depends(get_db)):
        obj = self.dao.get(id)
        if not obj:
            raise HTTPException(status_code=404, detail="Item not found")
        return obj

    def create(self, obj_in: CreateSchemaType, db: Session = Depends(get_db)):
        return self.dao.create(obj_in)

    def update(self, id: int, obj_in: UpdateSchemaType, db: Session = Depends(get_db)):
        obj = self.dao.update(id, obj_in)
        if not obj:
            raise HTTPException(status_code=404, detail="Item not found")
        return obj

    def delete(self, id: int, db: Session = Depends(get_db)):
        obj = self.dao.delete(id)
        if not obj:
            raise HTTPException(status_code=404, detail="Item not found")
        return obj