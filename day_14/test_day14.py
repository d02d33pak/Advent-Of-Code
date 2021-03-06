"""
Tests for Day 14
"""

from day14 import parse_input, part1, part2


def test_part1():
    """ Test part one """
    assert part1(parse_input("test_input_1.txt")) == 165


def test_part2():
    """ Test part two """
    assert part2(parse_input("test_input_2.txt")) == 208
