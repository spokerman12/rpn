import math
from ..cli import direct_mode


def test_operators_00():
    rpn_input = "2 2 +"
    solution = direct_mode(rpn_input)
    from_math = 2 + 2
    assert solution == str(from_math)


def test_operators_01():
    rpn_input = "22 2 -"
    solution = direct_mode(rpn_input)
    from_math = 22 - 2
    assert solution == str(from_math)


def test_operators_02():
    rpn_input = "15 2 *"
    solution = direct_mode(rpn_input)
    from_math = 15 * 2
    assert solution == str(from_math)


def test_operators_03():
    rpn_input = "12 2.424234 /"
    solution = direct_mode(rpn_input)
    from_math = 12 / 2.424234
    assert solution[0:6] == str(from_math)[0:6]


def test_operators_04():
    rpn_input = "17 sqrt"
    solution = direct_mode(rpn_input)
    from_math = 17 ** 0.5
    assert solution[0:6] == str(from_math)[0:6]


def test_operators_05():
    rpn_input = "4 2 **"
    solution = direct_mode(rpn_input)
    from_math = 4 ** 2
    assert solution == str(from_math)


def test_operators_06():
    rpn_input = "10 fact"
    solution = direct_mode(rpn_input)
    from_math = math.factorial(10)
    assert solution == str(from_math)


def test_operators_07():
    rpn_input = "0 not"
    solution = direct_mode(rpn_input)
    from_math = not (0)
    assert solution == str(int(from_math))


def test_operators_08():
    rpn_input = "4 5 !="
    solution = direct_mode(rpn_input)
    from_math = 4 != 5
    assert solution == str(int(from_math))


def test_operators_09():
    rpn_input = "5 2 %"
    solution = direct_mode(rpn_input)
    from_math = 5 % 2
    assert solution == str(from_math)


def test_operators_10():
    rpn_input = "2 ++"
    solution = direct_mode(rpn_input)
    from_math = 2 + 1
    assert solution == str(from_math)


def test_operators_11():
    rpn_input = "2 --"
    solution = direct_mode(rpn_input)
    from_math = 2 - 1
    assert solution == str(from_math)


def test_operators_12():
    rpn_input = "5 7 &"
    solution = direct_mode(rpn_input)
    from_math = 5 & 7
    assert solution == str(from_math)


def test_operators_13():
    rpn_input = "5 7 |"
    solution = direct_mode(rpn_input)
    from_math = 5 | 7
    assert solution == str(from_math)


def test_operators_14():
    rpn_input = "5 7 ^"
    solution = direct_mode(rpn_input)
    from_math = 5 ^ 7
    assert solution == str(from_math)


def test_operators_15():
    rpn_input = "5 7 ~"
    solution = direct_mode(rpn_input)
    from_math = (1 << 7) - 1 - 5
    assert solution == str(from_math)


def test_operators_16():
    rpn_input = " 5 2 <<"
    solution = direct_mode(rpn_input)
    from_math = 5 << 2
    assert solution == str(from_math)


def test_operators_17():
    rpn_input = "5 2 >>"
    solution = direct_mode(rpn_input)
    from_math = 5 >> 2
    assert solution == str(from_math)


def test_operators_18():
    rpn_input = "5 7 &&"
    solution = direct_mode(rpn_input)
    from_math = 5 and 7
    assert solution == str(from_math)


def test_operators_19():
    rpn_input = "5 7 ||"
    solution = direct_mode(rpn_input)
    from_math = 5 or 7
    assert solution == str(from_math)


def test_operators_20():
    rpn_input = "5 7 ^^"
    solution = direct_mode(rpn_input)
    from_math = bool(5) != bool(7)
    assert solution == str(int(from_math))


def test_operators_21():
    rpn_input = "4 5 <"
    solution = direct_mode(rpn_input)
    from_math = 4 < 5
    assert solution == str(int(from_math))


def test_operators_22():
    rpn_input = "4 5 >"
    solution = direct_mode(rpn_input)
    from_math = 4 > 5
    assert solution == str(int(from_math))


def test_operators_23():
    rpn_input = "4 5 >="
    solution = direct_mode(rpn_input)
    from_math = 4 >= 5
    assert solution == str(int(from_math))


def test_operator_24():
    rpn_input = "4 5 <="
    solution = direct_mode(rpn_input)
    from_math = 4 <= 5
    assert solution == str(int(from_math))


def test_operators_25():
    rpn_input = "0.4 acos"
    solution = direct_mode(rpn_input)
    from_math = math.acos(0.4)
    assert solution[0:4] == str(from_math)[0:4]


def test_operators_26():
    rpn_input = "0.4 asin"
    solution = direct_mode(rpn_input)
    from_math = math.asin(0.4)
    assert solution[0:4] == str(from_math)[0:4]


def test_operators_27():
    rpn_input = "46 atan"
    solution = direct_mode(rpn_input)
    from_math = math.atan(46)
    assert solution[0:4] == str(from_math)[0:4]


def test_operators_28():
    rpn_input = "46 cos"
    solution = direct_mode(rpn_input)
    from_math = math.cos(46)
    assert solution[0:4] == str(from_math)[0:4]


def test_operators_29():
    rpn_input = "46 sin"
    solution = direct_mode(rpn_input)
    from_math = math.sin(46)
    assert solution[0:4] == str(from_math)[0:4]


def test_operators_30():
    rpn_input = "46 cosh"
    solution = direct_mode(rpn_input)
    from_math = math.cosh(46)
    assert solution == str(int(from_math))


def test_operators_31():
    rpn_input = "46 sinh"
    solution = direct_mode(rpn_input)
    from_math = math.sinh(46)
    assert solution == str(int(from_math))


def test_operators_32():
    rpn_input = "456 tanh"
    solution = direct_mode(rpn_input)
    from_math = math.tanh(46)
    assert solution == str(int(from_math))


def test_operators_33():
    rpn_input = "6.12 ceil"
    solution = direct_mode(rpn_input)
    from_math = math.ceil(6.12)
    assert solution == str(from_math)


def test_operators_34():
    rpn_input = "6.12 floor"
    solution = direct_mode(rpn_input)
    from_math = math.floor(6.12)
    assert solution == str(from_math)


def test_operators_35():
    rpn_input = "6.12 2 round"
    solution = direct_mode(rpn_input)
    from_math = round(6.12, 2)
    assert solution[0:4] == str(from_math)[0:4]


def test_operators_36():
    rpn_input = "123.551 ip"
    solution = direct_mode(rpn_input)
    from_math = 123.551 // 1
    assert solution == "123"


def test_operators_37():
    rpn_input = "123.551 fp"
    solution = direct_mode(rpn_input)
    from_math = 123.551 - 123.551 // 1
    assert solution[0:6] == str(from_math)[0:6]


def test_operator38():
    rpn_input = "-123 pos"
    solution = direct_mode(rpn_input)
    from_math = 1 if -123 >= 0 else 0
    assert solution == str(from_math)


def test_operators_39():
    rpn_input = "-15 abs"
    solution = direct_mode(rpn_input)
    from_math = abs(15)
    assert solution == str(from_math)


def test_operators_40():
    rpn_input = "123 41 max"
    solution = direct_mode(rpn_input)
    from_math = max([123, 41])
    assert solution == str(from_math)


def test_operators_41():
    rpn_input = "123 41 min"
    solution = direct_mode(rpn_input)
    from_math = min([123, 41])
    assert solution == str(from_math)


def test_operators_42():
    rpn_input = "142 ln"
    solution = direct_mode(rpn_input)
    from_math = math.log(142, math.e)
    assert solution[0:6] == str(from_math)[0:6]


def test_operators_43():
    rpn_input = "155 log"
    solution = direct_mode(rpn_input)
    from_math = math.log(155, 10)
    assert solution[0:6] == str(from_math)[0:6]


def test_operators_44():
    rpn_input = "125 5 log_"
    solution = direct_mode(rpn_input)
    from_math = math.log(125, 5)
    assert solution[0:6] == str(from_math)[0:6]


def test_operators_45():
    rpn_input = "7 2 pow"
    solution = direct_mode(rpn_input)
    from_math = 7 ** 2
    assert solution == str(from_math)
