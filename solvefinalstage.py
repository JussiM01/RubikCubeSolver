from solvecorrectyellowcorners import *

def correct_1(cube): return cube[(-10, 0, 9)] == 'o'
def correct_2(cube): return cube[(0, 10, 9)] == 'g'
def correct_3(cube): return cube[(10, 0, 9)] == 'r'
def correct_4(cube): return cube[(0, -10, 9)] == 'b'

def num_correct_edges(cube):
    return sum([int(correct_1(cube)), int(correct_2(cube)),
        int(correct_3(cube)), int(correct_4(cube))])

clockwise1 = ['F', 'F', 'U', 'L', 'Ri', 'F', 'F', 'Li', 'R', 'U', 'F', 'F']
clockwise2 = ['L', 'L', 'U', 'B', 'Fi', 'L', 'L', 'Bi', 'F', 'U', 'L', 'L']
clockwise3 = ['B', 'B', 'U', 'R', 'Li', 'B', 'B', 'Ri', 'L', 'U', 'B', 'B']
clockwise4 = ['R', 'R', 'U', 'F', 'Bi', 'R', 'R', 'Fi', 'B', 'U', 'R', 'R']

countercw1 = ['F', 'F', 'Ui', 'L', 'Ri', 'F', 'F', 'Li', 'R', 'Ui', 'F', 'F']
countercw2 = ['L', 'L', 'Ui', 'B', 'Fi', 'L', 'L', 'Bi', 'F', 'Ui', 'L', 'L']
countercw3 = ['B', 'B', 'Ui', 'R', 'Li', 'B', 'B', 'Ri', 'L', 'Ui', 'B', 'B']
countercw4 = ['R', 'R', 'Ui', 'F', 'Bi', 'R', 'R', 'Fi', 'B', 'Ui', 'R', 'R']

clockwise = [clockwise1, clockwise2, clockwise3, clockwise4]
countercw = [countercw1, countercw2, countercw3, countercw4]

correct_edge = [correct_1, correct_2, correct_3, correct_4]

def recurse_correct_es(cube, rot1, rot2):
    new_cube, rotations1, rotations2 = cube, rot1, rot2
    n = num_correct_edges(new_cube)
    if n == 4: return (new_cube, rotations1, rotations2)
    if n == 0:
        new_cube = rotate(new_cube, clockwise1)
        rotations2 += clockwise1
        return recurse_correct_es(new_cube, rotations1, rotations2)
    for i in range(4):
        if correct_edge[i]:
            test_cube = rotate(new_cube, clockwise[i])
            if num_correct_edges(test_cube) == 4:
                return (test_cube, rotations1, rotations2 + clockwise[i])
            new_cube = rotate(new_cube, countercw[i])
            rotations2 += countercw[i]
            return (new_cube, rotations1, rotations2)

def make_correct_edges(cube):
    new_cube, rotations1, rotations2 = make_correct_corners(cube)
    return recurse_correct_es(new_cube, rotations1, rotations2)

# TODO: Test and debug.
