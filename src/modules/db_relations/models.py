from core.models import BaseTableModel
from modules.db_relations.schemas import ShortTagBase, UserTagBase


# NOTE: Model for UserTag relation
class UserTag(BaseTableModel, UserTagBase, table=True):
    pass

# NOTE: Model for ShortTag relation
class ShortTag(BaseTableModel, ShortTagBase, table=True):
    pass