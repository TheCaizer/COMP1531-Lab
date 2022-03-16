from count import count_char

def test_empty():
    assert count_char("") == {}

def test_simple():
    assert count_char("abc") == {"a": 1, "b": 1, "c": 1}

def test_double():
    assert count_char("aa") == {"a": 2}

def test_capital():
    assert count_char("HelloOOo") == {"H": 1,"e": 1, "l": 2, "o": 2, "O":2}

def test_numbers():
    assert count_char("122") == {"1": 1, "2": 2}

def test_mix():
    assert count_char("12mann") == {"1": 1, "2": 1, "m": 1, "a": 1, "n": 2}

def test_space():
     assert count_char(" ") == {" ": 1}

def test_symbols():
    assert count_char("-2 > -5") == {" ": 2, "-": 2, "2": 1, "5": 1, ">": 1}