#!/usr/bin/env python3
"""module that will work with the asyncio and random modules"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """func takes an arg, waits for a rand delay and returns it

    Args:
        max_delay(int): number to wait

    Returns:
        float: random number waited

    """
    random_num: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_num)
    return random_num


if __name__ == '__main__':
    asyncio.run(wait_random())
