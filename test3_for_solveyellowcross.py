from scramblecube import *
from solveyellowcross import *

"""Test which checks that make_a_yellow_cross(cube)[1] and
make_a_yellow_cross(cube)[2] are rotation sequence for which

rotate(turn(rotate(cube, make_a_yellow_cross(cube)[1]), x, 180),
make_a_yellow_cross(cube)[2]) == make_a_yellow_cross(cube)[0]

as they are supposed to be."""

def test_rotations_for_solveyellowcross(num_iter):
    count = 0
    for n in range(num_iter):
        cube = scramble(start_cube)
        output = make_a_yellow_cross(cube)
        new_cube = rotate(turn(rotate(cube, output[1]), x, 180), output[2])
        if output[0] == new_cube: count += 1
    print('Rotations match ' + str(count) + ' out of ' + str(num_iter) + '.')
