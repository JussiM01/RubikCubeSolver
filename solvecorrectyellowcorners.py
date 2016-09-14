from solveyellowcorners import *

def correct_A(cube): pass
def correct_B(cube): pass
def correct_C(cube): pass
def correct_D(cube): pass

def num_correct_corners(cube):
    return sum([int(correct_A(cube)), int(correct_B(cube)),
        int(correct_C(cube)), int(correct_F(cube))])

def correct_yellow_corners(cube): return num_correct_corners(cube) == 4



def recurse_correct_cs(cube, rot1, rot2):
    rotations1, rotations2 = rot1, rot2
    if correct_yellow_corners(cube): return (cube, rot1, rot2)
    # for i in range(3):
    #     if num_yellow_corners(cube) == i:
    #         for j in range(4):
    #             if num_corners[i][j](cube):
    #                 new_cube = rotate(cube, rot_seq_y_cs[j])
    #                 rotations2 += rot_seq_y_cs[j]
                    return recurse_correct_cs(new_cube, rotations1, rotations2)

def make_correct_edges(cube):
    new_cube, rotations1, rotations2 = make_yellow_corners(cube)
    return recurse_correct_cs(new_cube, rotations1, rotations2)
