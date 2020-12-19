"""
Tests for Day 02
"""

from day02 import get_input, part1, part2


def test_part1():
    """ Checks for nums in list """
    assert part1(get_input("test_input.txt")) == 2


def test_part2():
    """ Test part two """
    assert part2("test_input.txt") == 1
