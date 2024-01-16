#!/usr/bin/env python3
"""
   Basic async syntax for python
   integer argument max_delay
   that waits for random delay
   between 0 and max_delay

   Return:
       the async function
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
