"""
Advent of Code : Day 13
"""

from os import path


def parse_input(filename):
    """ Parse input file values """
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, filename)

    with open(file_path, "r") as file:
        values = file.read().splitlines()
    return values


# PART 1
def part1(notes):
    """ Find bus id that leave at the earliest """
    my_time = int(notes[0])
    bus_ids = notes[1].split(",")
    bus_ids = sorted([int(bus_id) for bus_id in bus_ids if bus_id != "x"])

    min_time = None  # (bus_id, waiting_time)

    for bus in bus_ids:
        if my_time % bus == 0:
            return 0
        else:
            diff = (bus * ((my_time // bus) + 1)) - my_time
            if min_time is None or diff < min_time[1]:
                min_time = (bus, diff)

    return min_time[0] * min_time[1]


# PART 2
def part2(notes):
    """ Check on other criteria """

    # all bus ids are prime number
    # for explanation watch this (https://www.youtube.com/watch?v=4_5mluiXF5I)
    # just an implementation of his solution

    buses = notes[1].split(",")

    step_size = 1
    time = 0

    for index, bus in enumerate(buses):
        if bus == "x":
            continue

        bus = int(bus)
        while True:
            dep_time = time + index
            if dep_time % bus == 0:
                step_size *= bus
                break

            time += step_size

    return time
