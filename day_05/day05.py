"""
Advent of Code : Day 05
"""

from os import path


def parse_input(filename):
    """ Parse input file values """
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    with open(file_path, "r") as file:
        values = file.read().splitlines()
    return values


# PART 1
def part1(boarding_pass):
    """ Find seat id and then largest seat id of all ids """
    max_seat_id = 0

    for seat in boarding_pass:
        rows_range = [0, 127]
        cols_range = [0, 7]

        for i in range(0, 6):
            mid = (rows_range[0] + rows_range[1]) // 2
            if seat[i] == "F":
                rows_range[1] = mid
            elif seat[i] == "B":
                rows_range[0] = mid + 1

        row = rows_range[0] if seat[6] == "F" else rows_range[1]

        for j in range(7, 9):
            mid = (cols_range[0] + cols_range[1]) // 2
            if seat[j] == "L":
                cols_range[1] = mid
            elif seat[j] == "R":
                cols_range[0] = mid + 1

        col = cols_range[0] if seat[9] == "L" else cols_range[1]

        seat_id = row * 8 + col

        max_seat_id = max(seat_id, max_seat_id)

    return max_seat_id


# PART 2
def part2(tree_line):
    """ TODO """
    print(tree_line)
    return 0
