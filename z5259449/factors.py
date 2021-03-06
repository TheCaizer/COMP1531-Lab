'''
NOTE: This exercise assumes you have completed divisors.py
'''
import pytest
from divisors import divisors

# You may find this helpful
def is_prime(n):
    return n != 1 and divisors(n) == {1, n}

def factors(n):
    '''
    A generator that generates the prime factors of n. For example
    >>> list(factors(12))
    [2,2,3]
    Params:
      n (int): The operand
    Yields:
      (int): All the prime factors of n in ascending order.
    Raises:
      ValueError: When n is <= 1.
    '''
    if(n <= 1):
        raise ValueError
    else:
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                yield i
        if n > 1:
            yield n
