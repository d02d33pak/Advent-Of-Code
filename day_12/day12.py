"""
Advent of Code : Day 12
"""

import re
from os import path


def parse_input(filename):
    """ Parse input file values """
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    with open(file_path, "r") as file:
        values = list()
        for line in file:
            values.append(re.match(r"^(\w)(\d+)$", line.strip()).groups())
    return values


# PART 1
def part1(instructions):
    """ Find Manhattan distance """

    curr_dir = "E"
    turns = ["E", "S", "W", "N"]
    direction = dict()
    direction["E"] = 0
    direction["W"] = 0
    direction["N"] = 0
    direction["S"] = 0

    for instruction in instructions:
        cmd, val = instruction[0], int(instruction[1])

        if cmd in ("E", "S", "W", "N"):
            direction[cmd] += val
        elif cmd == "F":
            direction[curr_dir] += val
        elif cmd == "R":
            curr_dir = turns[(turns.index(curr_dir) + (val // 90)) % 4]
        elif cmd == "L":
            curr_dir = turns[(turns.index(curr_dir) - (val // 90)) % 4]

    east_west = abs(direction["E"] - direction["W"])
    north_south = abs(direction["N"] - direction["S"])

    return east_west + north_south


# PART 2
def part2(instructions):
    """ Solve Part two """

    print(instructions)

    return 0
