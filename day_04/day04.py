"""
Advent of Code : Day 04
"""

from os import path


def get_input(filename):
    """ Parse input file values """
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    with open(file_path, "r") as file:
        list_of_passports = list()
        passport = dict()

        for line in file:
            line = line.strip()  # to get rid of \n from the string

            if len(line) != 0:
                for entry in line.split(" "):
                    # this is what an entry looks like
                    # ecl:brn pid:760753108 byr:193
                    key, value = entry.split(":")
                    passport[key] = value
            else:
                # if its an empty line
                if len(passport) > 0:
                    list_of_passports.append(passport)
                passport = dict()

        if len(passport) > 0:
            list_of_passports.append(passport)

    return list_of_passports


# PART 1
def part1(list_of_passports):
    """ Find no. of valid passports """
    valid_count = 0
    req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for passport in list_of_passports:
        valid = True
        for field in req_fields:
            if field not in passport:
                valid = False
        if valid:
            valid_count += 1

    return valid_count


# PART 2
def part2(list_of_passports):
    """ Find valid passports based on stricter criteria """
    return 0
