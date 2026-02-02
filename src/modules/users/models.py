from sqlmodel import Field

from src.core.models import BaseTableModel
from src.modules.users.schemas import UserBase


class User(BaseTableModel, UserBase, table=True):
    provider_user_id: str = Field(nullable=False, unique=True, index=True)
    email_verified: bool = Field(default=False)
    pass
