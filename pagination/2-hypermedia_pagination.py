#!/usr/bin/env python3
"""simple pagination"""
import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """def that returns a list containing the range
        specified in the tuple passed"""
        assert type(page) is int and type(page_size) is int
        assert page > 0
        assert page_size > 0
        self.dataset()

        tup = self.index_range(page, page_size)

        if tup[0] >= len(self.__dataset):
            return []
        else:
            return self.__dataset[tup[0]:tup[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """func that builds a dict in function of certain
        parameters
        """
        total_pages = math.ceil(len(self.dataset())/page_size)
        p = {
                "page size": page_size,
                "page": page,
                "data": self.get_page(page, page_size),
                "next page": page + 1 if page < total_pages else None,
                "prev_page": page - 1 if page > 1 else None
        }
        return p

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        '''funct that returns a tuple containing
        start and ending indexes
        '''

        index = page * page_size - page_size
        index_1 = index + page_size
        return (index, index_1)
