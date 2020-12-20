"""
Day 4 Main Module
"""

from day04 import get_input, part1, part2

if __name__ == "__main__":
    # trying out the new walrus[:=] oprtr in python
    if (part := int(input("Enter Part: "))) == 1:
        print(part1(get_input("input.txt")))
    elif part == 2:
        print(part2(get_input("input.txt")))
    else:
        print("Wrong choice [1|2]")
