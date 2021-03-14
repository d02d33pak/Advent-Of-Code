"""
Advent of Code : Day 16
"""

import re
from os import path


def parse_input(filename):
    """ Parse input file values """
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    re_fields = re.compile(r"^(\w+\s*\w+): (\d+)-(\d+) or (\d+)-(\d+)$")

    with open(file_path, "r") as file:
        lines = file.read().splitlines()

    attributes = {}
    tickets = []

    for line in lines:
        if "or" in line:
            fields = re_fields.search(line)
            attributes[fields.group(1)] = [
                (int(fields.group(2)), int(fields.group(3))),
                (int(fields.group(4)), int(fields.group(5))),
            ]

        elif "," in line:
            tickets.append([int(x) for x in line.split(",")])

    return [attributes, tickets]


# ----------------------------------------------
#  Data is split in 2 parts:
#  0. Dictionary of attributes and their ranges
#  1. List of lists of values on a tickets
# ----------------------------------------------

# PART 1
def part1(data):
    """ Check Valid Passwords """

    attr = data[0]
    tickets = data[1]

    sum_invalid = 0

    for ticket in tickets:
        for value in ticket:
            is_invalid = True

            for _, ranges in attr.items():
                low1, high1 = ranges[0][0], ranges[0][1]
                low2, high2 = ranges[1][0], ranges[1][1]

                if value in range(low1, high1) or value in range(low2, high2):
                    is_invalid = False
                    break

            if is_invalid:
                sum_invalid += value

    return sum_invalid


# PART 2
def part2(data):
    """ Check on other criteria """

    print(data)

    return 0
