from inverse import inverse
import pytest
def test_inverse():
    inverse1 = {1: 'A', 2: 'B', 3: 'A'}
    assert inverse(inverse1) == {'A': [1, 3], 'B': [2]}
def test_error():
    list = ['a','b','c']
    with pytest.raises(ValueError):
        inverse(list)
def test_empty():
    dict = {}
    assert inverse(dict) == {}
