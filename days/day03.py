from helpers import *

d = get_aoc_data(day=3)


def part1():
    map = {}
    dupes = 0
    for n, x, y, w, h in d.parsed('#<int> @ <int>,<int>: <int>x<int>'):
        for x1 in range(x, x + w):
            for y1 in range(y, y + h):
                if (x1, y1) in map:
                    if map.get((x1, y1)) == 1:
                        dupes += 1
                        map[x1, y1] = 2
                else:
                    map[x1, y1] = 1

    return dupes


def part2():
    map = {}
    not_overlapped = set()
    for n, x, y, w, h in d.parsed('#<int> @ <int>,<int>: <int>x<int>'):
        not_overlapped.add(n)
        for x1 in range(x, x + w):
            for y1 in range(y, y + h):
                if (x1, y1) in map:
                    not_overlapped.discard(n)
                    not_overlapped.discard(map[x1, y1])
                else:
                    map[x1, y1] = n

    return scalar(not_overlapped)
