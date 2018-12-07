from types import SimpleNamespace

from helpers import *
import toposort

d = get_aoc_data(day=7)


def part1():
    sort = defaultdict(set)
    all_tasks = set()
    for pre, post in d.parsed('Step <> must be finished before step <> can begin.'):
        sort[post].add(pre)
        all_tasks.add(pre)
        all_tasks.add(post)

    order = ''
    completed = set()
    while all_tasks:
        for i in sorted(all_tasks):
            if all(j in completed for j in sort[i]):
                order += i
                all_tasks.discard(i)
                completed.add(i)
                break

    return order



def task_duration(task):
    return ord(task) - 4


def part2():
    sort = defaultdict(set)
    all_tasks = set()
    for pre, post in d.parsed('Step <> must be finished before step <> can begin.'):
        sort[post].add(pre)
        all_tasks.add(pre)
        all_tasks.add(post)

    order = ''
    completed = set()
    all_tasks_init = set(all_tasks)
    workers = [SimpleNamespace(duration=0, task=None) for i in range(5)]
    seconds = 0
    while True:
        for w in workers:
            if not w.duration:
                if w.task:
                    completed.add(w.task)
                    w.task = None

            else:
                w.duration -= 1

        for w in workers:
            if not w.task:
                for i in sorted(all_tasks):
                    if all(j in completed for j in sort[i]):
                        order += i
                        all_tasks.discard(i)
                        w.task = i
                        w.duration = task_duration(i) - 1
                        break

        print(seconds, *[w.task or '-' for w in workers])

        if completed == all_tasks_init:
            break

        seconds += 1

    return seconds
