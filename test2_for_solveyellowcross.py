from scramblecube import *
from solveyellowcross import *
from test2_for_solve2layers import *

def yellow_cross_solved(cube):
    if not twolayers_solved(cube): return False
    if not yellow_cross(cube): return False
    return True

def test_make_a_yellow_cross(num_iter):
    count = 0
    for n in range(num_iter):
        cube = scramble(start_cube)
        new_cube = make_a_2nd_layer(cube)[0]
        solved = yellow_cross_solved(new_cube)
        if solved: count += 1
    print('Solved correctly ' + str(count) + ' out of ' + str(num_iter) + '.')
