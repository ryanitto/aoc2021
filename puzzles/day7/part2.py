"""
Day 7 - Part 2
"""

from puzzles import Puzzle

puzzle = Puzzle(__file__)
nums = sorted(puzzle.comma_line_to_ints())


def run():
    min_n, max_n = min(nums), max(nums)
    result = sum([sum(range(1, abs(n - 0) + 1)) for n in nums])  # Start with 0

    # for i in range(min_n, max_n + 1):
    #     for n in nums:
    #         if i > 0 and n > 0:
                # print(divmod(sum(range(1, abs(n - i) + 1)), i), n, i)
                # pass
        # fuel_sum = sum([sum(range(1, abs(n - i) + 1)) for n in nums])
        # result = fuel_sum if fuel_sum < result else result

    div_sum = {i: list(zip(*[divmod(sum(range(0, abs(n - i) + 1)) * i, i) for n in nums if i > 0 and n > 0])) for i in range(min_n, max_n + 1)}
    div_sum = {k: sum(list(v[0]) + list(v[1])) for k, v in div_sum.items() if any(v)}
    print(div_sum)
    print(min(div_sum.values()))

    return result


if __name__ == '__main__':
    print(run())
