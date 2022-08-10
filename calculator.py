"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    user_input = input('Enter your equation here: ')
    tokens = user_input.split(' ')
    tokens_1 = int(tokens[1])
    tokens_2 = int(tokens[2])
    if tokens[0] == 'q':
        break
    elif tokens[0] == '+':
        print(add(tokens_1, tokens_2))

    