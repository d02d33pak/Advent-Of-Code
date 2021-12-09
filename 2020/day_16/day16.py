"""
Advent of Code : Day 16
"""

import re
from os import path


def parse_input(filename):
    """ Parse input file values """
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    re_fields = re.compile(r"^(\w+\s*\w+): (\d+)-(\d+) or (\d+)-(\d+)$")

    with open(file_path, "r") as file:
        lines = file.read().splitlines()

    attributes = {}
    tickets = []

    for line in lines:
        if "or" in line:
            fields = re_fields.search(line)
            attributes[fields.group(1)] = [
                (int(fields.group(2)), int(fields.group(3))),
                (int(fields.group(4)), int(fields.group(5))),
            ]

        elif "," in line:
            tickets.append([int(x) for x in line.split(",")])

    return [attributes, tickets]


def is_ticket_valid(ticket, attr):
    """
    Util fn to check if ticket is valid
    based on given attribute's ranges
    """
    sum_invalid = 0
    ticket_valid = True

    for value in ticket:
        is_invalid = True

        for _, ranges in attr.items():
            low1, high1 = ranges[0][0], ranges[0][1] + 1
            low2, high2 = ranges[1][0], ranges[1][1] + 1

            if value in range(low1, high1) or value in range(low2, high2):
                is_invalid = False
                break

        if is_invalid:
            sum_invalid += value
            ticket_valid = False

    return ticket_valid, sum_invalid


# ----------------------------------------------
#  Data is split in 2 parts:
#  0. Dictionary of attributes and their ranges
#  1. List of lists of values on a tickets
# ----------------------------------------------

# PART 1
def part1(data):
    """ Sum on invalid values in nearby tickets """

    attr = data[0]
    tickets = data[1]

    sum_invalid = 0

    for ticket in tickets:
        _, sum_per_ticket = is_ticket_valid(ticket, attr)
        sum_invalid += sum_per_ticket

    return sum_invalid


# PART 2
def part2(data):
    """ Check on other criteria """

    attr = data[0]
    tickets = data[1]

    valid_tickets = []

    for ticket in tickets:
        valid_ticket, _ = is_ticket_valid(ticket, attr)
        if valid_ticket:
            valid_tickets.append(ticket)

    possible_col = {}  # dict to hold possible col for each field/attr/rule

    for field, ranges in attr.items():
        low1, high1 = ranges[0][0], ranges[0][1] + 1
        low2, high2 = ranges[1][0], ranges[1][1] + 1
        valid_col = []

        for i in range(20):
            all_pass = True

            for ticket in valid_tickets:
                value = ticket[i]

                if value not in range(low1, high1) and value not in range(low2, high2):
                    all_pass = False
                    break

            if all_pass:
                valid_col.append(i)

        possible_col[field] = valid_col

    fixed_col = {}  # dict to hold confirmed col for each field/attr/rule

    while len(fixed_col) < 20:
        fixed_field = {
            key: value[0] for key, value in possible_col.items() if len(value) == 1
        }
        [(key, value)] = fixed_field.items()  # only contain 1 key-pair value
        fixed_col[key] = value

        for value_list in possible_col.values():
            if value in value_list:
                value_list.remove(value)

    product_of_departure = 1
    for key, value in fixed_col.items():
        if key.startswith("departure"):
            product_of_departure *= valid_tickets[0][value]

    return product_of_departure
