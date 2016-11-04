from scramblecube import *
from solveyellowcorners import *

"""Test which checks that make_yellow_corners(cube)[1] and
make_yellow_corners(cube)[2] are rotation sequence for which

rotate(turn(rotate(cube, make_yellow_corners(cube)[1]), x, 180),
make_yellow_corners(cube)[2]) == make_yellow_corners(cube)[0]

as they are supposed to be."""

def test_rotations_for_solveyellowcorners(num_iter):
    count = 0
    for n in range(num_iter):
        cube = scramble(start_cube)
        output = make_yellow_corners(cube)
        new_cube = rotate(turn(rotate(cube, output[1]), x, 180), output[2])
        if output[0] == new_cube: count += 1
    print('Rotations match ' + str(count) + ' out of ' + str(num_iter) + '.')
