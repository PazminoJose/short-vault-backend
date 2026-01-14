from sqlmodel import Session, SQLModel, create_engine

from core import config

db_url = config.get_settings().DATABASE_URL
engine = create_engine(db_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session