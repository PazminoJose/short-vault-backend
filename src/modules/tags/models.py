from sqlmodel import Relationship
from core.models import BaseTableModel
from modules.db_relations.models import ShortTag
from modules.tags.schemas import TagBase
from modules.shorts.models import Short


class Tag(BaseTableModel, TagBase, table=True):
    shorts: list["Short"] = Relationship(back_populates="tags", link_model=ShortTag) 
    pass