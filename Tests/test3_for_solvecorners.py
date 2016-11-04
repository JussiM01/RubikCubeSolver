from scramblecube import *
from solvecorners import *

"""Test which checks that make_a_top_layer(cube)[1] is a rotation sequence for
which

        rotate(cube, make_a_cross(cube)[1]) == make_a_top_layer(cube)[0]

as it is supposed to be."""

def test_rotations_for_solvecorners(num_iter):
    count = 0
    for n in range(num_iter):
        cube = scramble(start_cube)
        output = make_a_top_layer(cube)
        if output[0] == rotate(cube, output[1]): count += 1
    print('Rotations match ' + str(count) + ' out of ' + str(num_iter) + '.')
