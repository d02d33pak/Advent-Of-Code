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
    """ Count the number of trees encountered """
    height = len(tree_line)
    width = len(tree_line[0])
    x_coord, y_coord, tree_count = 0, 1, 0

    for line in tree_line[1:height:y_coord]:
        x_coord = (x_coord + 3) % width
        if line[x_coord] == "#":
            tree_count += 1
    return tree_count


# PART 2
def part2(tree_line):
    """ Product of the no. of trees on diff. slopes """
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    height = len(tree_line)
    width = len(tree_line[0])
    product_trees = 1

    for slope in slopes:
        x_coord, y_coord, trees = 0, 0, 0
        while y_coord < height - 1:
            x_coord = (x_coord + slope[0]) % width
            y_coord = y_coord + slope[1]
            if tree_line[y_coord][x_coord] == "#":
                trees += 1

        product_trees *= trees

    return product_trees
