from factors import factors, is_prime
import inspect
import pytest
def test_generator():
    '''
    Ensure it is generator function
    '''
    assert inspect.isgeneratorfunction(factors), "factors does not appear to be a generator"

def test_error():
    with pytest.raises(ValueError):
        factors(-1)

def test_12():
    assert list(factors(12)) == [2,2,3]

def test_100():
    assert list(factors(100)) == [2,2,5,5]
