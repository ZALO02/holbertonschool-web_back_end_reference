#!/usr/bin/env python3
"""module that will work with the asyncio and random modules"""


import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """coroutine that spawns wait_random n times with spec delay

    Args:
        n: number of times
        max_delay: max delay

    Returns:
        List: the return value
    """

    list_a = [asyncio.create_task(wait_random(max_delay))for _ in range(n)]
    list_b = [await task for task in asyncio.as_completed(list_a)]
    return list_b
