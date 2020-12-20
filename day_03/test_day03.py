"""
Tests for Day 03
"""

from day03 import parse_input, part1, part2


def test_part1():
    """ Checks for nums in list """
    assert part1(parse_input("test_input.txt")) == 7


def test_part2():
    """ Test part two """
    assert part2(parse_input("test_input.txt")) == 336
