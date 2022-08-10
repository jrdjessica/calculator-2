"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    user_input = input('Enter your equation here: ')
    tokens = user_input.split(' ')
    if len(tokens) == 3:
        tokens_1 = float(tokens[1])
        tokens_2 = float(tokens[2])
    elif len(tokens) == 2:
        tokens_1 = float(tokens[1])

    if tokens[0] == 'q':
        break
    elif tokens[0] == '+':
        print(add(tokens_1, tokens_2))
    elif tokens[0] == "-":
        print(subtract(tokens_1, tokens_2))
    elif tokens[0] == '*':
        print(multiply(tokens_1, tokens_2))
    elif tokens[0] == '/':
        print(divide(tokens_1, tokens_2))
    elif tokens[0] == 'square':
        print(square(tokens_1))
    elif tokens[0] == 'cube':
        print(cube(tokens_1))
    elif tokens[0] == 'pow':
        print(power(tokens_1, tokens_2))
    elif tokens[0] == 'mod':
        print(mod(tokens_1, tokens_2))