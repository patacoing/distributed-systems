from fastapi import Depends
from redis.cluster import RedisCluster

from app.config.settings import CacheSettings, get_cache_settings


class CacheClient:
    def __new__(cls, cache_settings: CacheSettings = Depends(get_cache_settings)):
        if not hasattr(cls, "instance"):
            cls.client = RedisCluster(
                host=cache_settings.cache_host,
                port=cache_settings.cache_port,
            )
            cls.instance = super(CacheClient, cls).__new__(cls)
        return cls.instance
