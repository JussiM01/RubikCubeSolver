from sidesandprinting import *
from pointsandrotations import *
from solvefinalstate import *

# top_cross = [{(i, 0, 10) for i in ps } | {(0, j, 10) for j in ps},
#     {(10, 0, 9), (10, 0, 0)}, {(-10, 0, 9), (-10, 0, 0)},
#     {(0, -9, 9), (0, -9, 0)},  {(0, 9, 9), (0, 9, 0)}]
#
# top_layer = [set(up), {(10, j, 9) for j in ps}, {(-10, j, 9) for j in ps},
#     {(i, -10, 9) for i in ps}, {(i, 10, 9) for i in ps}]
#
# top_2_layers = [set(up), {(10, j, k) for j in ps for k in [0, 9]},
#     {(-10, j, k) for j in ps for k in [0, 9]},
#     {(i, -10, k) for i in ps for k in [0, 9]},
#     {(i, 10, k) for i in ps for k in [0, 9]}]
#
# solved_cube = [set(s) for s in sides]
#
# top_states = [solved_cube, top_2_layers, top_layer, top_cross]
# states = ['solved cube', 'two layers', 'layer', 'cross']
#
# def all_same(cube, coordinate_set):
#     return len({cube[p] for p in coordinate_set}) == 1
#
# def check_top_state(cube, state):
#     return {all_same(cube, coord_set) for coord_set in state} == {True}

def cube_solved(cube):
    if {cube[p] == 'r' for p in front} != {True}: return False
    if {cube[p] == 'b' for p in left} != {True}: return False
    if {cube[p] == 'o' for p in back} != {True}: return False
    if {cube[p] == 'g' for p in right} != {True}: return False
    if {cube[p] == 'y' for p in up} != {True}: return False
    if {cube[p] == 'w' for p in down} != {True}: return False
    return True

def cross_solved(cube):
    if not white_cross_up(cube): return False
    if not blue_pieces(cube): return False
    if not orange_pieces(cube): return False
    if not green_pieces(cube): return False
    if not red_pieces(cube): return False
    return True

up_cross = {(0, 0, 10), (0, 9, 10), (-9, 0, 10), (0, -9, 10), (9, 0, 10)}
segment_R = {(0, 10, 9), (0, 10, 0)}
segment_B = {(-10, 0, 9), (-10, 0, 0)}
segment_L = {(0, -10, 9), (0, -10, 0)}
segment_F = {(10, 0, 9), (10, 0, 0)}

def white_cross_up(cube): return {cube[p] for p in up_cross} == {'w'}
def blue_pieces(cube): return {cube[p] for p in segment_R} == {'b'}
def orange_pieces(cube): return {cube[p] for p in segment_B} == {'o'}
def green_pieces(cube): return {cube[p] for p in segment_L} == {'g'}
def red_pieces(cube): return {cube[p] for p in segment_F} == {'r'}

def corners_solved(cube):
    if not white_side_up(cube): return False
    if not blue_triangle(cube): return False
    if not orange_triangle(cube): return False
    if not green_triangle(cube): return False
    if not red_triangle(cube): return False
    return True

triangle_R = {(9, 10, 9), (0, 10, 9), (-9, 10, 9), (0, 10, 0)}
triangle_B = {(-10, 9, 9), (-10, 0, 9), (-10, -9, 9), (-10, 0, 0)}
triangle_L = {(-9, -10, 9), (0, -10, 9), (9, -10, 9), (0, -10, 0)}
triangle_F = {(10, -9, 9), (10, 0, 9), (10, 9, 9), (10, 0, 0)}

def white_side_up(cube): return {cube[p] for p in up} == {'w'}
def blue_triangle(cube): return {cube[p] for p in triangle_R} == {'b'}
def orange_triangle(cube): return {cube[p] for p in triangle_B} == {'o'}
def green_triangle(cube): return {cube[p] for p in triangle_L} == {'g'}
def red_triangle(cube): return {cube[p] for p in triangle_F} == {'r'}

def twolayers_solved(cube):
    if not white_side_down(cube): return False
    if not green_2layers(cube): return False
    if not orange_2layers(cube): return False
    if not blue_2layers(cube): return False
    if not red_2layers(cube): return False
    return True

twolayers_R = {p for p in points if p[y] == 10 and p[z] < 9}
twolayers_B = {p for p in points if p[x] == -10 and p[z] < 9}
twolayers_L = {p for p in points if p[y] == -10 and p[z] < 9}
twolayers_F = {p for p in points if p[x] == 10 and p[z] < 9}

def white_side_down(cube): return {cube[p] for p in down} == {'w'}
def green_2layers(cube): return {cube[p] for p in twolayers_R} == {'g'}
def orange_2layers(cube): return {cube[p] for p in twolayers_B} == {'o'}
def blue_2layers(cube): return {cube[p] for p in twolayers_L} == {'b'}
def red_2layers(cube): return {cube[p] for p in twolayers_F} == {'r'}

solved_state = [cube_solved, correct_yellow_corners, yellow_top, yellow_cross,
    twolayers_solved, corners_solved, cross_solved]

string_rep = ['cube', 'correct yellow corners', 'yellow top', 'yellow cross',
    'two layers', 'white corners', 'white cross']

def switch_top_side(cube, side_label):
    if side_label == 'front': return turn(cube, y, 90)
    if side_label == 'bottom': return turn(cube, y, 180)
    if side_label == 'back': return turn(cube, y, 270)
    if side_label == 'left': return turn(cube, x, 90)
    if side_label == 'right': return turn(cube, x, 270)
    return cube

def check_state(cube): # Alter this function.
    if check_top_state(cube, solved_cube): return states[0]
    for i in range(1, 4):
        for side in side_labels:
            if check_top_state(switch_top_side(cube, side), top_states[i]):
                return (states[i], side)

def print_state(cube): # Alter this function.
    state = check_state(cube)
    if state == 'solved cube': print('solved cube')
else: print(state[0] + 'on the' + state[1] + 'side') # Should return:
    # 'your cube is scrambled' if none of the states is true.

# TODO: Test and debug.
# Add all needed stages to top_states and states.
# Change the definitions so that top_cross needs to be white (as in the guide).
# Change/add also the rest of the definitions as tey are in the solution guide.
