"""
Tests for Day 17
"""

from day17 import parse_input, part1, part2


def test_part1():
    """ Checks for nums in list """
    assert part1(parse_input("test_input.txt")) == 112


def test_part2():
    """ Test part two """
    assert part2(parse_input("test_input.txt")) == 848
