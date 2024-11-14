from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers together

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b

    Raises:
        TypeError: If a or b are not numbers
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    return a + b


def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Divide a by b.

    Args:
        a: First number
        b: Second number

    Returns:
        Quotient of a divided by b

    Raises:
        TypeError: If a or b are not numbers
        ValueError: If b is zero
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
