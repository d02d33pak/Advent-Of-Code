"""
Advent of Code : Day 07
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
def part1(rules):
    """ Count bags that can fit your bag """
    graph = dict()

    parent = re.compile(r"^(\w+\s\w+)")
    child = re.compile(r"(?:contain|,)\s\d+\s(\w+\s\w+)")

    for rule in rules:
        parent_bag = parent.match(rule).group(1)
        child_bags = child.findall(rule)
        graph[parent_bag] = child_bags

    # this is what graph will look like
    # {
    # "light red": ["bright white bag", "muted yellow"],
    # "bright white": ["shiny gold"] so on...
    # }

    my_bag = "shiny gold"
    found_in = set()

    def fit_my_bag(curr_bag):
        for parent, child in graph.items():
            if len(child) != 0:
                if curr_bag in child:
                    found_in.add(parent)
                    fit_my_bag(parent)

    fit_my_bag(my_bag)
    count = len(found_in)

    return count


# PART 2 : THIS ONE WAS QUITE A HEAD-SCRATCHER
def part2(rules):
    """ Number of bags to be carried within """

    graph = dict()

    parent = re.compile(r"^(\w+\s\w+)")
    child = re.compile(r"(?:contain|,)\s(\d)+\s(\w+\s\w+)")

    for rule in rules:
        parent_bag = parent.match(rule).group(1)
        child_bags = child.findall(rule)
        graph[parent_bag] = child_bags

    # this is what graph will look like
    # {
    #    "light red":
    #    [ ('1', "bright white bag"), ('2', "muted yellow") ],
    #    "bright white":
    #    [ ('1' "shiny gold") ],
    #    so on...
    # }

    my_bag = "shiny gold"

    # BEWARE - RECURSION & GRAPH BELOW

    def count_bags_within(curr_bag):
        count = 0
        for parent_bag, children_bags in graph.items():
            if curr_bag in parent_bag:
                if len(children_bags) == 0:
                    return 1
                else:
                    child_sum = 0
                    for bag in children_bags:
                        return_val = count_bags_within(bag[1])
                        if return_val != 1:
                            count += int(bag[0])  # add the parent bag to the count
                        inside = int(bag[0]) * return_val
                        child_sum += inside
                    count += child_sum

        return count

    sum_of_bags = count_bags_within(my_bag)

    return sum_of_bags
