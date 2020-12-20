"""
Advent of Code : Day 04
"""

import re
from os import path


def parse_input(filename):
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
    valid_count = 0
    req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    year_pattern = re.compile(r"^(\d{4})$")
    hgt_pattern = re.compile(r"^(\d+)(cm|in)$")
    hcl_pattern = re.compile(r"^#[0-9a-f]{6}$")
    ecl_pattern = re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$")
    pid_pattern = re.compile(r"^(\d{9})$")

    for passport in list_of_passports:
        valid = True
        for field in req_fields:
            if field in passport:
                if field == "byr":
                    match = year_pattern.match(passport[field])
                    if match:
                        if int(match.group(1)) not in range(1920, 2002 + 1):
                            valid = False
                    else:
                        valid = False

                elif field == "iyr":
                    match = year_pattern.match(passport[field])
                    if match:
                        if int(match.group(1)) not in range(2010, 2020 + 1):
                            valid = False
                    else:
                        valid = False

                elif field == "eyr":
                    match = year_pattern.match(passport[field])
                    if match:
                        if int(match.group(1)) not in range(2020, 2030 + 1):
                            valid = False
                    else:
                        valid = False

                elif field == "hgt":
                    match = hgt_pattern.match(passport[field])
                    if match:
                        if match.group(2) == "cm":
                            if int(match.group(1)) not in range(150, 193 + 1):
                                valid = False
                        elif match.group(2) == "in":
                            if int(match.group(1)) not in range(59, 76 + 1):
                                valid = False
                        else:
                            valid = False
                    else:
                        valid = False

                elif field == "hcl":
                    match = hcl_pattern.match(passport[field])
                    if not match:
                        valid = False

                elif field == "ecl":
                    match = ecl_pattern.match(passport[field])
                    if not match:
                        valid = False

                elif field == "pid":
                    match = pid_pattern.match(passport[field])
                    if not match:
                        valid = False
            else:
                valid = False

        if valid:
            valid_count += 1

    return valid_count
