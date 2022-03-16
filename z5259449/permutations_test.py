from permutations import permutations
from hypothesis import given, strategies, assume
import pytest
def test_empty():
    assert permutations('') == ['']
def test_ABC():
    assert permutations('ABC') == ['ABC', 'BAC', 'BCA', 'ACB', 'CAB', 'CBA']
def test_numbers():
    assert permutations('1234') ==['1234', '2134', '2314', '2341', '1324', '3124', '3214', '3241', '1342', '3142', '3412', '3421', '1243', '2143', '2413', '2431', '1423', '4123', '4213', '4231', '1432', '4132', '4312', '4321']
def test_error():
    with pytest.raises(ValueError):
        permutations(123)