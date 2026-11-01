from collections import deque

def is_palindrome(word):
    if type(word) == str:
        if not word:
            return False
        original_dq = deque([], len(word))
        for i in word:
            original_dq.append(i.lower())
            print(original_dq)
        reverse_dq = original_dq.copy()
        reverse_dq.extendleft(reverse_dq)
        print('reverse :', reverse_dq)
        if reverse_dq == original_dq:
            return True
        else:
            return False
    else:
        raise ValueError('Data type must be a string')



