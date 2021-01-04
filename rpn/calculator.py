#
# calculator.py: The Calculator class that fuels the rpn program.
#
#                You can import just this module and operators.py
#                in your own code.
#
#                Note that this is more of a CLI-oriented
#                reverse Polish notation calculator; so it's not
#                an equivalent of, say, an HP‑35, but it can
#                perform the same operations, maybe even more
#                because this was built to work in UNIX pipelines
#                and in conjunction with other programs.
#
#                More info on its usage on README.md.
#


import re
import math
import os
from collections import deque
from random import seed, random
from .operators import operators


class Calculator:
    def __init__(self, display_mode="decimal", precision=6, log_file=None):

        self.precision = (
            int(os.environ["RPN_PRECISION"])
            if "RPN_PRECISION" in os.environ.keys()
            else precision
        )
        self.display_modes = {
            "binary": lambda x: "0b{0:b}".format(math.ceil(x)),
            "decimal": lambda x: ("{0:." + str(self.precision) + "g}").format(x),
            "oct": lambda x: "0o{0:o}".format(math.ceil(x)),
            "hex": lambda x: "0x{0:x}".format(math.ceil(x)),
        }
        self.storage = 0
        self.stack = []
        self.display_mode = display_mode
        self.log_file = None if not log_file else open(log_file, "w")
        self.implemented_operators = operators
        self.implemented_manipulations = []
        self.implemented_constants = ["e", "pi", "randfloat"]
        self.defined_variables = {}

    def solve(self, rpn_input):
        # Solves an RPN input

        if self.validate_input(rpn_input):
            clean_input = deque([elem for elem in rpn_input.split(" ") if elem != ""])
            result = self.calculate_result(clean_input)
        else:
            raise SyntaxError("Syntax error")
        return result

    def calculate_result(self, valid_input):
        # After the input was parsed, calculates the result

        # Valid input is either [num] or [num, ...]
        result = valid_input.popleft()
        self.stack.append(result)

        if len(valid_input) == 0:
            result = self.interpret_number(result)

        while len(valid_input) != 0:
            operand = valid_input.popleft()
            if self.is_operator(operand):
                try:
                    A = self.stack.pop()
                    result = self.operate(a=A, b=None, op=operand)
                except:
                    B = self.stack.pop()
                    result = self.operate(a=B, b=A, op=operand)
                self.stack.append(str(result))
            else:
                self.stack.append(str(operand))
        return result

    def interpret_number(self, operand):
        # Interprets numbers in different
        # notations and constants

        if self.is_number(operand):
            if self.is_variable(operand):
                result = self.variables(operand)
            else:
                if "." in operand:
                    result = float(operand)
                elif self.is_bin(operand):
                    result = int(operand, 2)
                elif self.is_hex(operand):
                    result = int(operand, 16)
                elif self.is_oct(operand):
                    result = int(operand, 8)
                else:
                    result = int(operand, 10)
        elif self.is_constant(operand):
            result = self.lookup_constant(operand)
        else:
            result = None
        return result

    def operate(self, a, b=None, op=None):
        # Performs the implemented operation

        a_num = self.interpret_number(a)
        if not b and not op:
            result = a_num
        elif b:
            b_num = self.interpret_number(b)
            result = self.implemented_operators[op](a_num, b_num)
        elif not b and op:
            result = self.implemented_operators[op](a_num)
        return result

    def validate_input(self, rpn_input):
        # Determines if an RPN input is valid
        sequence = deque([elem for elem in rpn_input.split(" ") if elem != ""])

        # All elements in input should be valid
        for element in sequence:
            elem_is_valid = any(
                [
                    self.is_number(element),
                    self.is_operator(element),
                    self.is_manipulation(element),
                    self.is_constant(element),
                    self.is_variable(element),
                ]
            )
            if not elem_is_valid:
                return False

        # First element is always a number
        # ...or a manipulation, but we haven't implemented that yet.
        if not (self.is_number(sequence[0]) or self.is_constant(sequence[0])):
            return False

        # Last element is always an operator
        # unless the sequence is just [num]
        elif len(sequence) > 1 and not self.is_operator(sequence[len(sequence) - 1]):
            return False

        return True

    def is_number(self, raw_string):
        string = raw_string.lower()
        is_int = (
            raw_string == "0"
            or bool(re.fullmatch(r"[1-9]+[0-9]*", string))
            or bool(re.fullmatch(r"-[1-9]+[0-9]*", string))
        )
        is_float = bool(re.fullmatch(r"[0-9]+\.{1}[0-9]+", string)) or bool(
            re.fullmatch(r"-[0-9]+\.{1}[0-9]+", string)
        )
        return any(
            [
                is_int,
                is_float,
                self.is_hex(string),
                self.is_bin(string),
                self.is_oct(string),
            ]
        )

    def is_hex(self, string):
        return bool(re.fullmatch(r"0x[a-f0-9]+", string))

    def is_bin(self, string):
        return bool(re.fullmatch(r"0b[0-1]+", string))

    def is_oct(self, string):
        return bool(re.fullmatch(r"0o[0-7]+", string))

    def is_operator(self, string):
        return string in self.implemented_operators.keys()

    def is_manipulation(self, string):
        return string in self.implemented_manipulations

    def is_constant(self, string):
        return string in self.implemented_constants

    def is_variable(self, string):
        return string in self.defined_variables

    def lookup_constant(self, constant):
        seed(1)
        if constant == "e":
            return math.exp(1)
        elif constant == "pi":
            return math.pi
        elif constant == "randfloat":
            from datetime import datetime
            seed(datetime.now())
            return float(random())
        else:
            return 0
