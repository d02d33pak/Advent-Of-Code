"""
Tests for Day 10
"""

from day10 import parse_input, part1, part2


def test_part1_a():
    """ Test part one """
    assert part1(parse_input("test_input1.txt")) == 35


def test_part1_b():
    """ Test part one """
    assert part1(parse_input("test_input2.txt")) == 220


def test_part2_a():
    """ Test part two """
    assert part2(parse_input("test_input1.txt")) == 8


def test_part2_b():
    """ Test part two """
    assert part2(parse_input("test_input2.txt")) == 19208
