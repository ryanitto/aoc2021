import os


class Puzzle(object):
    PUZZLE_EXT = 'txt'

    def __init__(self, filepath):
        if filepath:
            self._file = os.path.splitext(filepath)[0] + os.path.extsep + self.PUZZLE_EXT
            self.lines = None
        with open(self._file) as f:
            self.lines = [f.split()[0] for f in f.readlines()]

    def __str__(self):
        return self.lines

    def lines_as_int(self):
        return [int(line) for line in self.lines]

    def lines_as_float(self):
        return [float(line) for line in self.lines]
