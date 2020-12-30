"""
Advent of Code : Day 15
"""


# PART 1
def part1(num_list, limit):
    """ Find 2020th num """
    last_index = dict()

    for i, num in enumerate(num_list[:-1]):
        last_index[num] = i

    while len(num_list) < limit:
        prev_num = num_list[-1]
        prev_occ = last_index.get(prev_num, -1)
        last_index[prev_num] = len(num_list) - 1
        if prev_occ == -1:
            num_list.append(0)
        else:
            num_list.append(last_index[prev_num] - prev_occ)

    return num_list[-1]


# PART 2
def part2(num_list, limit):
    """ Find something """

    return part1(num_list, limit)
