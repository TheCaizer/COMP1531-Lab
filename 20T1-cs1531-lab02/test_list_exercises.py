from list_exercises import *

def test_reverse():
    l = ["how", "are", "you"]
    reverse_list(l)
    assert l == ["you", "are", "how"]

    m = ["how", 0 ,"me"]
    reverse_list(m)
    assert m == ["me" , 0 , 'how']

    n = []
    reverse_list(n)
    assert n == []

    o = ["dope"]
    reverse_list(o)
    assert o == ["dope"]

def test_min():
    assert minimum([1, 2, 3, -10]) == -10
    assert minimum([0, 10 ,-10]) == -10

def test_sum():
    assert sum_list([7, 7, 7]) == 21
    assert sum_list([-7,7,7]) == 7
    