#!/usr/bin/env python3
"""Async Generator"""
import asyncio
from typing import Generator


async def async_generator() -> Generator[float]:
    """Yield random numbers between 0 and 10"""
    import random
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random()
