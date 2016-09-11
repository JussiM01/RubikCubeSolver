from solve2layers import *

b_left = [(0, -9, 10), (0, 0, 10), (-9, 0, 10)]
b_right = [(-9, 0, 10), (0, 0, 10), (0, 9, 10)]
f_right = [(9, 0, 10), (0, 0, 10), (0, 9, 10)]
f_left = [(0, -9, 10), (0, 0, 10), (9, 0, 10)]
horizontal = [p for p in points if p[x] == 0] #
vertical = [p for p in points if p[y] == 0] #

def yellow_cross(cube): return {cube[p] for p in up_cross} == {'y'}
def yellow_angle_back_left(cube): return {cube[p] for p in b_left} == {'y'}
def yellow_angle_back_right(cube): return {cube[p] for p in b_right} == {'y'}
def yellow_angle_front_right(cube): return {cube[p] for p in f_right} == {'y'}
def yellow_angle_front_left(cube): return {cube[p] for p in f_left} == {'y'}    #
def yellow_line_horizontal(cube): return {cube[p] for p in horizontal} == {'y'} #
def yellow_line_vertical(cube): return {cube[p] for p in vertical} == {'y'}
def yellow_center(cube): return cube[(0, 0, 0)] == 'y'

bl_rot = ['F', 'U', 'R', 'Ui', 'Ri', 'Fi'] # SHOULD THE LINE CONDITIOND BE
br_rot = ['L', 'U', 'F', 'Ui', 'Fi', 'Li'] # CHECKED FIRST?
fr_rot = ['B', 'U', 'L', 'Ui', 'Li', 'Bi'] # IF SO, CHANGE THE ORDER EVERYWHERE.
fl_rot = ['R', 'U', 'B', 'Ui', 'Bi', 'Ri']
hor_rot = ['F', 'R', 'U', 'Ri', 'Ui', 'Fi']
ver_rot = ['L', 'F', 'U', 'Fi', 'Ui', 'Li']
cent_rot = ['F', 'U', 'R', 'Ui', 'Ri', 'Fi']

yellow_paterns = [yellow_angle_back_left, yellow_angle_back_right,
    yellow_angle_front_right, yellow_angle_front_left, yellow_line_horizontal,
    yellow_line_vertical] #
seq_for_y_cross = [bl_rot, br_rot, fr_rot, fl_rot, hor_rot, ver_rot, cent_rot] #

def recurse_yellow_cross(cube, rot1, rot2):
    rotations1, rotations2 = rot1, rot2
    if yellow_cross(cube): return (cube, rot1, rot2)
    for i in range(6):
        if yellow_paterns[i](cube):
            new_cube = rotate(cube, seq_for_y_cross[i])
            rotations2 += seq_for_y_cross[i]
            return recurse_yellow_cross(new_cube, rotations1, rotations2)

def make_a_yellow_cross(cube):
    new_cube, rotations1, rotations2 = make_a_2nd_layer(cube)
    return recurse_yellow_cross(new_cube, rotations1, rotations2)

# TODO: Test and debug.
