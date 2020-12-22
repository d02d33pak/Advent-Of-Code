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

    while index not in visited:
        visited.add(index)
        opr, val = instructions[index].split()
        val = int(val)

        index = index + val if opr == "jmp" else index + 1

        if opr == "acc":
            accumulator += val

    return accumulator


# PART 2
def part2(instructions):
    """ Find nop, jmp to be swapped """
    print(instructions)
    return 0
