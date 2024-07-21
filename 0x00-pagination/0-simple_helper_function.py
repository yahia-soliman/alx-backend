#!/usr/bin/env python3
"""Calculate the start index and end index based on page & size"""
import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """Get the first and last indices of a page"""
    start = (page - 1) * page_size
    return start, start + page_size
