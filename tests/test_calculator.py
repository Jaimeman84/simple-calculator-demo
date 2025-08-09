import pytest
from src.calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_addition(calculator):
    assert calculator.calculate(2, 3, "+") == 5.0
    assert calculator.calculate(-1, 1, "+") == 0.0
    assert calculator.calculate(0.1, 0.2, "+") == pytest.approx(0.3)

def test_subtraction(calculator):
    assert calculator.calculate(5, 3, "-") == 2.0
    assert calculator.calculate(-1, -1, "-") == 0.0
    assert calculator.calculate(0.5, 0.2, "-") == 0.3

def test_multiplication(calculator):
    assert calculator.calculate(2, 3, "*") == 6.0
    assert calculator.calculate(-2, 3, "*") == -6.0
    assert calculator.calculate(0.5, 2, "*") == 1.0

def test_division(calculator):
    assert calculator.calculate(6, 2, "/") == 3.0
    assert calculator.calculate(-6, 2, "/") == -3.0
    assert calculator.calculate(5, 2, "/") == 2.5

def test_division_by_zero(calculator):
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        calculator.calculate(5, 0, "/")

def test_invalid_operation(calculator):
    with pytest.raises(ValueError, match="Invalid operation"):
        calculator.calculate(5, 2, "%") 