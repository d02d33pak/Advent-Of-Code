"""
Advent of Code 2021: Day 04
"""

from os import path


def parse_input(filename):
    """Parse input file values"""
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    with open(file_path, "r", encoding="utf-8") as file:
        nums, *grids = file.read().splitlines()

        nums = list(map(int, nums.split(",")))

        boards = []
        for row in grids:
            if row == "":
                new_grid = []
                boards.append(new_grid)
            else:
                new_grid.append(list(map(int, row.split())))

    return nums, boards


def check_bingo(board):
    """Check if board has any bingo row/column"""
    row_sums = list(map(sum, board))
    col_sums = [sum(x) for x in zip(*board)]

    if 0 in row_sums or 0 in col_sums:
        return True

    return False


def sum_of_board(board):
    """Sum of all elements of the board"""
    board_sum = 0
    for row in board:
        for val in row:
            board_sum += val
    return board_sum


# PART 1
def part1(inputs):
    """Find first bingo board and calculate score"""
    nums, boards = inputs
    found = False
    result = 0

    for num in nums:
        if found:
            break
        for board in boards:
            if found:
                break
            for row in board:
                for index, val in enumerate(row):
                    if val == num:
                        row[index] = 0
            if check_bingo(board):
                result = sum_of_board(board) * num
                found = True
                break

    return result


# PART 2
def part2():
    """Part 2"""
    return True
