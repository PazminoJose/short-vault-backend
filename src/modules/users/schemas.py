from typing import Optional

from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    name: str = Field(nullable=False)
    email: str = Field(nullable=False, unique=True, index=True)
    avatar_url: str = Field(nullable=True)


class UserPublic(UserBase):
    id: int


class UserCreate(UserBase):
    provider_user_id: str
    email_verified: bool
    pass


class UserUpdate(SQLModel):
    name: Optional[str] = None
    email: Optional[str] = None
    avatar_url: Optional[str] = None
    email_verified: Optional[bool] = None
    pass
