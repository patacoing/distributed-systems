from pydantic import AnyHttpUrl
from fastapi import Depends

from app.services.url_shortener_service import UrlShortenerService


class UrlShortenerController:
    def __init__(
        self,
        url_shortener_service: UrlShortenerService = Depends(UrlShortenerService),
    ) -> None:
        self.url_shortener_service = url_shortener_service

    def shorten_url(self, url: AnyHttpUrl) -> str:
        return self.url_shortener_service.shorten_url(url)
