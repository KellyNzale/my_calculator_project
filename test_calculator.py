import pytest
from calculator import Calculator, Calculation

@pytest.mark.parametrize("a,b,operator,expected", [
    (3, 2, '+', 5),
    (5, 3, '-', 2),
    (4, 3, '*', 12),
    (10, 2, '/', 5),
])
def test_calculate(a, b, operator, expected):
    result = Calculator.calculate(a, b, operator)
    assert result == expected
    last_calc = Calculator.get_last_calculation()
    assert last_calc.result == expected
    assert last_calc.operator == operator

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(10, 0)

def test_clear_history():
    Calculator.clear_history()
    assert Calculator.get_last_calculation() is None
