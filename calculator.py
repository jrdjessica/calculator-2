"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    user_input = input('Enter your equation here: ')
    tokens = user_input.split(' ')
    if tokens[0] == 'q':
        break