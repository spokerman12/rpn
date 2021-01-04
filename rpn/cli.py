#
# cli.py: Provides rpn as you'd expect a UNIX command
#         line interface program to behave.
#

import sys
import os
import traceback
import readline

from .calculator import Calculator


def show_help():
    # Shows help doc

    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/assets/help_doc.txt") as help_doc:
        print(help_doc.read())

def show_operators():
    # Shows operators cheatsheet

    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/assets/operators_doc.txt") as operators_doc:
        print(operators_doc.read())


def interactive_mode(args=None):
    # CLI with infinite loop interface until user inputs
    # 'exit' or stops the program.
    # args is always None unless running tests

    print(
        "\n",
        "| Reverse Polish Notation calculator\n",
        "| - To exit, press Ctrl+C or type 'exit'.\n",
        "| - To show help docs, type 'help'.\n",
        "| \n",
        "| Built with <3 by Daniel Francis (github.com/spokerman12)\n",
    )

    calculator = Calculator()
    last_input = ""
    result = ""
    result_for_display_mode = ""
    while True:
        try:
            rpn_input = read_input() if not args else args

            # First check for CLI-only commands:
            if rpn_input == "exit":
                sys.exit(0)
            elif rpn_input == "help":
                show_help()
                if args:
                    return
            elif rpn_input == "":
                pass
            else:

                # Extract desired display mode first
                calculator_input, display_mode = extract_display_mode(
                    rpn_input, calculator.display_mode
                )

                # Show if display mode changed
                if calculator.display_mode != display_mode:
                    calculator.display_mode = display_mode
                    print(" Switched to:", display_mode)

                # There is still input to process
                if calculator_input:
                    result = calculator.solve(calculator_input)
                    if isinstance(result, int):
                        result_for_display_mode = calculator.display_modes[
                            calculator.display_mode
                        ](result)
                    elif isinstance(result, float):
                        result_for_display_mode = float(str(result))
                    print(result_for_display_mode)

                # Input is fully processed
                else:
                    result_for_display_mode = result
                    print(result_for_display_mode)
            last_input = rpn_input
            if args:
                return result_for_display_mode
        except Exception as e:
            print("  Error:", e)
            print("  Check your syntax (or type 'help' or 'exit')")
            if args:
                return result_for_display_mode


def direct_mode(rpn_input):
    # One-shot CLI interface

    calculator = Calculator()
    calculator_input, display_mode = extract_display_mode(
        rpn_input, calculator.display_mode
    )
    if calculator_input:
        result = calculator.solve(calculator_input)
        result_for_display_mode = calculator.display_modes[display_mode](result)
        if isinstance(str(result), int):
            result_for_display_mode = calculator.display_modes[calculator.display_mode](
                result
            )
        elif isinstance(str(result), float):
            result_for_display_mode = float(str(result))
        return result_for_display_mode  # Depends on mode change. This could change
    else:
        return ''

def launch_cli(args=sys.argv):
    # Main CLI procedure
    # Check out README.md for more detailed info.

    # Display help on help-related arg
    if any(arg in ["help", "-help", "--help", "-h", "--h"] for arg in args):
        show_help()
        sys.exit(0)

    if any(arg in ["operators", "-operators", "--operators", "-o", "--o"] for arg in args):
        show_operators()
        sys.exit(0)    

    # Interactive mode
    elif len(args) == 1:
        try:
            result = interactive_mode()
            sys.exit(0)
        except Exception as e:
            traceback.print_exc()
            sys.exit(1)

    # File read mode
    elif args[1] == "--read":
        line_num = 0
        with open(args[2], "r") as read_file:
            for line in read_file.readlines():
                line_num += 1
                if line != "":
                    new_args = line.strip("\n")
                    try:
                        result = direct_mode(new_args)
                        print(result)  # Depends on mode change. This could change
                    except Exception as e:
                        traceback.print_exc()
                        print("Please check your syntax on line", line_num)
                        return None
                else:
                    continue

    # Direct mode
    else:
        try:
            result = direct_mode(" ".join(args[1:]))
            print(result)  # Depends on mode. This could change
            return result
        except Exception as e:
            traceback.print_exc()
            print("Please check your syntax and possible escaped terminal chars like * and >")
            return None


def extract_display_mode(args, previous_mode):
    # Extracts possible display modes from the arguments
    # and returns a clean input.

    modes = {"--bin": "binary", "--dec": "decimal", "--oct": "oct", "--hex": "hex"}
    new_args = args.split(" ")
    for mode in modes.keys():
        if mode in args:
            display_mode = modes[new_args[new_args.index(mode)]]
            new_args = [operand for operand in new_args if operand not in modes.keys()]
            break
        display_mode = previous_mode
    return (" ".join(new_args), display_mode)


def read_input(pre_typed=""):
    # Makes it so the CLI is editable
    # and can fetch its input history.

    readline.set_startup_hook(lambda: readline.insert_text(pre_typed))
    try:
        rpn_input = input("> ")
    finally:
        readline.set_startup_hook(None)
    return rpn_input
