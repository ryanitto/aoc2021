"""
Day 5 - Part 1
"""

from puzzles import Puzzle

puzzle = Puzzle(__file__)
lines = puzzle.lines


class Point(object):
    value = 0

    def __repr__(self):
        return str(self.value) if self.value else '.'

    def __int__(self):
        return self.value


def parse_to_coords():
    lines_to_coord_strs = [l.split(' -> ') for l in lines]
    coords_strs_to_pairs = [[int(x) for x in c.split(',')] for l in lines_to_coord_strs for c in l]

    # Get horizontal & vertical lines (puzzle prompt said "for now...")
    pairs_to_segments = [coords_strs_to_pairs[i] + coords_strs_to_pairs[i + 1] for i in range(0, len(coords_strs_to_pairs), 2)]
    valid_x_segments_indeces = [pairs_to_segments.index(s) for s in pairs_to_segments if s[0] == s[2]]
    valid_y_segments_indeces = [pairs_to_segments.index(s) for s in pairs_to_segments if s[1] == s[3]]
    valid_indeces = sorted(valid_x_segments_indeces + valid_y_segments_indeces)

    coords = [pairs_to_segments[v] for v in valid_indeces]
    return coords


def determine_floor_coverage(coords):
    x_size = sorted((max([max([c[0], c[2]]) for c in coords]), min([min([c[0], c[2]]) for c in coords])))
    y_size = sorted((max([max([c[1], c[3]]) for c in coords]), min([min([c[1], c[3]]) for c in coords])))
    max_size = sorted(x_size + y_size)[2:]
    return max_size[0] + 1


def draw_diagram(floor_size, coords):
    diagram = [[Point() for i in range(floor_size)] for i in range(floor_size)]
    y_points = [(c[1], c[3]) for c in coords]
    x_points = [(c[0], c[2]) for c in coords]
    # print(y_to_indeces)
    for c in coords:
        y_seg = sorted([c[1], c[3]])
        x_seg = sorted([c[0], c[2]])

        # If there's a range between Y values, we're drawing vertically!
        if y_seg[0] - y_seg[1]:
            for i in range(y_seg[0], y_seg[1] + 1):
                seg = diagram[i][x_seg[0]:x_seg[1]+1]
                for s in seg:
                    s.value += 1

        # If there's a range between X values, we're drawing horizontally!
        if x_seg[0] - x_seg[1]:
            row = diagram[y_seg[0]]
            seg = row[x_seg[0]:x_seg[1]+1]
            for s in seg:
                s.value += 1

    return diagram


def run():
    result = 0

    coords = parse_to_coords()
    floor_size = determine_floor_coverage(coords)
    diagram = draw_diagram(floor_size, coords)
    for d in diagram:
        for r in d:
            if r.value > 1:
                result += 1

    return result


if __name__ == '__main__':
    print(run())
