from pointsandrotations import *
from sidesandprinting import *
from solvingstatecheck import *

def top_white_center(cube):
    for side_label in side_labels:
        rotated_cube = switch_top_side(cube, side_label)
        if rotated_cube[(0, 0, 10)] == 'w': return (rotated_cube, side_label)

def blue_right_center(cube):
    for deg in [0, 90, 180, 270]:
        rotated_cube = turn(cube, z, deg)
        if rotated_cube[(0, 10, 0)] == 'b': return (rotated_cube, (z, deg))

def color_fits(cube, face, color_pair):
    return (cube[face] == color_1 or cube[face] == color_2)

top_edges = [{(0, 9, 10), (0, 10, 9)}, {(9, 0, 10), (10, 0, 9)},
    {(0, -9, 10), (0, -10, 9)}, {(-9, 0, 10), (-10, 0, 9)}]
bottom_edges = [{(0, 9, -10), (0, 10, -9)}, {(9, 0, -10), (10, 0, -9)},
    {(0, -9, -10), (0, -10, -9)}, {(-9, 0, -10), (-10, 0, -9)}]
color_pairs = [('w', 'b'), ('w', 'r'), ('w', 'g'), ('w', 'o')]

def place_top_edge(cube, order):
    new_cube, rotations = cube, []
    current, color_pair = top_edges[order], color_pairs[order]
    for edge in top_edges:
        if {color_fits(cube, face, color_pair) for face in edge} == {True}:
            if edge == current: break
            pass # Direction depend on the edge.
            return (new_cube, rotations)
    for edge in bottom_edges:
        if {color_fits(cube, face, color_pair) for face in edge} == {True}:
            pass # Direction depend on the edge.
            return (new_cube, rotations)

def fit_top_edge(cube, order):
    new_cube, rotations = place_top_edge(cube)
    pass # If wrong color at the top: do required rotations.
    return (new_cube, rotations)

def make_a_cross(cube):
    instructions = {}
    rotations = []
    step_1 = top_white_center(cube)
    cube_1 = step_1[0]
    instructions['which side on top'] = step_1[1]
    step_2 = blue_right_center(cube_1)
    cube_2 = step_2[0]
    rotations.append(step_2[1])
    step_3 = fit_top_edge(cube_3, 0)
    cube_3 = step_3[0]
    rotations.append(step_3[1])
    pass

    # TODO: There are obvious ways to refactor the code by writing functions
    # which combine some repeated actions.
