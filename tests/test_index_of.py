import pytest
from fwc.index_of import index_of


def test_index_of():
    assert index_of([2, 7, 3, 2, 4], 2) == 0
    assert index_of([2, 7, 3, 2, 4], 8) == -1
    assert index_of([2, 7, 3, 2, 4], 2, -4) == 3
    assert index_of([2, 7, 3, 2, 4], 2, 4) == -1
