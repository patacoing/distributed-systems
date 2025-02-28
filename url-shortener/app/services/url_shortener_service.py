from fastapi import Depends
from pydantic import AnyHttpUrl

from app.services.hasher_service import HasherService
from app.services.unique_id_generator_service import UniqueIdGeneratorService
from app.repositories.url_repository import UrlRepository
from app.repositories.cache_repository import CacheRepository


class UrlShortenerService:
    def __init__(
        self,
        url_repository: UrlRepository = Depends(UrlRepository),
        cache_repository: CacheRepository = Depends(CacheRepository),
        hasher_service: HasherService = Depends(HasherService),
        unique_id_generator_service: UniqueIdGeneratorService = Depends(
            UniqueIdGeneratorService
        ),
    ):
        self.url_repository = url_repository
        self.cache_repository = cache_repository
        self.hasher_service = hasher_service
        self.unique_id_generator_service = unique_id_generator_service

    def shorten_url(self, url: AnyHttpUrl) -> str:
        if (
            cached_shortened_url
            := self.cache_repository.get_shortened_url_from_long_url(str(url))
        ):
            return cached_shortened_url

        existing_url = self.url_repository.find_url_from_long_url(url)
        if existing_url is not None:
            self.cache_repository.save_shortened_url(
                existing_url.shortened_url, existing_url.url
            )
            return existing_url.shortened_url

        unique_id = self.unique_id_generator_service.generate_unique_id()
        hashed_url = self.hasher_service.hash(unique_id)

        url_model = self.url_repository.save_shortened_url(unique_id, url, hashed_url)

        return url_model.shortened_url
