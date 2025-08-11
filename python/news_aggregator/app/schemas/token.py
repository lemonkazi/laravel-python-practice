from pydantic import BaseModel
from app.schemas.user import UserOut

class Token(BaseModel):
    access_token: str
    refresh_token: str

class TokenWithUser(Token):
    user: UserOut

class TokenRefreshResponse(BaseModel):
    access_token: str
