from puzzles import Puzzle

puzzle = Puzzle(__file__)
lines = puzzle.lines


class Spot(int):
    drawn = False


class Card:
    def __init__(self, rows_as_str):
        self._rows = [Spot(x) for r in rows_as_str for x in r.split()]

    @property
    def rows(self):
        new_rows = []
        for i in range(0, len(self._rows), 5):
            new_rows.append(self._rows[i:i+5])
        return new_rows

    @property
    def columns(self):
        return list(zip(*self.rows))

    @property
    def bingo(self):
        bingos = []
        for row in self.rows:
            bingos.append(all([r.drawn for r in row]))
        for col in self.columns:
            bingos.append(all([c.drawn for c in col]))
        return any(bingos)

    def draw_number(self, num):
        for row in self.rows:
            for r in row:
                if r == num:
                    r.drawn = True
        return num

    def score(self):
        unmarked_sum = sum([r for row in self.rows for r in row if r.drawn is False])
        return unmarked_sum


def run():
    result = None
    cards = []
    num_to_draw = [int(l) for l in lines.pop(0).split(',')]

    for i in range(0, len(lines), 6):
        cards.append(Card(lines[i+1:i+6]))

    for n in num_to_draw:
        for i, b in enumerate(cards):
            b.draw_number(n)
            if b.bingo:
                return b.score() * n

    return result

if __name__ == '__main__':
    print(run())
