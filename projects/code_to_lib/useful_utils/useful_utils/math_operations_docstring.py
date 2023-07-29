def add(a, b):
    """
    Return the sum of two numbers.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Return the difference between two numbers.

    Parameters:
        a (int or float): The minuend.
        b (int or float): The subtrahend.

    Returns:
        int or float: The result of subtracting b from a.
    """
    return a - b

def multiply(a, b):
    """
    Return the product of two numbers.

    Parameters:
        a (int or float): The first factor.
        b (int or float): The second factor.

    Returns:
        int or float: The product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Return the result of dividing two numbers.

    Parameters:
        a (int or float): The dividend.
        b (int or float): The divisor.

    Returns:
        int or float: The result of dividing a by b.

    Raises:
        ValueError: If b is zero (0).
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
