#!/usr/bin/env python3
"""module that will work with the asyncio and random modules"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """coroutine that spawns wait_random n times with spec delay

    Args:
        n: number of times
        max_delay: max delay

    Returns:
        List: the return value
    """

    list_a = [await task_wait_random(max_delay) for _ in range(n)]
    return sorted(list_a)
