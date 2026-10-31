from collections import deque
from pytest import raises

def is_palindrome(thing):
    if type(thing) == str:
        pass
    if not thing:
        return False
    else:
        raise ValueError('Data type must be a string')

