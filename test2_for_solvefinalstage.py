from scramblecube import *
from solvefianlstage import *
from test2_for_solve2layers import *

def cube_solved(cube):
    if {cube[p] == 'r' for p in front} != {True}: return False
    if {cube[p] == 'b' for p in left} != {True}: return False
    if {cube[p] == 'o' for p in back} != {True}: return False
    if {cube[p] == 'g' for p in right} != {True}: return False
    if {cube[p] == 'y' for p in up} != {True}: return False
    if {cube[p] == 'w' for p in down} != {True}: return False
    return True

def test_make_correct_edges(num_iter):
    count = 0
    for n in range(num_iter):
        cube = scramble(start_cube)
        new_cube = make_correct_edges(cube)[0]
        solved = cube_solved(new_cube)
        if solved: count += 1
    print('Solved correctly ' + str(count) + ' out of ' + str(num_iter) + '.')
