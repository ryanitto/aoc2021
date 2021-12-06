"""
Day 6 - Part 2
"""

from puzzles import Puzzle

puzzle = Puzzle(__file__)
lines = puzzle.lines
line_to_ints = [int(l) for l in lines[0].split(',')]

fishes = [int(l) for l in line_to_ints]
fish_range = range(9)
fish_dict = {i: fishes.count(i) for i in fish_range}


def make_babies():
    done_making_babies = 0
    for i in fish_range:
        if i > 0:
            fish_dict[i-1] = fish_dict[i]
        else:
            done_making_babies = fish_dict[i]

    fish_dict[6] += done_making_babies
    fish_dict[8] = done_making_babies

    return done_making_babies, fish_dict


def run():
    days = 0
    while days != 256:
        make_babies()
        days += 1

    return sum(fish_dict.values())


if __name__ == '__main__':
    print(run())
