"""
Advent of Code 2021: Day 03
"""

from os import path


def parse_input(filename):
    """Parse input file values"""
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    with open(file_path, "r", encoding="utf-8") as file:
        values = file.read().splitlines()
    return values


# PART 1
def part1(report):
    """Calculate Power Consumption"""

    gamma_number, epsilon_number = "", ""

    for i in range(len(report[0])):
        zero_count, one_count = 0, 0

        for number in report:
            if number[i] == "0":
                zero_count += 1
            else:
                one_count += 1

        if zero_count > one_count:
            gamma_number += "0"
            epsilon_number += "1"
        else:
            gamma_number += "1"
            epsilon_number += "0"

    gamma = int(gamma_number, 2)
    epsilon = int(epsilon_number, 2)

    return gamma * epsilon


# PART 2
def part2(report):
    """Calculate Life Support Rating"""

    oxygen_report = co2_report = report

    for i in range(len(report[0])):
        zero_count, one_count = 0, 0
        for number in oxygen_report:
            if number[i] == "0":
                zero_count += 1
            else:
                one_count += 1

        if zero_count > one_count:
            oxygen_report = [num for num in oxygen_report if num[i] == "0"]
        else:
            oxygen_report = [num for num in oxygen_report if num[i] == "1"]

        if len(oxygen_report) == 1:
            break

    for i in range(len(report[0])):
        zero_count, one_count = 0, 0
        for number in co2_report:
            if number[i] == "0":
                zero_count += 1
            else:
                one_count += 1

        if one_count >= zero_count:
            co2_report = [num for num in co2_report if num[i] == "0"]
        else:
            co2_report = [num for num in co2_report if num[i] == "1"]

        if len(co2_report) == 1:
            break

    oxygen_rating = int(oxygen_report[0], 2)
    co2_rating = int(co2_report[0], 2)

    return oxygen_rating * co2_rating
