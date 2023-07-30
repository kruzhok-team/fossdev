import pytest
from calculator import Calculator

# Define the fixture to set up an instance of the Calculator class for testing
@pytest.fixture
def calculator_instance():
    return Calculator()

def test_add(calculator_instance):
    result = calculator_instance.add(3, 4)
    assert result == 7

def test_subtract(calculator_instance):
    result = calculator_instance.subtract(10, 5)
    assert result == 5

def test_multiply(calculator_instance):
    result = calculator_instance.multiply(2, 3)
    assert result == 6

def test_divide(calculator_instance):
    result = calculator_instance.divide(10, 2)
    assert result == 5

def test_divide_by_zero(calculator_instance):
    with pytest.raises(ValueError):
        calculator_instance.divide(10, 0)

def test_divide_float(calculator_instance):
    result = calculator_instance.divide(5, 0.1)
    assert result == pytest.approx(50)

if __name__ == '__main__':
    pytest.main()
