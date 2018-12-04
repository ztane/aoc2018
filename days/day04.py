from helpers import *

d = get_aoc_data(day=4)

shift = Parser('[<*>] Guard #<int> begins shift')
asleep = Parser('[<*>:<int>] falls asleep')
wakes_up = Parser('[<*>:<int>] wakes up')


def part1_and_2():
    guard_sleeps = defaultdict(Counter)
    current_guard = Counter()

    asleep_minute = None
    for i in sorted(d.lines):
        if shift(i):
            current_guard = guard_sleeps[scalar(shift)]

        elif asleep(i):
            asleep_minute = scalar(asleep)

        elif wakes_up(i):
            current_guard.update(range(asleep_minute, scalar(wakes_up)))

    part1_guard, part1_sleeps = max(guard_sleeps.items(),
                                    key=lambda g: sum(g[1].values()))
    part2_guard, part2_sleeps = max(guard_sleeps.items(),
                                    key=lambda g: max(g[1].values(), default=0))

    return (part1_guard * part1_sleeps.most_common(1)[0][0],
            part2_guard * part2_sleeps.most_common(1)[0][0])

