from pydantic import AnyHttpUrl
from fastapi import FastAPI, Depends, Response
from typing import AsyncGenerator
from contextlib import asynccontextmanager

from app.controllers.long_url_controller import LongUrlController
from app.controllers.url_shortener_controller import UrlShortenerController
from app.config.database import create_tables, DatabaseEngine
from app.config.database import get_database_settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    engine = DatabaseEngine(get_database_settings())
    create_tables(engine.engine)
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/api/v1/data/shorten")
def shorten_url(
    url: AnyHttpUrl,
    url_shortener_controller: UrlShortenerController = Depends(UrlShortenerController),
) -> str:
    return url_shortener_controller.shorten_url(url)


@app.get("/api/v1/{shortened_url}")
def redirect_to_long_url(
    shortened_url: str,
    long_url_controller: LongUrlController = Depends(LongUrlController),
) -> Response:
    return long_url_controller.redirect_to_long_url(shortened_url)
