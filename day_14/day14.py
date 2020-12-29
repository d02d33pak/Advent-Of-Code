"""
Advent of Code : Day 14
"""

import re
from os import path


def parse_input(filename):
    """ Parse input file values """
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    with open(file_path, "r") as file:
        values = file.read().splitlines()

    return values


# PART 1
def part1(data):
    """ sum of dict values after masking """

    find_index = re.compile(r"\[\d+\]")

    mask = ""
    result = 0
    mem = dict()
    for line in data:
        if line.startswith("mask"):
            mask = line.split(" = ")[-1]
        else:
            index, value = line.split(" = ")
            index = find_index.search(index).group(0)
            bin_value = "{0:b}".format(int(value)).zfill(36)

            new_bin_value = ""
            for i, bit in enumerate(mask):
                if bit == "X":
                    new_bin_value += bin_value[i]
                else:
                    new_bin_value += bit
            mem[index] = int(new_bin_value, 2)

    for val in mem.values():
        result += val

    return result


# PART 2
def part2(data):
    """ remaining values after masking """
    print(data)
