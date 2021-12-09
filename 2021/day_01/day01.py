"""
Advent of Code : Day 01
"""

from os import path


def parse_input(filename):
    """ Parse input file values """
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    with open(file_path, "r") as file:
        values = set(map(int, file.read().splitlines()))
    return values


# PART 1
def part1(list_of_nums):
    """ Part 1 """
    return True


# PART 2
def part2(list_of_nums):
    """ Part 2 """
    return True
