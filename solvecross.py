from pointsandrotations import *
from sidesandprinting import *
from solvingstatecheck import *

def color_fits(cube, face, color_pair):
    return (cube[face] == color_pair[0] or cube[face] == color_pair[1])

top_edges = [((0, 9, 10), (0, 10, 9)), ((-9, 0, 10), (-10, 0, 9)),
    ((0, -9, 10), (0, -10, 9)), ((9, 0, 10), (10, 0, 9))]
side_edges = [((10, 9, 0), (9, 10, 0)), ((-9, 10, 0), (-10, 9, 0)),
    ((-10, -9, 0), (-9, -10, 0)), ((9, -10, 0), (10, -9, 0))]
bottom_edges = [((0, 9, -10), (0, 10, -9)), ((-9, 0, -10), (-10, 0, -9)),
    ((0, -9, -10), (0, -10, 9)), ((9, 0, -10), (10, 0, -9))]
color_pairs = [('w', 'b'), ('w', 'o'), ('w', 'g'), ('w', 'r')]
side_rot = [['R'], ['B'], ['L'], ['F']]
side_inv = [['Ri'], ['Bi'], ['Li'], ['Fi']]

def place_top_edge(cube, order):
    new_cube, rotations = cube, []
    current, color_pair = top_edges[order], color_pairs[order]
    for edge in top_edges:
        if {color_fits(cube, face, color_pair) for face in edge} == {True}:
            if edge == current:
                return (new_cube, rotations)
            else:
                new_cube = rotate(new_cube, side_rot[top_edges.index(edge)] * 2)
                rotations += (side_rot[top_edges.index(edge)] * 2)
    for edge in side_edges:
        if {color_fits(cube, face, color_pair) for face in edge} == {True}:
            new_cube = rotate(new_cube, side_rot[side_edges.index(edge)])
            rotations += (side_rot[side_edges.index(edge)])
    for edge in bottom_edges:
        if {color_fits(cube, face, color_pair) for face in edge} == {True}:
            n = bottom_edges.index(edge) - order
            if n > 0:
                new_cube = rotate(new_cube, ['D'] * n)
                rotations += (['D'] * n)
            if n < 0:
                new_cube = rotate(new_cube, ['Di'] * -n)
                rotations += (['Di']  * -n)
            new_cube = rotate(new_cube, side_rot[bottom_edges.index(edge)] * 2)
            rotations += (side_rot[bottom_edges.index(edge)] * 2)
    return (new_cube, rotations)

def fit_top_edge(cube, order):
    new_cube, rotations = place_top_edge(cube, order)
    if new_cube[top_edges[order][0]] != 'w':
        rot_sequence = side_inv[order] + ['U'] + side_inv[order - 1] + ['Ui']
        new_cube = rotate(new_cube, rot_sequence)
        rotations += rot_sequence
    return (new_cube, rotations)

def make_a_cross(cube):
    new_cube, rotations = cube, []
    for order in range(4):
        new_step = fit_top_edge(new_cube, order)
        new_cube = new_step[0]
        rotations += new_step[1]
    return (new_cube, rotations)

    # TODO: Fix the bugs.
    # Divide place_top_edge into sorter functions.
