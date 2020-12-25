"""
Tests for Day 12
"""

from day12 import parse_input, part1, part2


def test_part1():
    """ Test part one """
    assert part1(parse_input("test_input.txt")) == 25


def test_part2():
    """ Test part two """
    assert part2(parse_input("test_input.txt")) == 0
