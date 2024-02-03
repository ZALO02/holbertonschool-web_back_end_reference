#!/usr/bin/env python3
"""module that will work with the asyncio and random modules"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """func that measures the exec time of another coroutine

    Args:
        n: number of times
        max_delay: max delay

    Returns:
        average elapsed time
    """

    time_1 = time.time()
    asyncio.run(wait_n(n, max_delay))
    time_2 = time.time()
    total_time = time_2 - time_1
    return total_time / n
