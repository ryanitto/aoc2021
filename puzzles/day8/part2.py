"""
Day 8 - Part 2
"""

from puzzles import Puzzle
from itertools import chain

puzzle = Puzzle(__file__)
lines = puzzle.lines

class Deduce:
    zero = ''
    one = ''
    two = ''
    three = ''
    four = ''
    five = ''
    six = ''
    seven = ''
    eight = ''
    nine = ''

    def __init__(self, puzzle_str):
        self.raw_signal = [''.join(sorted(s)) for s in puzzle_str[0].split()]
        self.raw_output = [''.join(sorted(s)) for s in puzzle_str[1].split()]

        self.signal_to_counts = [len(s) for s in self.raw_signal]

        # Known digits
        self.one = self.raw_signal[self.signal_to_counts.index(2)]
        self.four = self.raw_signal[self.signal_to_counts.index(4)]
        self.seven = self.raw_signal[self.signal_to_counts.index(3)]
        self.eight = self.raw_signal[self.signal_to_counts.index(7)]
        self.partial_known_chars = list(set(chain.from_iterable([{*self.one}, {*self.four}, {*self.seven}])))

        # Deduce digits
        self.determine_num([2, 9, 3, 5, 6, 0])

        # Digits to list (10)
        self.digits = [self.zero, self.one, self.two, self.three, self.four, self.five, self.six, self.seven,
                       self.eight, self.nine]

        self.output = self.determine_output()

    def determine_num(self, num_list):
        signal = self.partial_known_chars
        five_len_signals = [s for s in self.raw_signal if len(s) == 5]
        six_len_signals = [s for s in self.raw_signal if len(s) == 6]

        for num in num_list:
            # 2
            if num == 2:
                for i, f in enumerate(five_len_signals):
                    if len({*f}.difference(set(signal))) == 2:
                        self.two = five_len_signals.pop(i)

            # 9
            if num == 9:
                for i, s in enumerate(six_len_signals):
                    if len({*s}.difference(set(signal))) == 1:
                        self.nine = six_len_signals.pop(i)

            # 3
            if num == 3:
                for i, f in enumerate(five_len_signals):
                    if len({*f}.difference({*self.two})) == 1:
                        self.three = five_len_signals.pop(i)

            # 5
            if num == 5:
                self.five = five_len_signals.pop(0)

            # 6
            if num == 6:
                for i, f in enumerate(six_len_signals):
                    if len({*f}.difference({*self.five})) == 1:
                        self.six = six_len_signals.pop(i)

            # 0
            if num == 0:
                self.zero = six_len_signals.pop(0)

        return None

    def determine_output(self):
        str_to_num = ''.join([str(self.digits.index(r)) for r in self.raw_output])
        return int(str_to_num)

    def __repr__(self):
        return f'{self.zero, self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine}'


def extended_parsing(str_list):
    return sum(list([Deduce(s.split(' | ')).output for s in str_list]))


def run():
    result = extended_parsing(lines)
    return result


if __name__ == '__main__':
    print(run())
