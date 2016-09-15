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

def correct_CD(cube): return correct_C(cube) and correct_D(cube)
def correct_AC(cube): return correct_A(cube) and correct_C(cube)
def correct_BA(cube): return correct_B(cube) and correct_A(cube)
def correct_DB(cube): return correct_D(cube) and correct_B(cube)

def num_correct_corners(cube):
    return sum([int(correct_A(cube)), int(correct_B(cube)),
        int(correct_C(cube)), int(correct_F(cube))])

def correct_yellow_corners(cube): return num_correct_corners(cube) == 4

switchCD_seq = ['Ri', 'F', 'Ri', 'B', 'B', 'R', 'Fi', 'Ri', 'B', 'B', 'R', 'Ui']
switchAC_seq = ['Fi', 'L', 'Fi', 'R', 'R', 'F', 'Li', 'Fi', 'R', 'R', 'F', 'Ui']
switchBA_seq = ['Li', 'B', 'Li', 'F', 'F', 'L', 'Bi', 'Li', 'F', 'F', 'L', 'Ui']
switchDB_seq = ['Bi', 'R', 'Bi', 'L', 'L', 'B', 'Ri', 'Bi', 'L', 'L', 'B', 'Ui']

correct_pairs = [correct_diag, correct_CD, correct_AC, correct_BA, correct_DB]
cc_seq = [switchCD_seq, switchCD_seq, switchAC_seq, switchBA_seq, switchDB_seq]

def recurse_correct_cs(cube, rot1, rot2):
    rotations1, rotations2 = rot1, rot2
    if correct_yellow_corners(cube): return (cube, rot1, rot2)
    for i in range(5):
        if correct_pairs[i](cube):
            new_cube = rotate(cube, cc_seq[i])
            rotations2 += cc_seq[i]
            return recurse_correct_cs(new_cube, rotations1, rotations2)

def make_correct_corners(cube):
    new_cube, rotations1, rotations2 = make_yellow_corners(cube)
    n = num_correct_corners(new_cube)
    if n == 4: return (new_cube, rotations1, rotations2)
    if n < 2:
        for j in range(1, 4):
            new_cube = rotate(new_cube, (['U'] * j))
            rotations2 += (['U'] * j)
            if num_correct_corners(new_cube) > 1:
                return recurse_correct_cs(new_cube, rotations1, rotations2)

# TODO: Test and debug.
