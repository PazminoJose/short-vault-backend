from datetime import datetime
from typing import Optional

from pydantic import HttpUrl
from sqlmodel import Field, SQLModel


class ShortBase(SQLModel):
    title: str = Field(nullable=False)
    platform: str = Field(nullable=False)
    cover_url: str  = Field(nullable=False)
    short_url: str  = Field(nullable=False)

class ShortPublic(ShortBase):
    id: int
    created_at: datetime

class ShortCreate(ShortBase):
    user_id: int
    cover_url: HttpUrl
    short_url: HttpUrl
    pass

class ShortUpdate(ShortBase):
    title: Optional[str] = None
    platform: Optional[str] = None
    cover_url: Optional[HttpUrl] = None
    short_url: Optional[HttpUrl] = None
    