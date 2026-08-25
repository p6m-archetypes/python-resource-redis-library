from __future__ import annotations

import redis.asyncio as aioredis

_client: aioredis.Redis | None = None


async def init_cache(settings) -> None:
    global _client
    _client = aioredis.from_url(settings.redis_url, decode_responses=True)


async def close_cache() -> None:
    global _client
    if _client is not None:
        await _client.aclose()
        _client = None


def get_cache() -> aioredis.Redis:
    if _client is None:
        raise RuntimeError("Cache not initialized — call init_cache() first")
    return _client
