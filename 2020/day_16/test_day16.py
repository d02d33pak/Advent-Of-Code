"""
Tests for Day 16
"""

from day16 import parse_input, part1


def test_part1():
    """ Checks for nums in list """
    assert part1(parse_input("test_input.txt")) == 71
