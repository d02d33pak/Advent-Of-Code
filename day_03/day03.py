"""
Advent of Code : Day 03
"""

from os import path


def get_input(filename):
    """ Parse input file values """
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    with open(file_path, "r") as file:
        values = file.read().splitlines()
    return values


# PART 1
def part1(tree_line):
    """ Check Valid Passwords """
    x_val, tree_count = 0, 0
    for line in tree_line[1:]:
        x_val = (x_val + 3) % len(line)
        if line[x_val] == "#":
            tree_count += 1
    return tree_count


# PART 2
def part2(tree_line):
    """ Check on other criteria """
    print(tree_line)
