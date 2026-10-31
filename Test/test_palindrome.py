import palindrome, pytest


def test_zero():
    test = palindrome.is_palindrome()
    assert test == True
