from pydantic import Field
from core.models import BaseTableModel

# NOTE: Model for UserTag relation
class UserTag(BaseTableModel, table=True):
    user_id: int = Field(foreign_key="user.id")
    tag_id: int = Field(foreign_key="tag.id")
    pass

# NOTE: Model for ShortTag relation
class ShortTag(BaseTableModel, table=True):
    short_id: int = Field(foreign_key="short.id")
    tag_id: int = Field(foreign_key="tag.id")
    pass