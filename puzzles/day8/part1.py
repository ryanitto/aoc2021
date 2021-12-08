"""
Day 8 - Part 1
"""

from puzzles import Puzzle
from itertools import chain

puzzle = Puzzle(__file__)
lines = puzzle.lines


def extended_parsing(str_list):
    return list(chain.from_iterable([[len(x) for x in s.split(' | ')[-1].split()] for s in str_list]))


def run():
    puzzle = (extended_parsing(lines))

    one = puzzle.count(2)
    four = puzzle.count(4)
    seven = puzzle.count(3)
    eight = puzzle.count(7)

    return sum((one, four, seven, eight))


if __name__ == '__main__':
    print(run())
