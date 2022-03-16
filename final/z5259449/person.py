'''
Person Exercise
'''

class Person:
    '''
    A named person.
    '''
    def __init__(self, first_name, last_name):
        if(first_name == None):
            self.__first_name = None
        if(last_name == None):
            self.__last_name = None
        self.__first_name = first_name
        self.__last_name = last_name
    @property
    def first_name(self):
        if(self.__first_name is None):
            return None
        return f'{self.__first_name}'
    @first_name.setter
    def first_name(self, value):
        self.__first_name = value
    @property
    def last_name(self):
        if(self.__last_name is None):
            return None
        return f'{self.__last_name}'
    @last_name.setter
    def last_name(self, value):
        self.__last_name = value
    @property
    def full_name(self):
        if(self.__last_name is None):
            return f'{self.__first_name}'
        if(self.__first_name is None):
            return f'{self.__last_name}'
        return f'{self.__first_name} {self.__last_name}'
    @full_name.setter
    def full_name(self, value):
        arr = value.split()
        self.__first_name = arr[0]
        self.__last_name = arr[1]

# Do NOT change any code below this line

def test_simple():
    '''
    Check that Person tracks first, last and full name
    '''
    john = Person("John", "Smith")
    assert john.first_name == "John"
    assert john.last_name == "Smith"
    assert john.full_name == "John Smith"

def test_name_change():
    '''
    Check that names can be changed
    '''
    teacher = Person("Hayden", "Smith")
    teacher.first_name = "Rob"
    assert teacher.first_name == "Rob"
    assert teacher.full_name == "Rob Smith"

    teacher.last_name = "Everest"
    assert teacher.last_name == "Everest"
    assert teacher.full_name == "Rob Everest"

    teacher.full_name = "Simon Haddad"
    assert teacher.first_name == "Simon"
    assert teacher.last_name == "Haddad"

def test_single_name():
    '''
    Some people only have one name.
    '''
    madonna = Person("Madonna", None)
    assert madonna.first_name == "Madonna"
    assert madonna.last_name is None
    assert madonna.full_name == "Madonna"

def test_spaces():
    '''
    Extra spaces should be ignored.
    '''
    tutor = Person("Michelle", "Seeto")
    tutor.full_name = "Vivian  Dang" # Note one extra space

    # No spaces in name components
    assert tutor.first_name == "Vivian"
    assert tutor.last_name == "Dang"