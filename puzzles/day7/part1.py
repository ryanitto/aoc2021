"""
Day 7 - Part 1
"""

from puzzles import Puzzle

puzzle = Puzzle(__file__)
nums = puzzle.comma_line_to_ints()


def run():
    min_n, max_n = min(nums), max(nums)
    result = sum([abs(n - 0) for n in nums])  # Start with 0

    for i in range(min_n, max_n + 1):
        fuel_sum = sum([abs(n - i) for n in nums])
        result = fuel_sum if fuel_sum < result else result

    return result


if __name__ == '__main__':
    print(run())
