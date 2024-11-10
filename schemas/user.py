from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    rol_id: int

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int