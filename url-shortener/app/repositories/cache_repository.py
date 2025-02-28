from fastapi import Depends

from app.repositories.i_cache_repository import ICacheRepository
from app.config.cache import CacheClient


class CacheRepository(ICacheRepository):
    def __init__(self, cache_engine: CacheClient = Depends(CacheClient)):
        self.client = cache_engine.client

    def get_long_url_from_shortened_url(self, shortened_url: str) -> str | None:
        return self._get(shortened_url)

    def get_shortened_url_from_long_url(self, long_url: str) -> str | None:
        return self._get(long_url)

    def save_shortened_url(self, shortened_url: str, long_url: str) -> str:
        return self._save(long_url, shortened_url)

    def save_long_url(self, long_url: str, shortened_url: str) -> str:
        return self._save(shortened_url, long_url)

    def _save(self, key: str, value: str, expire: int = 100) -> str:
        self.client.set(key, value, ex=expire)
        return value

    def _get(self, key: str) -> str | None:
        value = self.client.get(key)
        if value is None:
            return None

        return value.decode()
