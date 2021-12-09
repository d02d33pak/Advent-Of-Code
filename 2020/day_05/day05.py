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


def find_seat_id(boarding_pass):
    """ To find seat id for the given boarding pass """
    row = find_row(boarding_pass)
    col = find_col(boarding_pass)
    seat_id = row * 8 + col

    return seat_id


def find_row(boarding_pass):
    """ To find row from the boarding pass """
    rows_range = [0, 127]

    for i in range(0, 6):
        mid = (rows_range[0] + rows_range[1]) // 2
        if boarding_pass[i] == "F":
            rows_range[1] = mid
        elif boarding_pass[i] == "B":
            rows_range[0] = mid + 1

    row = rows_range[0] if boarding_pass[6] == "F" else rows_range[1]

    return row


def find_col(boarding_pass):
    """ To find col from boarding pass """
    cols_range = [0, 7]

    for j in range(7, 9):
        mid = (cols_range[0] + cols_range[1]) // 2
        if boarding_pass[j] == "L":
            cols_range[1] = mid
        elif boarding_pass[j] == "R":
            cols_range[0] = mid + 1

    col = cols_range[0] if boarding_pass[9] == "L" else cols_range[1]

    return col


# PART 1
def part1(boarding_list):
    """ Find largest seat id """
    max_seat_id = 0

    for boarding_pass in boarding_list:
        seat_id = find_seat_id(boarding_pass)
        max_seat_id = max(seat_id, max_seat_id)

    return max_seat_id


# PART 2
def part2(boarding_list):
    """ Find your seat id """
    all_seat_ids = list()
    for boarding_pass in boarding_list:
        all_seat_ids.append(find_seat_id(boarding_pass))

    for i in range(max(all_seat_ids)):
        if i not in all_seat_ids:
            seat_id = i

    return seat_id
