from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password
from app.dao.base_dao import BaseDAO

class UserDAO(BaseDAO[User]):
    def __init__(self, db: Session):
        super().__init__(User, db)

    def create(self, obj_in: UserCreate) -> User:
        db_obj = User(
            name=obj_in.name,
            email=obj_in.email,
            password=hash_password(obj_in.password)
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()
