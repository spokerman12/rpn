# Reverse Polish Notation calculator

This is an "Entry RPN (β-type) Reverse Polish Notation (RPN)" calculator built in Python.

## Installation

*Note: This program needs Python 3 and a UNIX-based operating system to run correctly.*

Just run `make install` and, after asking nicely for `sudo`, Makefile will create an `rpn` symlink in your `/usr/local/bin`. This program doesn't need anything out of the Python 3 standard library.

If you want to develop this app, you can do `make requirements`, which will install Black and Pytest. More on developing below in this README.

## Usage

First, to understand RPN, please check the references at the bottom of this document.

This program has 3 modes:
1. **Interactive Mode**: Run `rpn` and you will enter Interactive mode. You can write RPN-styled calculations on your terminal.
2. **Direct Mode**: Run something like `rpn 2 4 +` and the result will be printed to stdout.
3. **File Mode**: Run `rpn --read ~/somefile` and `rpn` will interpret each line as an input to Direct Mode.
4. `rpn` supports printing results in decimal (`--decimal`), binary (`--bin`), octagesimal (`--oct`) and hexadecimal (`--hex`). Just provide the appropiate flag at any point during your input sequence. For example, `rpn 123 53 + 212 \* --bin` and `rpn 123 --bin 53 + 212 \*` both return `0b1001000111000000`
5. You can change `rpn`'s digit precision by changing your `RPN_PRECISION` environmental variable. You can do this by running something like `export RPN_PRECISION=10`
6. If you want to save `rpn`'s output in an external script while using Direct Mode, you can do so with `output=$(rpn 2 2 +)`. Note that this will pick up stderr, so make sure you write some error handling in your pipeline!

- To exit `rpn`, just type `exit`.
- To get a quick rundown of the program, type `help`.
- To show all operators, type `operators`.

## Cool features

- While in Interactive Mode, you can press the arrow keys, like you would in a regular terminal, and cycle through your input history.
- `rpn` takes four types of input. `rpn` **doesn't care what format you write your calculations in**:

```
$ rpn 0x123 0b10101 + 16 \* 0o7 -
4985

$ rpn 291 21 + 16 \* 7 -
4985
```

You can also use `rpn` as a notation converter:
```
$ rpn 0x123 
291

$ rpn 291 --oct
0o443
```

## Limitations

- Remember that the terminal needs some characters to be escaped to behave correctly as arguments to other programs. For `rpn`, this includes '\*','>' and '<'. So, if you'd want to multiply using Direct Mode, you'd do `rpn 3 5 \*`.
- Currently, the display of floating point numbers is only supported in `--decimal` display mode. Displaying floats in any other display mode will force a ceiling operation on the result. For example, `rpn 10 3 /` returns `3.3333333333333334814` but `rpn 10 3 / --bin` returns `0b100`, which is 4.

## Development

This program is modular so that it can be easily built upon. 

- `make tests` runs the unit tests in `rpn/tests` that check the integrity of the outputs.
- In `operators.py` you can see a large dictionary with all the currently available functions. Feel free to add your own! Just make sure to add some tests; precision, data types and other nuisances can cause unexpected results while developing a calculator like this.

Some great additions would be:
- Using the app as a filter in popular unix text editors.
- Implementing variables (the main structure is there, we'd just need to pick up the tokens and store the values)

But variables (and several other suggested features) became less relevant after implementing the input history. A CLI is for sure more powerful than a desktop calculator.

## References

* [Wikipedia: Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)
* [RPN Tutorial](https://hansklav.home.xs4all.nl/rpn/)

## Appendix: All implemented operators and constants

*Note: All of these are implemented using Python3's Math library. Check out their implementation in `operators.py`*

### Constants
- pi: 3.141592653589793116
- e: 2.7182818284590450908
- randfloat: A random floating point number using current time as seed. 

### Arithmetics
- +: X plus Y
- -: X minus Y
- \*: X times Y (Needs escaping in Direct Mode)
- /: X divided by Y
- sqrt: Square root of X
- \*\*: X to the power of Y (Needs escaping in Direct Mode)
- fact: Factorial of X
- not: Negation of X
- !=: X not equals Y
- %: X modulo Y
- ++: Increment X by 1
- --: Decrement X by 1

### Bitwise
- &: X and Y
- |: X or Y
- ^: X XOR Y
- ~: Not X
- <<: Shift X Y bits to the left
- \>\>: Shift X Y bits to the right (Needs escaping in Direct Mode)

### Boolean
- &&: X and Y
- ||: X or Y
- ^^: X XOR Y

### Arithmetic comparison
- <: X kesser than Y 
- <=: X kesser or equal than Y
- ==: X equal to Y
- >: X greater than Y (Needs escaping in Direct Mode)
- >=: X greater or equal than Y (Needs escaping in Direct Mode)

### Trigonometrics
- acos: arc Cosine of X
- asin: arc Sine of X
- atan: arc Tangent of X
- cos: Cosine of X
- cosh: Hyperbolic Cosine of X
- sin: Sine of X
- sinh: Hyperbolic Sine of X
- tanh: Hyperbolic Tangent of X

### Numeric utilities
- ceil: Ceiling of X
- floor: Floor of X
- round: Round float X by Y digits
- ip: Integer part of X
- fp: Floating part of X
- pos: Is X positive?
- abs: Absolute of X
- max: Max of [X,Y]
- min: Min of [X,Y]

### More math functions
- ln: Base e logarithm of X
- log: Base 10 logarithm of X
- log_: Base X logarithm of Y
- pow: X to the power of Y (some people prefer this one)