from sqlmodel import create_engine, SQLModel
from sqlalchemy import Engine
from fastapi import Depends

from app.config.settings import get_database_settings, DatabaseSettings


class DatabaseEngine:
    def __new__(
        cls, database_settings: DatabaseSettings = Depends(get_database_settings)
    ):
        if not hasattr(cls, "instance"):
            cls.engine = create_engine(database_settings.database_uri, echo=True)
            cls.instance = super(DatabaseEngine, cls).__new__(cls)
        return cls.instance


def create_tables(engine: Engine) -> None:
    SQLModel.metadata.create_all(engine)
