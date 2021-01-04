#
# test_validation.py: Unit tests for validating input.
#


import pytest
from ..calculator import Calculator


def test_validation_is_number_01():
    calculator = Calculator()
    rpn_input = "1"
    assert calculator.is_number(rpn_input)


def test_validation_is_number_02():
    calculator = Calculator()
    rpn_input = "1.0"
    assert calculator.is_number(rpn_input)


def test_validation_is_number_03_00():
    calculator = Calculator()
    rpn_input = "0"
    assert calculator.is_number(rpn_input)


def test_validation_is_number_03_01():
    calculator = Calculator()
    rpn_input = "10"
    assert calculator.is_number(rpn_input)


def test_validation_is_number_04():
    calculator = Calculator()
    rpn_input = "01"
    assert calculator.is_number(rpn_input) is False


def test_validation_is_number_05():
    calculator = Calculator()
    rpn_input = "01."
    assert calculator.is_number(rpn_input) is False


def test_validation_is_number_06():
    calculator = Calculator()
    rpn_input = "."
    assert calculator.is_number(rpn_input) is False


def test_validation_is_number_07():
    calculator = Calculator()
    rpn_input = "1.1343243240"
    assert calculator.is_number(rpn_input)


def test_validation_is_number_08():
    calculator = Calculator()
    rpn_input = "1.134324324.0"
    assert calculator.is_number(rpn_input) is False


def test_validation_is_number_09():
    calculator = Calculator()
    rpn_input = "1.134324324.0."
    assert calculator.is_number(rpn_input) is False


def test_validation_is_number_10():
    calculator = Calculator()
    rpn_input = "0x"
    assert calculator.is_number(rpn_input) is False


def test_validation_is_number_11():
    calculator = Calculator()
    rpn_input = "0x0"
    assert calculator.is_number(rpn_input)


def test_validation_is_number_12():
    calculator = Calculator()
    rpn_input = "0xa"
    assert calculator.is_number(rpn_input)


def test_validation_is_number_13():
    calculator = Calculator()
    rpn_input = "0xfaa"
    assert calculator.is_number(rpn_input)


def test_validation_is_number_14():
    calculator = Calculator()
    rpn_input = "0xfr"
    assert calculator.is_number(rpn_input) is False


def test_validation_is_number_15():
    calculator = Calculator()
    rpn_input = "x"
    assert calculator.is_number(rpn_input) is False


def test_validation_is_number_16():
    calculator = Calculator()
    rpn_input = "0b0"
    assert calculator.is_number(rpn_input)


def test_validation_is_number_17():
    calculator = Calculator()
    rpn_input = "1"
    assert calculator.is_number(rpn_input)


def test_validation_is_number_18():
    calculator = Calculator()
    rpn_input = "0b01"
    assert calculator.is_number(rpn_input)


def test_validation_is_number_19():
    calculator = Calculator()
    rpn_input = "10"
    assert calculator.is_number(rpn_input)


def test_validation_is_number_20():
    calculator = Calculator()
    rpn_input = "0b1010111"
    assert calculator.is_number(rpn_input)


def test_validation_is_number_21():
    calculator = Calculator()
    rpn_input = "2b"
    assert calculator.is_number(rpn_input) is False


def test_validation_is_number_22():
    calculator = Calculator()
    rpn_input = "224141w412"
    assert calculator.is_number(rpn_input) is False


def test_validation_is_number_23():
    calculator = Calculator()
    rpn_input = "224141wgaasfas412"
    assert calculator.is_number(rpn_input) is False


def test_validation_is_number_24():
    calculator = Calculator()
    rpn_input = "0000000000000000000000000002"
    assert calculator.is_number(rpn_input) is False


def test_validation_is_number_25():
    calculator = Calculator()
    rpn_input = "0o0"
    assert calculator.is_number(rpn_input)


def test_validation_is_number_26():
    calculator = Calculator()
    rpn_input = "0o01"
    assert calculator.is_number(rpn_input)


def test_validation_is_number_27():
    calculator = Calculator()
    rpn_input = "0o012312312"
    assert calculator.is_number(rpn_input)


def test_validation_is_number_28():
    calculator = Calculator()
    rpn_input = "0o12412412"
    assert calculator.is_number(rpn_input)


def test_validation_is_number_29():
    calculator = Calculator()
    rpn_input = "0o8"
    assert calculator.is_number(rpn_input) is False


def test_validation_is_number_30():
    calculator = Calculator()
    rpn_input = "0oa"
    assert calculator.is_number(rpn_input) is False


def test_validation_is_number_31():
    calculator = Calculator()
    rpn_input = "0o"
    assert calculator.is_number(rpn_input) is False


def test_validation_is_number_32():
    calculator = Calculator()
    rpn_input = "0o153165137"
    assert calculator.is_number(rpn_input)


def test_validation_is_number_33():
    calculator = Calculator()
    rpn_input = "a"
    assert calculator.is_number(rpn_input) is False


def test_validation_is_number_34():
    calculator = Calculator()
    rpn_input = "aadasdaewe"
    assert calculator.is_number(rpn_input) is False


def test_validation_is_operator_00():
    calculator = Calculator()
    rpn_input = "+"
    assert calculator.is_operator(rpn_input)


def test_validation_is_constant_00():
    calculator = Calculator()
    rpn_input = "pi"
    assert calculator.is_constant(rpn_input)


def test_validation_is_constant_01():
    calculator = Calculator()
    rpn_input = "e"
    assert calculator.is_constant(rpn_input)


def test_validation_is_constant_02():
    calculator = Calculator()
    rpn_input = "randfloat"
    assert calculator.is_constant(rpn_input)


def test_validation_validate_input_00():
    calculator = Calculator()
    rpn_input = "1 2 +"
    assert calculator.validate_input(rpn_input)


def test_validation_validate_input_01():
    calculator = Calculator()
    rpn_input = "o 2 +"
    assert calculator.validate_input(rpn_input) is False


def test_validation_validate_input_02():
    calculator = Calculator()
    rpn_input = "- 2 +"
    assert calculator.validate_input(rpn_input) is False


def test_validation_validate_input_03():
    calculator = Calculator()
    rpn_input = "2 + 2"
    assert calculator.validate_input(rpn_input) is False


def test_validation_validate_input_04():
    calculator = Calculator()
    rpn_input = "a 2 +"
    assert calculator.validate_input(rpn_input) is False


def test_validation_validate_input_05():
    calculator = Calculator()
    rpn_input = "0x1 0x2 +"
    assert calculator.validate_input(rpn_input)


def test_validation_validate_input_06():
    calculator = Calculator()
    rpn_input = "0b1 0x2 +"
    assert calculator.validate_input(rpn_input)


def test_validation_validate_input_07():
    calculator = Calculator()
    rpn_input = "0o1 0o2 +"
    assert calculator.validate_input(rpn_input)


def test_validation_validate_input_08():
    calculator = Calculator()
    rpn_input = "0b1 0b0 +"
    assert calculator.validate_input(rpn_input)


def test_validation_validate_input_09():
    calculator = Calculator()
    rpn_input = "0b1 0b0 + 0b1 0b0 + 0b0 123124124"
    assert calculator.validate_input(rpn_input) is False


def test_validation_validate_input_10():
    calculator = Calculator()
    rpn_input = "0b1 0b0 + 0b1 - 0b0 *"
    assert calculator.validate_input(rpn_input)


def test_validation_validate_input_11():
    calculator = Calculator()
    rpn_input = "0b1 0b0 + 0b1 0b0 + 0b0 / 0o125123 +"
    assert calculator.validate_input(rpn_input)


def test_validation_validate_input_12():
    calculator = Calculator()
    rpn_input = "2 + 2"
    assert calculator.validate_input(rpn_input) is False
