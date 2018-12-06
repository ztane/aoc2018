from helpers import *

d = get_aoc_data(day=6)


def part1_and_2():
    coords = list(d.parsed('<int>, <int>'))

    min_x = min([x for (x, y) in coords])
    max_x = max([x for (x, y) in coords])
    min_y = min([y for (x, y) in coords])
    max_y = max([y for (x, y) in coords])

    colour_count = Counter()
    infinite = set()
    in_region = 0

    for x in range(min_x - 100, max_x + 100):
        for y in range(min_y - 100, max_y + 100):
            minimum = inf
            for i, (cx, cy) in enumerate(coords):
                new = manhattan(x - cx, y - cy)
                if new < minimum:
                    minimum = new
                    colour = i
                elif new == minimum:
                    colour = -1

            manhattan_sum = sum(manhattan(x - cx, y - cy) for (cx, cy) in coords)
            if manhattan_sum < 10000:
                in_region += 1

            colour_count[colour] += 1
            if colour in infinite:
                continue

            if x in (min_x, max_x) or y in (min_y, max_y):
                infinite.add(colour)

    for k, c in colour_count.most_common():
        if k not in infinite:
            largest = c
            break

    return largest, in_region
