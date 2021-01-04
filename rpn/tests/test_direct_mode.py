#
# test_direct_mode.py: Unit tests for direct mode
#

import pytest
from ..cli import direct_mode


def test_direct_mode_00_0():
    rpn_input = "0"
    solution = direct_mode(rpn_input)
    assert solution == "0"


def test_direct_mode_00_1():
    rpn_input = "2"
    solution = direct_mode(rpn_input)
    assert solution == "2"


def test_direct_mode_01():
    rpn_input = "2 2 +"
    solution = direct_mode(rpn_input)
    assert solution == "4"


def test_direct_mode_02():
    rpn_input = "2 2 -"
    solution = direct_mode(rpn_input)
    assert solution == "0"


def test_direct_mode_03():
    rpn_input = "2 3 *"
    solution = direct_mode(rpn_input)
    assert solution == "6"


def test_direct_mode_04():
    rpn_input = "2 2 /"
    solution = direct_mode(rpn_input)
    assert solution == "1"


# From https://hansklav.home.xs4all.nl/rpn/
def test_direct_mode_05():
    rpn_input = "2 sqrt"
    solution = direct_mode(rpn_input)
    assert solution[0:4] == "1.41"


def test_direct_mode_06():
    rpn_input = "34 2 **"
    solution = direct_mode(rpn_input)
    assert solution == "1156"


def test_direct_mode_07():
    rpn_input = "12 3 +"
    solution = direct_mode(rpn_input)
    assert solution == "15"


def test_direct_mode_08():
    # 12 + 34 + 56 – 78 + 90 – 12)
    rpn_input = "12 34 + 56 + 78 - 90 + 12 -"
    solution = direct_mode(rpn_input)
    assert solution == "102"


def test_direct_mode_09():
    # 3 × (4 + (5 × (6 + 7)))
    rpn_input = "6 7 + 5 * 4 + 3 *"
    solution = direct_mode(rpn_input)
    assert solution == "207"


def test_direct_mode_10():
    rpn_input = " 0b1111 0b1100 - --bin"
    solution = direct_mode(rpn_input)
    assert solution == "0b11"


def test_direct_mode_11():
    rpn_input = " 0b1111 0b1100 - --bin"
    solution_1 = direct_mode(rpn_input)
    rpn_input = " 0b1111 0b1100 - --bin"
    solution_2 = direct_mode(rpn_input)
    assert int(solution_1,2) == int(solution_2,2)


def test_direct_mode_12():
    rpn_input = " 123 4124124 *"
    solution = direct_mode(rpn_input)
    assert solution == str(123*4124124)

