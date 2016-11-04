from solveyellowcross import *

top_cs = [(9, -9, 10), (-9, -9, 10), (-9, 9, 10), (9, 9, 10)]

def yellow_top(cube): return {cube[p] for p in up} == {'y'}
def num_yellow_corners(cube): return sum([int(cube[p] == 'y') for p in top_cs])

def yellow_face_1(cube): return cube[(9, -10, 9)] == 'y'
def yellow_face_2(cube): return cube[(-10, -9, 9)] == 'y'
def yellow_face_3(cube): return cube[(-9, 10, 9)] == 'y'
def yellow_face_4(cube): return cube[(10, 9, 9)] == 'y'

def fl_yellow_corner(cube): return cube[(9, -9, 10)] == 'y'
def bl_yellow_corner(cube): return cube[(-9, -9, 10)] == 'y'
def br_yellow_corner(cube): return cube[(-9, 9, 10)] == 'y'
def fr_yellow_corner(cube): return cube[(9, 9, 10)] == 'y'

def yellow_face_5(cube): return cube[(10, -9, 9)] == 'y'
def yellow_face_6(cube): return cube[(-9, -10, 9)] == 'y'
def yellow_face_7(cube): return cube[(-10, 9, 9)] == 'y'
def yellow_face_8(cube): return cube[(9, 10, 9)] == 'y'

y_cs_rot1 = ['R', 'U', 'Ri', 'U', 'R', 'U', 'U', 'Ri']
y_cs_rot2 = ['F', 'U', 'Fi', 'U', 'F', 'U', 'U', 'Fi']
y_cs_rot3 = ['L', 'U', 'Li', 'U', 'L', 'U', 'U', 'Li']
y_cs_rot4 = ['B', 'U', 'Bi', 'U', 'B', 'U', 'U', 'Bi']

no_y_corners = [yellow_face_1, yellow_face_2, yellow_face_3, yellow_face_4]

one_y_corner = [fl_yellow_corner, bl_yellow_corner, br_yellow_corner,
    fr_yellow_corner]

more_than_one_c = [yellow_face_5, yellow_face_6, yellow_face_7, yellow_face_8]

num_corners = [no_y_corners, one_y_corner, more_than_one_c, more_than_one_c]

rot_seq_y_cs = [y_cs_rot1, y_cs_rot2, y_cs_rot3, y_cs_rot4]

def recurse_y_corners(cube, rot1, rot2):
    rotations1, rotations2 = rot1, rot2
    if yellow_top(cube): return (cube, rot1, rot2)
    for i in range(3):
        if num_yellow_corners(cube) == i:
            for j in range(4):
                if num_corners[i][j](cube):
                    new_cube = rotate(cube, rot_seq_y_cs[j])
                    rotations2 += rot_seq_y_cs[j]
                    return recurse_y_corners(new_cube, rotations1, rotations2)

def make_yellow_corners(cube):
    new_cube, rotations1, rotations2 = make_a_yellow_cross(cube)
    return recurse_y_corners(new_cube, rotations1, rotations2)
