"""
Advent of Code : Day 01
"""

from itertools import combinations
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
    """ Two Sum """
    for num in list_of_nums:
        if 2020 - num in list_of_nums:
            return num * (2020 - num)
    return -1


# PART 2
def part2(list_of_nums):
    """ Three Sum """
    comb = set(combinations(list_of_nums, 2))

    for val1, val2 in comb:
        # trying out the new walrus[:=] oprtr in python
        if (diff := 2020 - val1 - val2) in list_of_nums:
            return val1 * val2 * diff
    return -1
