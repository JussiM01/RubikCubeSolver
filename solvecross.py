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

def white_blue_edge(cube):
    pass

def make_a_cross(cube):
    instructions = {}
    rotations = []
    step_1 = top_white_center(cube)
    cube_1 = step_1[0]
    instructions['which side on top'] = step_1[1]
    step_2 = blue_right_center(cube_1)
    cube_2 = step_2[0]
    rotations.append(step_2[1])
    step_3 = white_blue_edge(cube_3)
    cube_3 = step_3[0]
    rotations.append(step_3[1])
    pass

    # TODO: There are obvious ways to refactor the code by writing functions
    # which combine some repeated actions.
