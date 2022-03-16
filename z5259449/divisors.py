import pytest
def divisors(n):
    '''
    Given some number n, return a set of all the numbers that divide it. For example:
    >>> divisors(12)
    {1, 2, 3, 4, 6, 12}

    Params:
      n (int): The operand

    Returns:
      (set of int): All the divisors of n

    Raises:
      ValueError: If n is not a positive integer
    '''
    if(n <= 0):
        raise ValueError
    #test that you are given an int
    elif(type(n)  is not int):
        raise ValueError
    list = []
    for i in range(1,n+1):
        if(n%i==0):
            list.append(i)
    list = set(list)
    return list
