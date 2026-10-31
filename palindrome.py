from collections import deque
from pytest import raises

def is_palindrome(word):
    if type(word) == str:
        pass
        if not word:
            return False
        my_dq = deque()
        for i in word:
            my_dq.append(i)
        re_my_dq = deque(reversed(my_dq))
        print('my_dq : ', my_dq)
        print('re_my_dq : ', re_my_dq)
        if re_my_dq == my_dq:
            return True
        else:
            return False
    else:
        raise ValueError('Data type must be a string')




