#!/usr/bin/env python3
"""module in which we'll encounter pagination projects"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function that returns a tuple containing
    start and ending indexes
    """

    index_1 = page * page_size - page_size
    index_2 = index_1 + page_size
    return (index_1, index_2)
