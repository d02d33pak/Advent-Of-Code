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


FIND_INDEX = re.compile(r"\[(\d+)\]")

# PART 1
def part1(data):
    """ sum of dict values after masking """

    mask = ""
    result = 0
    mem = dict()
    for line in data:
        if line.startswith("mask"):
            mask = line.split(" = ")[-1]
        else:
            index, value = line.split(" = ")
            index = FIND_INDEX.search(index).group(1)
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


def write_value(address, value, mem):
    """ Recursive helper fn to write values to mem """
    xpos = address.find("X")
    if xpos == -1:
        index = int(address, 2)
        mem[index] = int(value)
    else:
        write_value(address[:xpos] + "0" + address[xpos + 1 :], value, mem)
        write_value(address[:xpos] + "1" + address[xpos + 1 :], value, mem)


# PART 2
def part2(data):
    """ sum of values after masking system 2.0 """

    result = 0
    mem = dict()
    mask = ""

    for line in data:
        if line.startswith("mask"):
            mask = line.split(" = ")[-1]
        else:
            index, value = line.split(" = ")
            index = FIND_INDEX.search(index).group(1)
            address = "{0:b}".format(int(index)).zfill(36)

            new_address = ""
            for i, bit in enumerate(mask):
                if bit == "0":
                    new_address += address[i]
                elif bit == "1":
                    new_address += "1"
                elif bit == "X":
                    new_address += "X"

            write_value(new_address, value, mem)

    for val in mem.values():
        result += val

    return result
