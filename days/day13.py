from types import SimpleNamespace

from helpers import *

d = get_aoc_data(day=13)


def part1_and_2():
    map = SparseComplexMap(d.lines)
    carts = []

    for y in range(map.rows):
        for x in range(map.columns):
            p = complex(x, y)
            mark = map[p]
            direction = {
                '^': -1j,
                'v': 1j,
                '<': -1,
                '>': 1
            }.get(mark)

            if direction:
                carts.append(
                    SimpleNamespace(
                        position=p,
                        direction=direction,
                        turn_direction=cycle((-1j, 1, 1j)),
                        removed=False
                    ))

    first_crash = None
    while True:
        current_positions = set([c.position for c in carts])
        carts.sort(key=lambda c: (c.position.imag, c.position.real))

        for i in carts:
            current_positions.discard(i.position)
            i.position += i.direction
            if i.position in current_positions:
                if not first_crash:
                    first_crash = i.position

                for j in list(carts):
                    if j.position == i.position:
                        j.removed = True

                current_positions.discard(i.position)
            else:
                current_positions.add(i.position)

            if map[i.position] == '/':
                cd = i.direction
                i.direction = complex(-cd.imag, -cd.real)

            elif map[i.position] == '\\':
                cd = i.direction
                i.direction = complex(cd.imag, cd.real)

            elif map[i.position] == '+':
                i.direction *= next(i.turn_direction)

        for c in list(carts):
            if c.removed:
                carts.remove(c)

        if len(carts) <= 1:
            return coords(first_crash), coords(carts[0].position) if carts else None
