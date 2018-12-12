from helpers import *

d = get_aoc_data(day=11)


def part1():
    def power(x, y):
        rack_id = x + 10
        power_level = rack_id * y
        power_level += serial
        power_level *= rack_id
        power_level = (power_level // 100) % 10 - 5
        return power_level

    serial = 8
    assert power(3, 5) == 4
    serial = 57
    assert power(122, 79) == -5

    serial, = d.extract_ints
    map = SparseMap(default=power)

    # serial = 18
    #
    # coords = []
    # for x in range(1, 301):
    #     print(x)
    #     for y in range(1, 301):
    #         p = 0
    #         for z in range(1, 302 - max(x, y)):
    #             for dx in range(z):
    #                 for dy in range(z):
    #                     p += map[x + dx, y + dy]
    #         coords.append((p, x, y, z))

    def power_from_top(x, y):
        if y <= 0:
            return 0

        return power(x, y) + top_map[x, y - 1]

    import sys
    sys.setrecursionlimit(10000)
    coords = []
    top_map = SparseMap(default=power_from_top)
    for x in range(1, 301):
        print(x)
        for y in range(1, 301):
            for z in range(1, 30): # - max(x, y)):
                p = 0
                for dx in range(z):
                    p += top_map[x + dx, y + z - 1] - top_map[x + dx, y - 1]

                coords.append((p, x, y, z))

    return max(coords)


def part2():
    ...
