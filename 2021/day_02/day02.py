"""
Advent of Code 2021: Day 02
"""

from os import path


def parse_input(filename):
    """Parse input file values"""
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    with open(file_path, "r", encoding="utf-8") as file:
        values = file.read().splitlines()
    return values


# PART 1
def part1(course):
    """Find the end position of the submarine"""
    depth, horizontal = 0, 0
    for value in course:
        command, unit = value.split(" ")
        if command == "forward":
            horizontal += int(unit)
        elif command == "up":
            depth -= int(unit)
        else:
            depth += int(unit)
    return horizontal * depth


# PART 2
def part2(course):
    """Find the end position of the submarine"""
    aim, depth, horizontal = 0, 0, 0
    for value in course:
        command, unit = value.split(" ")
        if command == "forward":
            horizontal += int(unit)
            depth += aim * int(unit)
        elif command == "up":
            aim -= int(unit)
        else:
            aim += int(unit)
    return horizontal * depth
