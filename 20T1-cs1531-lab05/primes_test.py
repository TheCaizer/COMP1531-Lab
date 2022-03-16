from primes import factors

def test_21():
    list = factors(21)
    assert list == [3, 7]

def test_315():
    list = factors(315)
    assert list == [3, 3, 5, 7]