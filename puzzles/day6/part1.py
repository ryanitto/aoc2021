"""
Day 6 - Part 1
"""

from puzzles import Puzzle

puzzle = Puzzle(__file__)
lines = puzzle.lines
line_to_ints = [int(l) for l in lines[0].split(',')]


class Fish(int):
    timer = 0

    def __init__(self, initial_timer):
        self.timer = initial_timer

    def __repr__(self):
        return f'{self.timer}'

    def __next__(self):
        if self.timer < 1:
            self.timer = 6
            fish = Fish(9)
            fishes.append(fish)
        else:
            self.timer -= 1


fishes = [Fish(l) for l in line_to_ints]


def run():
    yield map(next, fishes)


if __name__ == '__main__':
    result = None
    for i in range(80):
        result = len(list(next(run())))

    print(result)
