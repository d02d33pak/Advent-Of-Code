"""
Advent of Code : Day 19
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
def part1(data):
    """ Check Valid Passwords """
    return data


# PART 2
def part2(data):
    """ Check on other criteria """
    return data
