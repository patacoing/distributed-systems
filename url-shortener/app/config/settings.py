from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="allow")


class DatabaseSettings(EnvBaseSettings):
    database_uri: str


class CacheSettings(EnvBaseSettings):
    cache_host: str
    cache_port: int


class LocationSettings(EnvBaseSettings):
    datacenter_id: int
    machine_id: int
    time_interval: int = 10000


database_settings = DatabaseSettings()
location_settings = LocationSettings()
cache_settings = CacheSettings()


def get_database_settings():
    return database_settings


def get_location_settings():
    return location_settings


def get_cache_settings():
    return cache_settings
