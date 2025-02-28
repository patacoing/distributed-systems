from pydantic import AnyHttpUrl
from sqlmodel import Session, select
from sqlalchemy import Engine
from fastapi import Depends

from app.config.database import DatabaseEngine
from app.models.url import Url
from app.repositories.i_url_repository import IUrlRepository


class UrlRepository(IUrlRepository):
    def __init__(self, engine: DatabaseEngine = Depends(DatabaseEngine)):
        self.engine = engine.engine

    def find_long_url_from_shortened_url(self, shortened_url: str) -> str | None:
        with Session(self.engine) as session:
            stmt = select(Url).where(Url.shortened_url == shortened_url)
            result = session.exec(stmt)
            return next(result, None)

    def find_url_from_long_url(self, url: AnyHttpUrl) -> Url | None:
        with Session(self.engine) as session:
            stmt = select(Url).where(Url.url == str(url))
            result = session.exec(stmt)
            return next(result, None)

    def save_shortened_url(
        self, url_id: int, url: AnyHttpUrl, shortened_url: str
    ) -> Url:
        url_model = Url(id=url_id, url=str(url), shortened_url=shortened_url)

        with Session(self.engine) as session:
            session.add(url_model)
            session.commit()
            session.refresh(url_model)

        return url_model
