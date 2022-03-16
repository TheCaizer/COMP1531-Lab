from divisors import divisors
import pytest
def test_12():
    assert divisors(12) == {1,2,3,4,6,12}
def test0():
    with pytest.raises(ValueError):
        divisors(0)
def test_negative():
    with pytest.raises(ValueError):
        divisors(-1)
def test_float():
    with pytest.raises(ValueError):
        divisors(1.5)
def test100():
    assert divisors(100) == {1,2,4,5,10,20,25,50,100}