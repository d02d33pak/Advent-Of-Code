"""
Advent of Code : Day 18
"""

from os import path


def parse_input(filename):
    """ Parse input file values """
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    with open(file_path, "r") as file:
        values = file.read().splitlines()
    return values


def do_operation(operators, operands):
    """ Perform an operation (+ or *) on operands """
    second = operands.pop()
    first = operands.pop()
    operation = operators.pop()
    result = str(eval(first + operation + second))
    return result


# PART 1
# Solved using 2 stacks, 1 stack for operations, 1 stack for operands #
def part1(data):
    """ Sum of all operation's result """
    sum_of_operations = 0

    for line in data:
        operands = []
        operators = []

        for char in line:
            if char not in ("+", "*", "(", ")", " "):
                operands.append(char)

            elif char in ("+", "*"):
                if len(operators) == 0 or operators[-1] == "(":
                    operators.append(char)
                else:
                    result = do_operation(operators, operands)
                    operands.append(result)
                    operators.append(char)

            elif char == "(":
                operators.append(char)

            elif char == ")":
                result = do_operation(operators, operands)
                operands.append(result)
                _ = operators.pop()  # popping the opening bracket

        if len(operators) != 0:
            result = do_operation(operators, operands)
            operands.append(result)

        sum_of_operations += int(operands[0])  # sum of results on each line

    return sum_of_operations


# PART 2
def part2(data):
    """ Evaluate based on operator order """
    sum_of_operations = 0

    for line in data:
        operands = []
        operators = []

        for char in line:
            if char not in ("+", "*", "(", ")", " "):
                operands.append(char)

            elif char in ("+", "*"):
                if len(operators) == 0 or operators[-1] == "(":
                    operators.append(char)
                else:
                    # ADDED FOR PART 2 - PERFORM + BEFORE *
                    if char == "+" and operators[-1] == "*":
                        operators.append(char)
                    else:
                        result = do_operation(operators, operands)
                        operands.append(result)
                        operators.append(char)

            elif char == "(":
                operators.append(char)

            elif char == ")":
                while operators[-1] != "(":
                    result = do_operation(operators, operands)
                    operands.append(result)
                _ = operators.pop()  # popping the opening bracket

        while len(operators) != 0:
            result = do_operation(operators, operands)
            operands.append(result)

        sum_of_operations += int(operands[0])  # sum of results on each line

    return sum_of_operations
