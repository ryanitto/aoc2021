"""
Day 9 - Part 1
"""

from puzzles import Puzzle

puzzle = Puzzle(__file__)
lines = puzzle.lines

rows = [[int(i) for i in list(l)] for l in lines]
columns = list(zip(*rows))

# NOTE:  r == columns[j][i]
for i, row in enumerate(rows):
    for j, r in enumerate(row):
        # Gather edges & corners
        # Top/bottom edges
        if i == 0 or i == len(rows) - 1:
            print(r, 'top/bot edge')
        # Side edges
        if j == 0 or j == len(row) - 1:
            print(r, 'side edge')

        # Check all four directions
        if 0 < i < len(rows) - 1 and 0 < j < len(row) - 1:
            print(r, columns[j][i])



def run():
    result = None

    # print(lines)
    print(rows)
    print(columns)

    return result

if __name__ == '__main__':
    print(run())
