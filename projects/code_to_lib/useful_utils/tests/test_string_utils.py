from useful_utils.string_utils import concatenate, reverse, substring

def test_concatenate():
    assert concatenate('Hello', 'World') == 'HelloWorld'
    assert concatenate('Python', ' is awesome') == 'Python is awesome'

def test_reverse():
    assert reverse('hello') == 'olleh'
    assert reverse('Python') == 'nohtyP'

def test_substring():
    assert substring('hello', 2, 4) == 'll'
    assert substring('hello', 2, 1) == ''
    assert substring('hello', 1, 1) == ''
