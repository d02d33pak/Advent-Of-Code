"""
Tests for Day 15
"""

from day15 import part1, part2


def test_part1():
    """ Test part one """
    assert part1([0, 3, 6], 2020) == 436
    assert part1([1, 3, 2], 2020) == 1
    assert part1([2, 1, 3], 2020) == 10
    assert part1([1, 2, 3], 2020) == 27
    assert part1([2, 3, 1], 2020) == 78
    assert part1([3, 2, 1], 2020) == 438
    assert part1([3, 1, 2], 2020) == 1836


def test_part2():
    """ Test part two """
    assert part2([0, 3, 6], 30000000) == 175594
    assert part2([1, 3, 2], 30000000) == 2578
    assert part2([2, 1, 3], 30000000) == 3544142
    assert part2([1, 2, 3], 30000000) == 261214
    assert part2([2, 3, 1], 30000000) == 6895259
    assert part2([3, 2, 1], 30000000) == 18
    assert part2([3, 1, 2], 30000000) == 362
