#
# test_calculation.py: Unit tests for calculations
#

import pytest
from ..calculator import Calculator


def test_calculation_00_0():
    calculator = Calculator()
    rpn_input = "0"
    solution = calculator.solve(rpn_input)
    assert solution == 0


def test_calculation_00_1():
    calculator = Calculator()
    rpn_input = "0"
    solution = calculator.solve(rpn_input)
    assert solution == 0


def test_calculation_00_2():
    calculator = Calculator()
    rpn_input = "0"
    solution = calculator.solve(rpn_input)
    assert solution == 0


def test_calculation_00_3():
    calculator = Calculator()
    rpn_input = "0"
    solution = calculator.solve(rpn_input)
    assert solution == 0


def test_calculation_00_4():
    calculator = Calculator()
    rpn_input = "1"
    solution = calculator.solve(rpn_input)
    assert solution == 1


def test_calculation_01():
    calculator = Calculator()
    rpn_input = "2 2 +"
    solution = calculator.solve(rpn_input)
    assert solution == 4


def test_calculation_02():
    calculator = Calculator()
    rpn_input = "2 2 -"
    solution = calculator.solve(rpn_input)
    assert solution == 0


def test_calculation_03():
    calculator = Calculator()
    rpn_input = "2 3 *"
    solution = calculator.solve(rpn_input)
    assert solution == 6


def test_calculation_04():
    calculator = Calculator()
    rpn_input = "2 2 /"
    solution = calculator.solve(rpn_input)
    assert solution == 1


def test_calculation_05():
    calculator = Calculator()
    rpn_input = "9 fact"
    solution = calculator.solve(rpn_input)
    assert solution == 362880


def test_calculation_06():
    calculator = Calculator()
    rpn_input = "121 sqrt -1 **"
    solution = calculator.solve(rpn_input)
    assert "0.090909090" in str(solution)


def test_calculation_07():
    calculator = Calculator()
    rpn_input = "426 123 /"
    solution = calculator.solve(rpn_input)
    assert "3.463414634" in str(solution)


def test_calculation_07():
    # (13 + 8) × log 100
    calculator = Calculator()
    rpn_input = "13 8 + 100 log *"
    solution = calculator.solve(rpn_input)
    assert "42" in str(solution)


def test_calculation_08():
    # 3[4 + 5(6 + 7)]
    calculator = Calculator()
    rpn_input = "6 7 + 5 * 4 + 3 *"
    solution = calculator.solve(rpn_input)
    assert "207" in str(solution)


def test_calculation_09():
    # 3[4 + 5(6 + 7)]
    calculator = Calculator()
    rpn_input = "3 4 5 6 7 + * + *"
    solution = calculator.solve(rpn_input)
    assert "207" in str(solution)
