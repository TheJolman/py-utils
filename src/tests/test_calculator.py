import pytest
from algorithms.calculator import add, divide


def test_add_integers():
    assert add(1, 2) == 3


def test_add_floats():
    assert add(1.5, 2.5) == 4.0


def test_add_invalid_type():
    with pytest.raises(TypeError):
        add("1", 2)


def test_divide_valid():
    assert divide(6, 2) == 3.0


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_divide_invalid_type():
    with pytest.raises(TypeError):
        divide([], 2)


@pytest.mark.parametrize(
    "x,y,expected", [(4, 2, 2.0), (10, 5, 2.0), (-6, 2, -3.0), (3.6, 1.2, 3.0)]
)
def test_divide_parameterized(x, y, expected):
    assert divide(x, y) == expected
