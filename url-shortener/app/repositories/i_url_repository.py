from abc import ABC, abstractmethod
from pydantic import AnyHttpUrl

from app.models.url import Url


class IUrlRepository(ABC):
    @abstractmethod
    def find_long_url_from_shortened_url(self, shortened_url: str) -> str | None:
        raise NotImplementedError

    @abstractmethod
    def find_url_from_long_url(self, url: AnyHttpUrl) -> Url | None:
        raise NotImplementedError

    @abstractmethod
    def save_shortened_url(
        self, url_id: int, url: AnyHttpUrl, shortened_url: str
    ) -> Url:
        raise NotImplementedError
