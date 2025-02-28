from fastapi import Depends

from app.repositories.url_repository import UrlRepository
from app.repositories.cache_repository import CacheRepository


class LongUrlService:
    def __init__(
        self,
        url_repository: UrlRepository = Depends(UrlRepository),
        cache_repository: CacheRepository = Depends(CacheRepository),
    ):
        self.url_repository = url_repository
        self.cache_repository = cache_repository

    def get_long_url(self, shortened_url: str) -> str | None:
        cached_long_url = self.cache_repository.get_long_url_from_shortened_url(
            shortened_url
        )
        if cached_long_url:
            return cached_long_url

        result = self.url_repository.find_long_url_from_shortened_url(shortened_url)

        if result is None:
            return None

        self.cache_repository.save_long_url(result.url, shortened_url)

        return result.url
