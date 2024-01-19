#!/usr/bin/env python3
"""Async Generator"""
import asyncio
from typing import List
import random


async def async_generator() -> List[float]:
    """Yield random numbers between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random()
