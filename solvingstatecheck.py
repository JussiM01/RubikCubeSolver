from sidesandprinting import *
from pointsandrotations import *

top_cross = [{(i, 0, 10) for i in ps } | {(0, j, 10) for j in ps},
    {(10, 0, 9), (10, 0, 0)}, {(-10, 0, 9), (-10, 0, 0)},
    {(0, -9, 9), (0, -9, 0)},  {(0, 9, 9), (0, 9, 0)}]

top_layer = [set(up), {(10, j, 9) for j in ps}, {(-10, j, 9) for j in ps},
    {(i, -10, 9) for i in ps}, {(i, 10, 9) for i in ps}]

top_2_layers = [set(up), {(10, j, k) for j in ps for k in [0, 9]},
    {(-10, j, k) for j in ps for k in [0, 9]},
    {(i, -10, k) for i in ps for k in [0, 9]},
    {(i, 10, k) for i in ps for k in [0, 9]}]

solved_cube = [set(s) for s in sides]

top_states = [solved_cube, top_2_layers, top_layer, top_cross]
states = ['solved cube', 'two layers', 'layer', 'cross']

def all_same(cube, coordinate_set):
    return len({cube[p] for p in coordinate_set}) == 1

def check_top_state(cube, state):
    return {all_same(cube, coord_set) for coord_set in state} == {True}

def switch_top_side(cube, side_label):
    if side_label == 'front': return turn(cube, y, 90)
    if side_label == 'bottom': return turn(cube, y, 180)
    if side_label == 'back': return turn(cube, y, 270)
    if side_label == 'left': return turn(cube, x, 90)
    if side_label == 'right': return turn(cube, x, 270)
    return cube

def check_state(cube):
    if check_top_state(cube, solved_cube): return states[0]
    for i in range(1, 4):
        for side in side_labels:
            if check_top_state(switch_top_side(cube, side), top_states[i]):
                return (states[i], side)

def print_state(cube):
    state = check_state(cube)
    if state == 'solved cube': print('solved cube')
    else: print(state[0] + 'on the' + state[1] + 'side')
