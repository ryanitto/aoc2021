"""
Day 7 - Part 2
"""

from puzzles import Puzzle
import time

puzzle = Puzzle(__file__)
nums = puzzle.comma_line_to_ints()


def run():
    t = time.localtime()
    print(f'{t.tm_hour}:{t.tm_min}:{t.tm_sec}')
    min_n, max_n = min(nums), max(nums)
    result = sum([sum(range(1, abs(n - 0) + 1)) for n in nums])  # Start with 0

    for i in range(min_n, max_n + 1):
        fuel_sum = sum([sum(range(1, abs(n - i) + 1)) for n in nums])
        result = fuel_sum if fuel_sum < result else result

    t = time.localtime()
    print(f'{t.tm_hour}:{t.tm_min}:{t.tm_sec}')
    return result


if __name__ == '__main__':
    print(run())
