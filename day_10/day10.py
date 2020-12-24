"""
Advent of Code : Day 10
"""

from os import path


def parse_input(filename):
    """ Parse input file values """
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    with open(file_path, "r") as file:
        values = list(map(int, file.read().splitlines()))
    return values


# PART 1
def part1(adapters):
    """ Find adapters with jolt diff of 1 and 3 """
    adapters.sort()
    adapters.insert(0, 0)  # add 0 at start for the wall jolt
    adapters.append(max(adapters) + 3)  # adding phone's inbuilt adapter

    diff_of_one = 0
    diff_of_three = 0
    for i in range(len(adapters) - 1):
        diff = adapters[i + 1] - adapters[i]
        if diff == 1:
            diff_of_one += 1
        elif diff == 3:
            diff_of_three += 1

    return diff_of_one * diff_of_three


# PART 2
# Dynamic Programming
def part2(adapters):
    """ Find all possible combination of adapters """
    adapters.sort()
    adapters.insert(0, 0)  # add 0 at start for the wall jolt
    adapters.append(max(adapters) + 3)  # adding phone's inbuilt adapter

    # memoize already visisted node
    visited = dict()

    def repeat(i):
        if i == len(adapters) - 1:
            return 1
        if i in visited:
            return visited[i]
        answer = 0
        for j in range(i + 1, len(adapters)):
            if adapters[j] - adapters[i] <= 3:
                answer += repeat(j)

        visited[i] = answer

        return answer

    no_of_ways = repeat(0)  # no. of ways to reach the end starting from index 0

    return no_of_ways
