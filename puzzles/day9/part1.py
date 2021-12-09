"""
Day 9 - Part 1
"""

from puzzles import Puzzle

puzzle = Puzzle(__file__)
lines = puzzle.lines

rows = [[int(i) for i in list(l)] for l in lines]
columns = list(zip(*rows))

for row in rows:
    lowest_nums_in_row = filter(lambda x: x)
    print(lowest_nums_in_row)


def run():
    result = None

    print(lines)

    return result

if __name__ == '__main__':
    print(run())
