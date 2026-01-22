from typing import TYPE_CHECKING

from sqlmodel import Relationship

from src.core.models import BaseTableModel
from src.modules.db_relations.models import ShortTag
from src.modules.tags.schemas import TagBase

if TYPE_CHECKING:
    from src.modules.shorts.models import Short


class Tag(BaseTableModel, TagBase, table=True):
    shorts: list["Short"] = Relationship(back_populates="tags", link_model=ShortTag)
    pass
