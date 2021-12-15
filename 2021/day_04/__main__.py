"""
Day 4 Main Module
"""

from day04 import parse_input, part1, part2

if __name__ == "__main__":
    # trying out the new walrus[:=] oprtr in python
    if (part := int(input("Enter Part: "))) == 1:
        print(part1(parse_input("input")))
    elif part == 2:
        print(part2(parse_input("input")))
    else:
        print("Wrong choice [1|2]")
