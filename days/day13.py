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
                        crossing_turn_directions=cycle((-1j, 1, 1j)),
                        removed=False
                    ))

    first_crash = None
    while True:
        cart_positions = {c.position: c for c in carts}
        carts.sort(key=lambda c: (c.position.imag, c.position.real))

        for c in carts:
            if c.removed:
                continue

            cart_positions.pop(c.position)
            c.position += c.direction

            # crash?
            if c.position in cart_positions:
                if not first_crash:
                    first_crash = c.position

                c.removed = cart_positions.pop(c.position).removed = True
                continue
            else:
                cart_positions[c.position] = c

            if map[c.position] == '/':
                c.direction = complex(-c.direction.imag, -c.direction.real)

            elif map[c.position] == '\\':
                c.direction = complex(c.direction.imag, c.direction.real)

            elif map[c.position] == '+':
                c.direction *= next(c.crossing_turn_directions)

        for c in list(carts):
            if c.removed:
                carts.remove(c)

        if len(carts) <= 1:
            return (coords(first_crash),
                    coords(carts[0].position) if carts else None)
