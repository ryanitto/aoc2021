"""
Day 14 - Part 1
"""

from puzzles import Puzzle
from collections import deque, Counter

puzzle = Puzzle(__file__)
lines = puzzle.lines
NUM_STEPS = range(10)


class Pair(str):
    pair_letters = ''
    insert_letter = ''

    def __init__(self, pair_str):
        self.pair_letters, self.insert_letter = pair_str.split(' -> ')

    def __repr__(self):
        return f'{self.pair_letters}>>{self.insert_letter}'

    def __str__(self):
        return self.pair_letters

    def __cmp__(self, other):
        if isinstance(other, str):
            return self.pair_letters == other
        elif isinstance(other, Pair):
            return self.pair_letters == other.pair_letters
        else:
            return self == other


class Template(deque):
    pass


line_to_template = Template(lines.pop(0))
lines.pop(0)  # Remove blank line after template
lines_to_pairs = [Pair(l) for l in lines]


def grow_polymer():
    ltt = line_to_template
    ltt_str = ''.join(list(ltt))
    iter_ltt = iter(ltt)
    print(next(iter_ltt))
    print(next(iter_ltt))
    print(next(iter_ltt))
    print(next(iter_ltt))
    for _ in NUM_STEPS:
        rotate_count = 0
        for j in range(len(ltt_str) - 1):
            for i, l in enumerate(lines_to_pairs):
                compair = ltt_str[j] + ltt_str[j + 1]  # Like the variable pun?
                ltp = lines_to_pairs[i]
                compairison = ltp.pair_letters == compair
                # print(compair, repr(ltp), i, compairison)
                if compairison:
                    ltt.rotate(-1)
                    ltt.appendleft(ltp.insert_letter)
                    ltt.rotate(-1)
                    rotate_count += 2
        ltt.rotate(rotate_count)
        ltt_str = ''.join(list(ltt))
    return Counter(ltt)


def run():
    result = None

    mc = grow_polymer().most_common()
    result = int(mc[0][1]) - int(mc[-1][1])

    return result


if __name__ == '__main__':
    print(run())
