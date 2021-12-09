"""
Day 15 Main Module
"""

from day15 import part1, part2

if __name__ == "__main__":
    # trying out the new walrus[:=] oprtr in python
    if (part := int(input("Enter Part: "))) == 1:
        print(part1([9, 19, 1, 6, 0, 5, 4], 2020))
    elif part == 2:
        print(part2([9, 19, 1, 6, 0, 5, 4], 30000000))
    else:
        print("Wrong choice [1|2]")
