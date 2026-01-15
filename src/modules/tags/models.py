from core.models import BaseTableModel
from modules.tags.schemas import TagBase


class Tag(BaseTableModel, TagBase, table=True):
    pass