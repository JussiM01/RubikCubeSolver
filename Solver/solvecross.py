from pointsandrotations import *
from sidesandprinting import *

def color_fits(cube, face, color_pair):
    return (cube[face] == color_pair[0] or cube[face] == color_pair[1])

top_edges = [((0, 9, 10), (0, 10, 9)), ((-9, 0, 10), (-10, 0, 9)),
    ((0, -9, 10), (0, -10, 9)), ((9, 0, 10), (10, 0, 9))]
side_edges = [((10, 9, 0), (9, 10, 0)), ((-9, 10, 0), (-10, 9, 0)),
    ((-10, -9, 0), (-9, -10, 0)), ((9, -10, 0), (10, -9, 0))]
bottom_edges = [((0, 9, -10), (0, 10, -9)), ((-9, 0, -10), (-10, 0, -9)),
    ((0, -9, -10), (0, -10, -9)), ((9, 0, -10), (10, 0, -9))]
color_pairs = [('w', 'b'), ('w', 'o'), ('w', 'g'), ('w', 'r')]
side_rot = [['R'], ['B'], ['L'], ['F']]
side_inv = [['Ri'], ['Bi'], ['Li'], ['Fi']]

def place_top_edge(cube, edge, current, color_pair, order):
    new_cube, rotations = cube, []
    if edge == current:
        return (new_cube, rotations)
    else:
        new_cube = rotate(new_cube, side_rot[top_edges.index(edge)] * 2)
        rotations += (side_rot[top_edges.index(edge)] * 2)
    for edge2 in bottom_edges:
        if {color_fits(new_cube, face, color_pair) for face in edge2} == {True}:
            next_step = place_bottom_edge(new_cube, edge2, order)
            new_cube = next_step[0]
            rotations += next_step[1]
    return (new_cube, rotations)

def place_side_edge(cube, edge, color_pair, order):
    new_cube, rotations = cube, []
    new_cube = rotate(new_cube, side_rot[side_edges.index(edge) - 1])
    rotations += (side_rot[side_edges.index(edge) - 1])
    for edge2 in bottom_edges:
        if {color_fits(new_cube, face, color_pair) for face in edge2} == {True}:
            fix = []
            if order != 0 and order != bottom_edges.index(edge2):
                fix = side_inv[side_edges.index(edge) - 1]
            next_step = place_bottom_edge(new_cube, edge2, order, fix)
            new_cube = next_step[0]
            rotations += next_step[1]
    return (new_cube, rotations)

def place_bottom_edge(cube, edge, order, fix=[]):
    new_cube, rotations = cube, []
    n = order - bottom_edges.index(edge)
    if n > 0:
        new_cube = rotate(new_cube, ['D'] * n)
        rotations += (['D'] * n)
    if n < 0:
        new_cube = rotate(new_cube, ['Di'] * -n)
        rotations += (['Di']  * -n)
    if fix != []:
        new_cube = rotate(new_cube, fix)
        rotations += fix
    new_cube = rotate(new_cube, side_rot[bottom_edges.index(edge) + n] * 2)
    rotations += (side_rot[bottom_edges.index(edge) + n] * 2)
    return (new_cube, rotations)

def place_edge(cube, order):
    current, color_pair = top_edges[order], color_pairs[order]
    for edge in top_edges:
        if {color_fits(cube, face, color_pair) for face in edge} == {True}:
            return place_top_edge(cube, edge, current, color_pair, order)
    for edge in side_edges:
        if {color_fits(cube, face, color_pair) for face in edge} == {True}:
            return place_side_edge(cube, edge, color_pair, order)
    for edge in bottom_edges:
        if {color_fits(cube, face, color_pair) for face in edge} == {True}:
            return place_bottom_edge(cube, edge, order)

def fit_edge(cube, order):
    new_cube, rotations = place_edge(cube, order)
    if new_cube[top_edges[order][0]] != 'w':
        rot_sequence = side_inv[order] + ['U'] + side_inv[order - 1] + ['Ui']
        new_cube = rotate(new_cube, rot_sequence)
        rotations += rot_sequence
    return (new_cube, rotations)

def make_a_cross(cube):
    new_cube, rotations = cube, []
    for order in range(4):
        new_step = fit_edge(new_cube, order)
        new_cube = new_step[0]
        rotations += new_step[1]
    return (new_cube, rotations)
