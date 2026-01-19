from sqlmodel import Field, SQLModel


# NOTE: Schema for UserTag relation
class UserTagBase(SQLModel):
    user_id: int = Field(foreign_key="user.id")
    tag_id: int = Field(foreign_key="tag.id")

class UserTagPublic(UserTagBase):
    id: int

class UserTagCreate(UserTagBase):
    pass


# NOTE: Schema for ShortTag relation
class ShortTagBase(SQLModel):
    short_id: int = Field(foreign_key="short.id")
    tag_id: int = Field(foreign_key="tag.id")

class ShortTagPublic(ShortTagBase):
    id: int
    
class ShortTagCreate(ShortTagBase):
    pass