import palindrome, pytest


def test_step1():
    with pytest.raises(ValueError):
        step1 = palindrome.is_palindrome(3)

def test_step2():
    step2 = palindrome.is_palindrome('')
    assert step2 == False



