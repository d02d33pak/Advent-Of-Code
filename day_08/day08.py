"""
Advent of Code : Day 08
"""

from os import path


def parse_input(filename):
    """ Parse input file values """
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    with open(file_path, "r") as file:
        values = file.read().splitlines()
    return values


# PART 1
def part1(instructions):
    """ Find accumulator before bootloop """

    index = 0
    accumulator = 0
    visited = set()

    while index not in visited and index < len(instructions):
        visited.add(index)
        opr, val = instructions[index].split()

        index = index + int(val) if opr == "jmp" else index + 1

        if opr == "acc":
            accumulator += int(val)

    return accumulator


def not_infinite(instructions):
    """ check if loop is infinite """
    index = 0
    visited = set()

    while (index not in visited) and (index < len(instructions)):
        visited.add(index)
        opr, val = instructions[index].split()
        index = index + int(val) if opr == "jmp" else index + 1

    if index == len(instructions):
        return True

    return False


# PART 2
def part2(instructions):
    """ Find nop, jmp to be swapped """
    index = 0
    accumulator = 0
    while index < len(instructions):

        found = False

        instruction = instructions[index]
        opr, val = instruction.split()

        if opr == "nop":
            new_instructions = instructions.copy()
            new_instructions[index] = "jmp " + val
            found = True
        elif opr == "jmp":
            new_instructions = instructions.copy()
            new_instructions[index] = "nop " + val
            found = True

        if found:
            if not_infinite(new_instructions):
                accumulator = part1(new_instructions)
                break

        index += 1

    return accumulator
