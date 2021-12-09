"""
Advent of Code : Day 11
"""

from os import path


def parse_input(filename):
    """ Parse input file values """
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    values = list()
    with open(file_path, "r") as file:
        for string in file:
            values.append([char for char in string.strip()])
    return values


def check_adjacents(row, col, seat_map):
    """ Return the no. of adjacent seats occupied """
    occupied = 0
    # ttb = top to bottom, ltr = left to right

    for ttb in range(max(0, row - 1), min(len(seat_map), row + 2)):
        for ltr in range(max(0, col - 1), min(len(seat_map[row]), col + 2)):
            if ltr == col and ttb == row:
                pass
            elif seat_map[ttb][ltr] == "#":
                occupied += 1

    return occupied


def change_seating(old_map, tolerance):
    """ Seat people based on given rule """
    new_map = list()

    for row, _ in enumerate(old_map):
        line = list()
        for col, _ in enumerate(old_map[0]):
            adjacents = (
                check_adjacents(row, col, old_map)
                if tolerance == 4
                else check_new_adjacents(row, col, old_map)
            )
            if old_map[row][col] == "#" and adjacents >= tolerance:
                line.append("L")
            elif old_map[row][col] == "L" and adjacents == 0:
                line.append("#")
            else:
                line.append(old_map[row][col])
        new_map.append(line)

    return new_map


# PART 1
def part1(seat_map):
    """ Count seats occupied """

    old_map = seat_map.copy()
    match = False

    while not match:

        new_map = change_seating(old_map, 4)

        match = True
        for i, _ in enumerate(new_map):
            if new_map[i] != old_map[i]:
                match = False

        old_map = new_map.copy()

    # loop breaks when old map = new map
    # so count seats occupied in new map
    count = 0
    for i, _ in enumerate(new_map):
        for j, _ in enumerate(new_map[0]):
            if new_map[i][j] == "#":
                count += 1

    return count


def check_new_adjacents(row, col, seat_map):
    """ Return the no. of adjacent seats occupied """
    occupied = 0
    # ttb = top to bottom, ltr = left to right

    directions = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
    for direction in directions:
        pos = (col + direction[0], row + direction[1])
        while True:
            if (
                pos[0] < 0
                or pos[0] >= len(seat_map[row])
                or pos[1] < 0
                or pos[1] >= len(seat_map)
            ):
                break
            if seat_map[pos[1]][pos[0]] == "L":
                break
            if seat_map[pos[1]][pos[0]] == "#":
                occupied += 1
                break
            pos = (pos[0] + direction[0], pos[1] + direction[1])

    return occupied


# PART 2
def part2(seat_map):
    """ Count seats occupied with new rules """

    old_map = seat_map.copy()
    match = False

    while not match:

        new_map = change_seating(old_map, 5)

        match = True
        for i, _ in enumerate(new_map):
            if new_map[i] != old_map[i]:
                match = False

        old_map = new_map.copy()

    # loop breaks when old map = new map
    # so count seats occupied in new map
    count = 0
    for i, _ in enumerate(new_map):
        for j, _ in enumerate(new_map[0]):
            if new_map[i][j] == "#":
                count += 1

    return count
