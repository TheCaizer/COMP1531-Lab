def reverse_words(string_list):
    new_list = []
    space = " "
    for n in string_list:
        temp = n.split()
        temp.reverse()
        result = space.join(temp)
        new_list.append(result)
    string_list = new_list
    return string_list

def test_word():
    string_list = ["Hello World", "How are You"]
    assert reverse_words(string_list) == ["World Hello", "You are How"]

def test_single():
    string_list = ["Hello World"]
    assert reverse_words(string_list) == ["World Hello"]

def test_empty():
    string_list = []
    assert reverse_words(string_list) == []

def test_space():
    string_list = [" "]
    assert reverse_words(string_list) == [" "]

def test_space_word():
    string_list = [" ", "My Name is Jim"]
    assert reverse_words(string_list) == ["", "Jim is Name My"]

