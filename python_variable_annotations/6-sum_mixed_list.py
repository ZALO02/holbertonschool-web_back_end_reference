#!/usr/bin/env python3
"""module in which we'll define define a list and return
its sum"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """funct that takes a list of floats and integers
    and return its sum as a float"""
    summ: float = 0
    for elem in mxd_lst:
        summ += elem
    return summ
