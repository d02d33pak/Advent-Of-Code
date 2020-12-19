"""
Day 1 Main Module
"""

from day01 import get_input, part1, part2

if __name__ == "__main__":
    # trying out the new walrus[:=] oprtr in python
    if (part := input("Enter Part: ")) == 1:
        print(part1(get_input("input.txt")))
    elif part == 2:
        print(part2(get_input("input.txt")))
    else:
        print("Wrong choice [1|2]")
