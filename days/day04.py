from helpers import *

d = get_aoc_data(day=4)

shift = Parser('<str> Guard #<int> begins shift')
asleep = Parser('<str>:<int>] falls asleep')
wakes_up = Parser('<str>:<int>] wakes up')


def part1_and_2():
    guard_sleeps = defaultdict(Counter)
    current_guard = Counter()

    sleep_started = 0
    for i in sorted(d.lines):
        if shift(i):
            _, guard = shift
            current_guard = guard_sleeps[guard]

        elif asleep(i):
            _, minute = asleep
            sleep_started = minute

        elif wakes_up(i):
            _, minute = wakes_up
            for i in range(sleep_started, minute):
                current_guard[i] += 1
            sleep_started = None

    part1_guard, part1_sleeps = max(guard_sleeps.items(),
                                    key=lambda g: sum(g[1].values()))
    part2_guard, part2_sleeps = max(guard_sleeps.items(),
                                    key=lambda g: max(g[1].values(), default=0))

    return (part1_guard * part1_sleeps.most_common(1)[0][0],
            part2_guard * part2_sleeps.most_common(1)[0][0])
