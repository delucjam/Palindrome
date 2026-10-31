from collections import deque
from pytest import raises

def is_palindrome(word):
    if type(word) == str:
        pass
        if not word:
            return False
        my_dq = deque([word])
        re_my_dq = deque(reversed(my_dq))
        if re_my_dq == my_dq:
            return True
        return False
    else:
        raise ValueError('Data type must be a string')




