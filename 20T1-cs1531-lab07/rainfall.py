import statistics
from functools import reduce
import pytest

def rainfall(nums):
    length = list(filter(lambda m : m > 0, nums))
    sum = reduce(lambda a,b : a + b if(a>0 and b>0) else -1 * b + b + a,nums)
    # also can just do (lambda a,b: a+b, length)
    if(len(length) == 0):
        raise ValueError
    ans = sum/len(length)
    return ans
rainfall([1, -5, 3, 4, 4])
def test_simple():
    assert rainfall([1, 2, 3]) == 2

def test_negative():
    assert rainfall([1, -5, 3, 4, 4]) == 3

def test_zero():
    assert rainfall([1, 0, 2, 3]) == 2

def test_empty():
    with pytest.raises(ValueError):
        rainfall([-1, -2, -3])
