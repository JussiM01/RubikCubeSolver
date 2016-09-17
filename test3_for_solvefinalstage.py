from scramblecube import *
from solvefinalstage import *

"""Test which checks that make_correct_edges(cube)[1] and
make_correct_edges(cube)[2] are rotation sequence for which

rotate(turn(rotate(cube, make_correct_edges(cube)[1]), x, 180),
make_correct_edges(cube)[2]) == make_correct_edges(cube)[0]

as they are supposed to be."""

def test_rotations_for_solvefinalstage(num_iter):
    count = 0
    for n in range(num_iter):
        cube = scramble(start_cube)
        output = make_correct_edges(cube)
        new_cube = rotate(turn(rotate(cube, output[1]), x, 180), output[2])
        if output[0] == new_cube: count += 1
    print('Rotations match ' + str(count) + ' out of ' + str(num_iter) + '.')
