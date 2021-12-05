"""
Day 5 - Part 2
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

    pairs_to_segments = [coords_strs_to_pairs[i] + coords_strs_to_pairs[i + 1] for i in range(0, len(coords_strs_to_pairs), 2)]

    # Just horizontal & vertical
    valid_x_segments_indeces = [pairs_to_segments.index(s) for s in pairs_to_segments if s[0] == s[2]]
    valid_y_segments_indeces = [pairs_to_segments.index(s) for s in pairs_to_segments if s[1] == s[3]]

    # So, yeah, we gotta cover more than just horizontal & vertical.  Gotta do diagonal now...
    valid_diag_indeces = [pairs_to_segments.index(s) for s in pairs_to_segments if
     abs(s[0] - s[2]) == abs(s[1] - s[3])]
    diag_coords = [pairs_to_segments[pairs_to_segments.index(s)]
    for s in pairs_to_segments if abs(s[0] - s[2]) == abs(s[1] - s[3])]

    valid_indeces = sorted(valid_x_segments_indeces + valid_y_segments_indeces)

    straight_coords = [pairs_to_segments[v] for v in valid_indeces]
    return straight_coords, diag_coords


def determine_floor_coverage(coords):
    x_size = sorted((max([max([c[0], c[2]]) for c in coords]), min([min([c[0], c[2]]) for c in coords])))
    y_size = sorted((max([max([c[1], c[3]]) for c in coords]), min([min([c[1], c[3]]) for c in coords])))
    max_size = sorted(x_size + y_size)[2:]
    return max_size[0] + 1


def draw_diagram(floor_size, striaght_coords, diag_coords):
    diagram = [[Point() for i in range(floor_size)] for i in range(floor_size)]

    # Straight lines
    for c in striaght_coords:
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

    # Diagonal lines
    for d in diag_coords:
        x_seg = [d[0], d[2]]
        y_seg = [d[1], d[3]]

        x_step_dir = 1 if x_seg[0] < x_seg[1] else -1
        y_step_dir = 1 if y_seg[0] < y_seg[1] else -1

        x_coords = [x for x in range(x_seg[0], x_seg[1] + x_step_dir, x_step_dir)]
        y_coords = [y for y in range(y_seg[0], y_seg[1] + y_step_dir, y_step_dir)]
        for i, y in enumerate(y_coords):
            diagram[y][x_coords[i]].value += 1

    return diagram


def run():
    result = 0

    straight_coords, diag_coords = parse_to_coords()
    floor_size = determine_floor_coverage(straight_coords + diag_coords)
    diagram = draw_diagram(floor_size, straight_coords, diag_coords)
    for d in diagram:
        print(d)
        for r in d:
            if r.value > 1:
                result += 1

    return result


if __name__ == '__main__':
    print(run())
