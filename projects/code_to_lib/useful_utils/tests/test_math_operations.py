from useful_utils.math_operations import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 5) == 4

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(10, 7) == 3

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(20, 4) == 5
    assert divide(7, 2) == 3.5
