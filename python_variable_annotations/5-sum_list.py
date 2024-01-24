#!/usr/bin/env python3
"""module in which we'll define and describe different entities"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """funct that takes a list of floats
    and return its sum"""
    summ: float = 0
    for elem in input_list:
        summ += elem
    return summ
