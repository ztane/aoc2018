from helpers import *

d = get_aoc_data(day=12)


def run_to(target):
    data = list(d.lines)

    _,_,initial_state = data[0].partition(': ')
    map = {}
    for i in data[1:]:
        source, _, dest = i.partition(' => ')
        map[source] = dest

    state = {i: True for (i, e) in enumerate(initial_state) if e == '#'}

    iteration = 0

    while True:
        new_state = {}
        for i in range(min(state.keys()) - 4, max(state.keys()) + 5):
            vector = ''
            for j in range(-2, 3):
                vector += '.#'[state.get(i + j, False)]

            if map.get(vector) == '#':
                new_state[i] = True

        state_min = min(state.keys())
        new_min = min(new_state.keys())

        if {i - state_min for i in state.keys()} == {i - new_min for i in new_state.keys()}:

            print('converged at iteration', iteration)
            base = sum(new_state.keys())
            increment = base - sum(state.keys())
            print('increment per iteration', increment)
            print('base', base)
            print('end result', base + (target - iteration - 1) * increment)
            break

        state = new_state
        iteration += 1
        if iteration == target:
            return sum(new_state.keys())


def part1():
    return run_to(20)


def part2():
    return run_to(50_000_000_000)
