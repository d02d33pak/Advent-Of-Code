"""
Advent of Code : Day 06
"""

from os import path


def parse_input(filename):
    """ Parse input file values """
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    with open(file_path, "r") as file:
        all_group_answers = list()
        group_answers = list()

        for line in file:
            line = line.strip()
            if len(line) > 0:
                group_answers.append(line)
            else:
                if len(group_answers) > 0:
                    all_group_answers.append(group_answers)
                group_answers = list()

        if len(group_answers) > 0:
            all_group_answers.append(group_answers)

    return all_group_answers


# PART 1
def part1(all_groups_answer):
    """ count questions answered 'yes' by anyone """
    anyone_answered = 0
    for group_answers in all_groups_answer:
        common_answers = sorted(set("".join(group_answers)))
        anyone_answered += len(common_answers)
    return anyone_answered


# PART 2
def part2(all_groups_answer):
    """ count questions answered 'yes' by everyone """
    everyone_answered = 0
    for group_answers in all_groups_answer:
        answered = set("abcdefghijklmnopqrstuvwxyz")
        for answer in group_answers:
            # answered = answered.intersection(set(answer))
            answered.intersection_update(set(answer))

        everyone_answered += len(answered)

    return everyone_answered
