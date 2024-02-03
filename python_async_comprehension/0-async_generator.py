#!/usr/bin/env python3
"""Coroutine that takes no args"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """corou that'll loop 10 times, wait 1 sec
    then yield a random number
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
