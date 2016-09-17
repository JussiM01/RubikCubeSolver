from solveyellowcorners import *

def correct_A(cube):
    return {cube[(-9, -10, 9)] == 'b', cube[(-10, -9, 9)] == 'o'} == {True}

def correct_B(cube):
    return {cube[(-10, 9, 9)] == 'o', cube[(-9, 10, 9)] == 'g'} == {True}

def correct_C(cube):
    return {cube[(9, -10, 9)] == 'b', cube[(10, -9, 9)] == 'r'} == {True}

def correct_D(cube):
    return {cube[(10, 9, 9)] == 'r', cube[(9, 10, 9)] == 'g'} == {True}

def correct_diag(cube):
    if correct_A(cube) and correct_D(cube): return True
    if correct_B(cube) and correct_C(cube): return True
    return False

def correct_AB(cube): return correct_A(cube) and correct_B(cube)
def correct_BD(cube): return correct_B(cube) and correct_D(cube)
def correct_DC(cube): return correct_D(cube) and correct_C(cube)
def correct_CA(cube): return correct_C(cube) and correct_A(cube)

def num_correct_corners(cube):
    return sum([int(correct_A(cube)), int(correct_B(cube)),
        int(correct_C(cube)), int(correct_D(cube))])

def correct_yellow_corners(cube): return num_correct_corners(cube) == 4

switch1 = ['Ri', 'F', 'Ri', 'B', 'B', 'R', 'Fi', 'Ri', 'B', 'B', 'R', 'R', 'Ui']
switch2 = ['Fi', 'L', 'Fi', 'R', 'R', 'F', 'Li', 'Fi', 'R', 'R', 'F', 'F', 'Ui']
switch3 = ['Li', 'B', 'Li', 'F', 'F', 'L', 'Bi', 'Li', 'F', 'F', 'L', 'L', 'Ui']
switch4 = ['Bi', 'R', 'Bi', 'L', 'L', 'B', 'Ri', 'Bi', 'L', 'L', 'B', 'B', 'Ui']

non_diag_pairs = [correct_AB, correct_BD, correct_DC, correct_CA]
cc_seq = [switch1, switch2, switch3, switch4]

def recurse_correct_cs(cube, rot1, rot2):
    new_cube, rotations1, rotations2 = cube, rot1, rot2
    for i in range(4):
        n = num_correct_corners(new_cube)
        if n == 4: return (new_cube, rotations1, rotations2)
        if correct_diag(new_cube):
            new_cube = rotate(new_cube, cc_seq[0])
            rotations2 += cc_seq[0]
            return recurse_correct_cs(new_cube, rotations1, rotations2)
        for j in range(4):
            if non_diag_pairs[j](new_cube):
                new_cube = rotate(new_cube, cc_seq[j])
                rotations2 += cc_seq[j]
                return (new_cube, rotations1, rotations2)
        new_cube = rotate(new_cube, ['U'])
        rotations2 += ['U']

def make_correct_corners(cube):
    new_cube, rotations1, rotations2 = make_yellow_corners(cube)
    return recurse_correct_cs(new_cube, rotations1, rotations2)
