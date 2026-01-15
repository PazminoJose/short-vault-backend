from pydantic import Field

from core.models import BaseTableModel
from modules.shorts.schemas import ShortBase


class Short(BaseTableModel, ShortBase, table=True):
    userID: int = Field(nullable=False)
    pass