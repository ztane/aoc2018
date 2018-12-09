from helpers import *

d = get_aoc_data(day=9)


def play(players, points):
    elves = Counter()
    marbles = deque([0], maxlen=None)
    for i in range(1, points + 1):
        if i % 23 != 0:
            marbles.rotate(-1)
            marbles.append(i)

        if i % 23 == 0:
            score = i
            marbles.rotate(7)
            score += marbles.pop()
            marbles.rotate(-1)
            elvno = i % players
            elves[elvno] += score

    return elves.most_common(1)[0][1]


def part1_and_2():
    players, points = d.extract_ints
    return play(players, points), play(players, points * 100)

test_data = Data(dedent("""\
    10 players; last marble is worth 1618 points: high score is 8317
    13 players; last marble is worth 7999 points: high score is 146373
    17 players; last marble is worth 1104 points: high score is 2764
    21 players; last marble is worth 6111 points: high score is 54718
    30 players; last marble is worth 5807 points: high score is 37305"""))

parsed = test_data.parsed('<int> players; last marble is worth <int> points: high score is <int>')

for players, last_marble, high_score in parsed:
    assert play(players, last_marble) == high_score
