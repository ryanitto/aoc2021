"""
--- Part Two ---

On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms,
the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards
it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle
column is completely marked. If you were to keep playing until this point, the second board would have a sum of
unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?

"""

from puzzles import Puzzle

puzzle = Puzzle(__file__)
lines = puzzle.lines


class Spot(int):
    drawn = False


class Card:
    winning_number = None
    card_num = 0

    def __init__(self, rows_as_str, card_num):
        self._rows = [Spot(x) for r in rows_as_str for x in r.split()]
        self.card_num = card_num

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
        for r in self._rows:
            if r == num:
                r.drawn = True
        return num

    def score(self):
        unmarked_sum = sum([row for row in self._rows if row.drawn is False])
        return unmarked_sum

    def __str__(self):
        return '<card: {}>'.format(self.card_num)


def run():
    result = None
    cards = []
    winning_cards = set()
    last_card = None
    num_to_draw = [int(l) for l in lines.pop(0).split(',')]

    for i in range(0, len(lines), 6):
        cards.append(Card(lines[i + 1:i + 6], len(cards)))

    last_card = find_last_winning_card(cards, num_to_draw, winning_cards)
    result = last_card.score() * last_card.winning_number

    return result


def find_last_winning_card(cards, num_to_draw, winning_cards):
    last_card = None
    for n in num_to_draw:
        for i, b in enumerate(cards):
            if len(winning_cards) == len(cards):
                return last_card

            b.draw_number(n)
            if b.bingo:
                b.winning_number = n
                winning_cards.add(b)
                last_card = b


if __name__ == '__main__':
    print(run())
