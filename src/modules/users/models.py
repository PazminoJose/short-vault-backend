from core.models import BaseTableModel
from modules.users.schemas import UserBase

class User(BaseTableModel, UserBase,  table=True):
    pass