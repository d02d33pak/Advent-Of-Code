"""
Advent of Code : Day 17
"""

from os import path


def parse_input(filename):
    """ Parse input file values """
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    with open(file_path, "r") as file:
        values = file.read().splitlines()
    return values


# Util functions
def get_active_cubes(lines, quad=False):
    """ Return coordinates of active cubes """
    active_cubes = []

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                if quad:
                    active_cubes.append([i, j, 0, 0])
                else:
                    active_cubes.append([i, j, 0])

    return active_cubes


def get_neighbours(cube, quad=False):
    """ Get all 26 neighbour coordinates of given cube """
    neighbours = []
    if quad:
        cube_x, cube_y, cube_z, cube_w = cube
    else:
        cube_x, cube_y, cube_z = cube

    for delta_x in range(-1, 2):  # to iterate over -1, 0 and 1
        for delta_y in range(-1, 2):
            for delta_z in range(-1, 2):
                if quad:
                    for delta_w in range(-1, 2):
                        neighbours.append(
                            [
                                cube_x + delta_x,
                                cube_y + delta_y,
                                cube_z + delta_z,
                                cube_w + delta_w,
                            ]
                        )
                else:
                    neighbours.append(
                        [cube_x + delta_x, cube_y + delta_y, cube_z + delta_z]
                    )

    # cube itself isn't its neighbour
    if quad:
        neighbours.remove([cube_x, cube_y, cube_z, cube_w])
    else:
        neighbours.remove([cube_x, cube_y, cube_z])

    return neighbours


# PART 1
def part1(data):
    """ Count active cubes in 3-D """

    active_cubes = get_active_cubes(data)

    for _ in range(6):
        new_active_cubes = []
        to_be_activated = {}

        for cube in active_cubes:
            count = 0
            neighbours = get_neighbours(cube)

            for neighbour in neighbours:
                if neighbour in active_cubes:
                    count += 1
                else:
                    if str(neighbour) not in to_be_activated:
                        to_be_activated[str(neighbour)] = 0
                    to_be_activated[str(neighbour)] += 1

            if count in (2, 3):  # is either 2 or 3
                new_active_cubes.append(cube)

        for inactive in to_be_activated:
            if to_be_activated[inactive] == 3:
                new_active_cubes.append(eval(inactive))

        active_cubes = new_active_cubes

    return len(active_cubes)


# PART 2
def part2(data):
    """ Count active cubes in 4-D """

    active_cubes = get_active_cubes(data, quad=True)

    for _ in range(6):
        new_active_cubes = []
        to_be_activated = {}

        for cube in active_cubes:
            count = 0
            neighbours = get_neighbours(cube, quad=True)

            for neighbour in neighbours:
                if neighbour in active_cubes:
                    count += 1
                else:
                    if str(neighbour) not in to_be_activated:
                        to_be_activated[str(neighbour)] = 0
                    to_be_activated[str(neighbour)] += 1

            if count in (2, 3):  # is either 2 or 3
                new_active_cubes.append(cube)

        for inactive in to_be_activated:
            if to_be_activated[inactive] == 3:
                new_active_cubes.append(eval(inactive))

        active_cubes = new_active_cubes

    return len(active_cubes)
