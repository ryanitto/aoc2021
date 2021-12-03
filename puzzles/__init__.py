import os


class Puzzle(object):
    PUZZLE_FILE = 'puzzle.txt'

    def __init__(self, filepath=''):
        self.lines = None
        if filepath:
            self._file = os.path.join(os.path.dirname(filepath), self.PUZZLE_FILE)

        with open(self._file) as f:
            self.lines = [''.join(f.splitlines()) for f in f.readlines()]

    def __str__(self):
        return self.lines

    def lines_as_int(self):
        return [int(line) for line in self.lines]

    def lines_as_float(self):
        return [float(line) for line in self.lines]
