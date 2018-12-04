from helpers import *

d = get_aoc_data(day=2)


def part1():
    twos = threes = 0

    for i in d.lines:
        c = Counter(i)
        if 2 in c.values():
            twos += 1

        if 3 in c.values():
            threes += 1

    return twos * threes


def part2():
    seen = set()

    length_range = range(len(d.lines[0]))

    for w in d.lines:
        for j in length_range:
            # use a tuple here to avoid unnecessary string creation
            parts = w[:j], w[j + 1:]
            if parts in seen:
                return ''.join(parts)
            else:
                seen.add(parts)
