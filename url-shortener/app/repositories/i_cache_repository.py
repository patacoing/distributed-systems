from abc import abstractmethod, ABC


class ICacheRepository(ABC):
    def get_long_url_from_shortened_url(self, shortened_url: str) -> str | None:
        raise NotImplementedError

    def get_shortened_url_from_long_url(self, long_url: str) -> str | None:
        raise NotImplementedError

    def save_shortened_url(self, shortened_url: str, long_url: str) -> str:
        raise NotImplementedError

    def save_long_url(self, long_url: str, shortened_url: str) -> str:
        raise NotImplementedError
