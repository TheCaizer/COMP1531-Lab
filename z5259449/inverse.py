import pytest
def inverse(d):
    '''
    Given a dictionary d, invert its structure such that values in d map to lists of keys in d.
    For example:
    >>> inverse({1: 'A', 2: 'B', 3: 'A'})
    {'A': [1, 3], 'B': [2]}

    Params:
      d (dict): A dictionary where all the values are hashable (i.e. can be used as keys in the
      result).

    Returns:
      (dict): A dictionary with the structure described above.
    '''
    #check for if the given value is a fict
    if(type(d) is not dict):
        raise ValueError
    #create a new dict
    new = {}
    #iterate through all the keys and their values
    for key, value in d.items():
        #makes the key the value and makes a new list, then append the key
        #into the the new list
        #set default is a function that adds the key into value if it doesnt exist in list
        new.setdefault(value, list()).append(key)
    return new
