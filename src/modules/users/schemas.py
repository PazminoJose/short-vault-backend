from typing import Optional
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    email:str = Field(nullable=False)
    password: str = Field(nullable=False)
    avatar_url: str = Field(nullable=True)

class UserPublic(UserBase):
    id: int
    
class UserCreate(UserBase):
    pass

class UserUpdate(SQLModel):
    email: Optional[str] = None
    password: Optional[str] = None
    avatar_url: Optional[str] = None