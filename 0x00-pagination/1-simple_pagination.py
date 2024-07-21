#!/usr/bin/env python3
"""Calculate the start index and end index based on page & size"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Get the first and last indices of a page"""
    start = (page - 1) * page_size
    return start, start + page_size


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
        """Get the nth `page` of size `page_size` from the dataset
        """
        assert type(page) is type(page_size) is int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        max = len(data) - 1
        if start > max:
            return []

        return [data[i] for i in range(start, min(end, max))]
