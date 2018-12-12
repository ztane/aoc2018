import numpy

from helpers import *

d = get_aoc_data(day=10)


def part1():
    particles = []
    speeds = []
    for x, y, dx, dy in d.parsed('position=<<<int>, <int>> velocity=<<<int>, <int>>'):
        particles.append((x, y))
        speeds.append((dx, dy))

    p = numpy.array(particles)
    s = numpy.array(speeds)

    prev_norm = inf
    prev_p = p
    i = 0

    while True:
        i += 1
        norm1 = numpy.max(p[:, 1]) - numpy.min(p[:, 1])
        if norm1 > prev_norm:
            print(i)
            break

        prev_norm = norm1
        prev_p = p
        p += s

    min_vec = prev_p.min(0)
    print(min_vec)
    coords = (prev_p - min_vec)

    max_vec = coords.max(0) + numpy.array([1, 1])
    image = numpy.zeros(tuple(max_vec))
    print(image.shape)

    for x, y in coords:
        image[x, y] = 255

    from matplotlib import pyplot as plt
    plt.imshow(image, interpolation='nearest')
    plt.show()



def part2():
    pass