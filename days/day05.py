import string

from helpers import *

d = get_aoc_data(day=5)


def react(polymer):
    l = list(polymer)
    i = 0
    while True:
        if l[i].swapcase() == l[i + 1]:
            del l[i:i + 2]
            if i > 0:
                i -= 1
        else:
            i += 1
        if i >= len(l) - 1:
            break
    return len(l)


def part1():
    return react(d.data)


def part2():
    lenghts = [
        react(d.data.replace(i, '').replace(i.upper(), ''))
        for i in string.ascii_lowercase
    ]
    return min(lenghts)
