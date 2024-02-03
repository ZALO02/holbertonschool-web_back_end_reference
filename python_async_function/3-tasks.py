#!/usr/bin/env python3
"""module that will work with the asyncio and random modules"""

import asyncio
import time

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """func that takes and int and returns an asyncio task

    Args:
        max_delay: self-explanatory

    Returns:
        an asyncio task
    """

    task_1 = asyncio.create_task(wait_random(max_delay))
    return task_1
