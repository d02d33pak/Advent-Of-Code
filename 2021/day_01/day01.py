"""
Advent of Code 2021 : Day 01
"""

from os import path


def parse_input(filename):
    """Parse input file values"""
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    with open(file_path, "r", encoding="utf-8") as file:
        values = list(map(int, file.read().splitlines()))
    return values


# PART 1
def part1(depths):
    """Count no. of times depth increases"""
    increase_count = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            increase_count += 1
    return increase_count


# PART 2
def part2(depths):
    """Count no. of times sum of depths increases"""
    three_measurement_sum = []
    for i in range(len(depths) - 2):
        three_measurement_sum.append(sum(depths[i : i + 3]))

    return part1(three_measurement_sum)
