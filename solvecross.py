from pointsandrotations import *
from sidesandprinting import *
from solvingstatecheck import *

def color_fits(cube, face, color_pair):
    return (cube[face] == color_pair[0] or cube[face] == color_pair[1])

top_edges = [((0, 9, 10), (0, 10, 9)), ((9, 0, 10), (10, 0, 9)),
    ((0, -9, 10), (0, -10, 9)), ((-9, 0, 10), (-10, 0, 9))]
bottom_edges = [((0, 9, -10), (0, 10, -9)), ((9, 0, -10), (10, 0, -9)),
    ((0, -9, -10), (0, -10, -9)), ((-9, 0, -10), (-10, 0, -9))]
color_pairs = [('w', 'b'), ('w', 'r'), ('w', 'g'), ('w', 'o')]
side_rot = [(y, 180), (x, 180), (y, 180), (x, 180)]
side_fix1 = [(y, 270), (x, 270), (y, 90), (x, 90)]
side_fix2 = [(x, 270), (y, 90), (x, 90), (y, 270)]
bottom_rot = [(z, 0), (z, 90), (z, 180), (z, 270)]
row_ind = [0, 0, 3, 3]
row_ind2 = [0, 3, 3, 0]
top_faces = [(0, 9, 10), (9, 0, 10), (0, -9, 10), (-9, 0, 10)]

def place_top_edge(cube, order):
    new_cube, rotations = cube, []
    current, color_pair = top_edges[order], color_pairs[order]
    for edge in top_edges:
        if {color_fits(cube, face, color_pair) for face in edge} == {True}:
            if edge == current:
                return (new_cube, rotations)
            else:
                new_cube = rotate(new_cube, side_rot[order][0],
                    row_ind[order], side_rot[order][1])
                rotations.append(side_rot)
            return (new_cube, rotations)
    for edge in bottom_edges:
        if {color_fits(cube, face, color_pair) for face in edge} == {True}:
            new_cube = rotate(new_cube, side_rot[order][0], row_ind[order],
            side_rot[order][1])
    return (new_cube, rotations)

def fit_top_edge(cube, order):
    new_cube, rotations = place_top_edge(cube, order)
    if new_cube[top_edges[order][0]] != 'w':
        new_cube = rotate(new_cube, side_fix1[order][0], row_ind[order],
            side_fix1[order][1])
        rotations.append(side_fix1[order])
        new_cube = rotate(new_cube, z, 0, 90)
        rotations.append((z, 90))
        new_cube = rotate(new_cube, side_fix2[order][0], row_ind2[order],
            side_fix2[order][1])
        rotations.append(side_fix2[order])
        new_cube = rotate(new_cube, z, 0, 270)
        rotations.append((z, 270))
    return (new_cube, rotations)

def make_a_cross(cube):
    new_cube, rotations = cube, []
    for order in range(4):
        new_step = fit_top_edge(new_cube, order)
        new_cube = new_step[0]
        rotations.append(new_step[1])
    return (new_cube, rotations)

    # TODO: Fix the bugs.
    # Change the implementation of the row rotations.
