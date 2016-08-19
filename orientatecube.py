from pointsandrotations import *
from sidesandprinting import *
from solvingstatecheck import *

side_switch = {'front': (y, 90), 'bottom': (y, 180), 'back': (y, 270),
    'left': (x, 90), 'right': (x, 270), 'top': (x, 0)}

def top_white_center(cube):
    for side_label in side_labels:
        rotated_cube = switch_top_side(cube, side_label)
        if rotated_cube[(0, 0, 10)] == 'w':
            return (rotated_cube, side_switch[side_label])

def blue_right_center(cube):
    for deg in [0, 90, 180, 270]:
        rotated_cube = turn(cube, z, deg)
        if rotated_cube[(0, 10, 0)] == 'b': return (rotated_cube, (z, deg))

def orientate(cube):
    new_cube, turns = cube, []
    step_1 = top_white_center(cube)
    new_cube = step_1[0]
    turns.append(step_1[1])
    step_2 = blue_right_center(new_cube)
    new_cube = step_2[0]
    turns.append(step_2[1])
    return (new_cube, turns)
