from helpers import *

d = get_aoc_data(day=1)


def part1():
    return sum(d.extract_ints)


def part2():
    freq = 0
    seen = {0}

    for i in cycle(d.extract_ints):
        freq += i
        if freq in seen:
            return freq

        seen.add(freq)
