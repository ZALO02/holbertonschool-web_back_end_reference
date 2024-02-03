#!/usr/bin/env python3
"""Coroutine that'll execute parallelism"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """corou that'll exec async_comp 4 times, then
    returning elapsed time
    """

    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    finish = time.perf_counter()
    return finish - start
