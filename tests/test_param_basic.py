# tests/test_param_basic.py

import pytest

def add(a,b):
    return a+b

@pytest.mark.parametrize("a, b, expected",
                  [ (1, 1, 2), (2,3,5), (-1,3,2)])

def test_add(a, b, expected):
    assert add(a,b) == expected
