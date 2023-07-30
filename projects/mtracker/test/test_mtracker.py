import pytest
from mtracker.mtracker import execute_and_get_memory_usage

def _generate_list(n):
    lst = []
    for i in range(n):
        lst.append(i)
    return lst

def test_no_change():
    n = 10
    lst1 = _generate_list(n)
    lst2 = execute_and_get_memory_usage(_generate_list, n)
    assert len(lst1) == len(lst2)
    for l1, l2 in zip(lst1, lst2):        
        assert l1 == l2
