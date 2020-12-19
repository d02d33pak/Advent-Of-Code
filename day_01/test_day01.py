"""
Tests for Day 01
"""

from day01 import get_input, part1, part2


def test_part1():
    """ Checks for nums in list """
    assert part1(get_input("test_input.txt")) == 514579


def test_part2():
    """ Test part two """
    assert part2("test_input.txt") == 241861950
