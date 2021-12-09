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
    turns = ["E", "S", "W", "N"]  # ordered direction-wise
    direction = {"E": 0, "W": 0, "N": 0, "S": 0}

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

    ship_x, ship_y = 0, 0
    way_x, way_y = 10, 1  # +ve = East, North : -ve = West, South

    for instruction in instructions:
        cmd, val = instruction[0], int(instruction[1])

        if cmd == "E":
            way_x += val
        elif cmd == "W":
            way_x -= val
        elif cmd == "N":
            way_y += val
        elif cmd == "S":
            way_y -= val
        elif cmd == "L":
            for _ in range(val // 90):
                way_x, way_y = -way_y, way_x
        elif cmd == "R":
            for _ in range(val // 90):
                way_x, way_y = way_y, -way_x
        elif cmd == "F":
            ship_x += val * way_x
            ship_y += val * way_y

    return abs(ship_x) + abs(ship_y)
