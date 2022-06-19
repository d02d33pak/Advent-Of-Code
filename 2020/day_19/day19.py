"""
Advent of Code : Day 19
Reference = https://www.youtube.com/watch?v=dgnK4ASzVPU
"""

from os import path
from venv import create


def parse_input(filename):
    """Parse input file values"""
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    with open(file_path, "r") as file:
        rules, messages = file.read().split("\n\n")
        rules = rules.splitlines()
        messages = messages.splitlines()
    return rules, messages


def create_rules_dict(rules):
    """Create a dictionary of all the rules from strings"""
    rules_dict = {}
    for rule in rules:
        key, value = rule.split(": ")
        rules_dict[int(key)] = [val.split() for val in value.split(" | ")]
        # breaking '1 2 | 3 4' to ['1 2', '3 4']
        # and then again breaking '1 2' to ['1', '2'] and '3 4' to ['3', '4']
        # so rules_dict[0] = [['1', '2'], ['3', '4']]
    return rules_dict


solved_rules_dict = {}


def build_zeroth_strings(position, rules_dict):
    """Creating valid string for a position in rules in dict"""
    rule_options = rules_dict[position]

    if ['"a"'] in rule_options:
        return ["a"]
    if ['"b"'] in rule_options:
        return ["b"]

    if position in solved_rules_dict:
        return solved_rules_dict[position]

    valid_string = []
    for options in rule_options:
        sub_options = []
        for rule in options:
            new_sub_options = build_zeroth_strings(int(rule), rules_dict)
            if len(sub_options) == 0:
                sub_options = new_sub_options.copy()
            else:
                combined_options = []
                for sub_option in new_sub_options:
                    for sub_rule in sub_options:
                        combined_options.append(sub_rule + sub_option)
                sub_options = combined_options.copy()

        valid_string += sub_options

    solved_rules_dict[position] = valid_string
    return valid_string


# PART 1
def part1(data):
    """Counting messages that pass Rule 0"""
    rules, messages = data
    rules_dict = create_rules_dict(rules)

    # Converting list to set because "in" operation in set is O(1)
    zeroth_strings = set(build_zeroth_strings(0, rules_dict))

    count = 0
    for message in messages:
        if message in zeroth_strings:
            count += 1

    return count


# PART 2
def part2(data):
    """Check on other criteria"""
    _ = part1(data)

    print(solved_rules_dict[42])
    print(solved_rules_dict[31])

    return 0
