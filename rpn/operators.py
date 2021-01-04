#
# operators.py: The operators currently implemented
# 				in rpn. Feel free to add your own.
# 				Lambda calculus ROCKS!
#
# 				More detailed info on each one in README.md
#


import math

operators = {
    # Arithmetics
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "sqrt": lambda x: x ** (1 / 2),
    "**": lambda x, y: x ** y,
    "fact": lambda x: int(math.factorial(x)),
    "not": lambda x: not (x),
    "!=": lambda x, y: x != y,
    "%": lambda x, y: x % y,
    "++": lambda x: x + 1,
    "--": lambda x: x - 1,
    # Bitwise
    "&": lambda x, y: x & y,
    "|": lambda x, y: x | y,
    "^": lambda x, y: x ^ y,
    "~": lambda x, y: (1 << y) - 1 - x,
    "<<": lambda x, y: x << y,
    ">>": lambda x, y: x >> y,
    # Boolean
    "&&": lambda x, y: x and y,
    "||": lambda x, y: x or y,
    "^^": lambda x, y: bool(x) != bool(y),
    # Arithmetic comparison
    "<": lambda x, y: x < y,
    "<=": lambda x, y: x <= y,
    "==": lambda x, y: x == y,
    ">": lambda x, y: x > y,
    ">=": lambda x, y: x >= y,
    # Trigonometrics
    "acos": lambda x: math.acos(x),
    "asin": lambda x: math.asin(x),
    "atan": lambda x: math.atan(x),
    "cos": lambda x: math.cos(x),
    "cosh": lambda x: math.cosh(x),
    "sin": lambda x: math.sin(x),
    "sinh": lambda x: math.sinh(x),
    "tanh": lambda x: math.tanh(x),
    # Numeric utilities
    "ceil": lambda x: math.ceil(x),
    "floor": lambda x: math.floor(x),
    "round": lambda x, y: round(x, y),
    "ip": lambda x: x // 1,
    "fp": lambda x: x - x // 1,
    "pos": lambda x: 1 if x >= 0 else 0,
    "abs": lambda x: abs(x),
    "max": lambda x, y: max([x, y]),
    "min": lambda x, y: min([x, y]),
    # More math functions
    "ln": lambda x: math.log(x, math.e),
    "log": lambda x: math.log(x, 10),
    "log_": lambda x, y: math.log(x, y),
    "pow": lambda x, y: x ** y,
}
