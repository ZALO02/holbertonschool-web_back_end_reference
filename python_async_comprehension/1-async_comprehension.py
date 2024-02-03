#!/usr/bin/env python3
"""Coroutine that takes no args"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """corou that'll collect 10 num using async comp, then
    returning 10 rand numbers
    """

    rand_list = [i async for i in async_generator()]
    return rand_list
