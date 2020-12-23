"""
Advent of Code : Day 09
"""

from os import path


def parse_input(filename):
    """ Parse input file values """
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    with open(file_path, "r") as file:
        val = list(map(int, file.read().splitlines()))

    return val


def find_pair(target, values):
    """ Return sum pair for target value """
    values = set(values)
    for value in values:
        if target - value in values:
            return True

    return False


# PART 1
def part1(values, window=25):
    """ Find invalid XMAS no. """
    index = 0

    for value in values[window:]:
        if find_pair(value, values[index : (window + index)]):
            index += 1
        else:
            return value

    return -1


# PART 2
def part2(values, window=25):
    """ Solve part two """
    target = part1(values, window)

    sum_, index, offset = 0, 0, 0

    while sum_ != target:
        if sum_ < target:
            sum_ += values[offset + index]
            index += 1
        if sum_ > target:
            offset += 1
            sum_ = 0
            index = 0

    min_of_range = min(values[offset : offset + index])
    max_of_range = max(values[offset : offset + index])

    return min_of_range + max_of_range
