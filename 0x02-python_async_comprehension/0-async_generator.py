#!/usr/bin/env python3
"""Async Generator"""
import asyncio
from typing import List


async def async_generator() -> List[float]:
    """Yield random numbers between 0 and 10"""
    import random
    for i in range(10):
        await asyncio.sleep(1)
        yield 10 * random.random()
