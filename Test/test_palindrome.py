import palindrome, pytest
from collections import deque

def test_step1():
    with pytest.raises(ValueError):
        step1 = palindrome.is_palindrome(3)

def test_step2():
    step2 = palindrome.is_palindrome('')
    assert step2 == False

def test_step3():
    step3 = palindrome.is_palindrome('a')
    assert step3 == True


