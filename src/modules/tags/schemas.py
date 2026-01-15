from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class TagBase(SQLModel):
    name: str = Field(index=True, nullable=False)

class TagPublic(TagBase):
    id: int
    created_at: datetime

class TagCreate(TagBase):
    pass

class TagUpdate(TagBase):
    name: Optional[str] = None