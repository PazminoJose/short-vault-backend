from typing import TYPE_CHECKING
from pydantic import Field
from sqlmodel import Relationship
from core.models import BaseTableModel
from modules.db_relations.models import ShortTag
from modules.shorts.schemas import ShortBase

if TYPE_CHECKING:
    from modules.tags.models import Tag


class Short(BaseTableModel, ShortBase, table=True):
    tags: list["Tag"] = Relationship(back_populates="shorts", link_model=ShortTag)
    user_id: int = Field(nullable=False, foreign_key="user.id")
