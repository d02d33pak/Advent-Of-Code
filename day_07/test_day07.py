"""
Tests for Day 07
"""

from day07 import parse_input, part1, part2


def test_part1():
    """ Test part one """
    assert part1(parse_input("test_input.txt")) == 4


def test_part2():
    """ Test part two """
    assert part2(parse_input("test_input.txt")) == 32


def test_part2_2():
    """ Test part two, diff test input """
    assert part2(parse_input("test_input_2.txt")) == 126
