from scramblecube import *
from solveyellowcorners import *
from test2_for_solve2layers import *

def yellow_corners_solved(cube):
    if not twolayers_solved(cube): return False
    if not yellow_top(cube): return False
    return True

def test_make_yellow_corners(num_iter):
    count = 0
    for n in range(num_iter):
        cube = scramble(start_cube)
        new_cube = make_yellow_corners(cube)[0]
        solved = yellow_corners_solved(new_cube)
        if solved: count += 1
    print('Solved correctly ' + str(count) + ' out of ' + str(num_iter) + '.')
