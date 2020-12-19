"""
Advent of Code : Day 02
"""

import re
from os import path


def get_input(filename):
    """ Parse input file values """
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    with open(file_path, "r") as file:
        values = file.read().splitlines()
    return values


# PART 1
def part1(password_entries):
    """ Check Valid Passwords """
    result = 0

    ### solution version 1 ###

    # for entry in password_entries:
    #     minmax, char, password = entry.split()
    #     minmax = list(map(int, minmax.split("-")))  # "1-3" => [1, 3]
    #     char = char[0]  # a: => a
    #     count = password.count(char)
    #     if minmax[0] <= cound <= minmax[1]:
    #     result += 1

    ### alternate solution using regex ###
    match_grps = list()
    for entry in password_entries:
        # this is what an entry looks like [1-3 a: aabcc]
        ### NORMAL CAPTURE GROUPS
        match = re.match(r"^(\d+)-(\d+)\s(\w):\s(\w+)$", entry)
        match_grps.append(match.groups())

    for match in match_grps:
        count = match[3].count(match[2])
        if int(match[0]) <= count <= int(match[1]):
            result += 1

    return result


# PART 2
def part2(password_entries):
    """ Check on other criteria """
    result = 0

    ### solution version 1 ###

    # for entry in password_entries:
    #     indices, char, password = entry.split()
    #     indices = set(map(int, indices.split("-")))  # "1-3" => [1, 3]
    #     char = char[0]  # a: => a
    #     char_indices = {i + 1 for i, ch in enumerate(password) if ch == char}
    #     if len(indices.intersection(char_indices)) == 1:
    #         result += 1

    match_grps = list()
    for entry in password_entries:
        # this is what an entry looks like [1-3 a: aabcc]
        ### NAMED CAPTURE GROUPS
        match = re.match(
            r"^(?P<min_>\d+)-(?P<max_>\d+)\s(?P<char>\w):\s(?P<password>\w+)$", entry
        )
        match_grps.append(match.groupdict())

    for match in match_grps:
        occurrence = 0
        # if char exists at either of the 2 given indices
        if match["char"] == match["password"][int(match["min_"]) - 1]:
            occurrence += 1
        if match["char"] == match["password"][int(match["max_"]) - 1]:
            occurrence += 1
        if occurrence == 1:
            result += 1

    return result
