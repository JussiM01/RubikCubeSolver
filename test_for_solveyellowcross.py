from scramblecube import *
from solveyellowcross import *
from test2_for_solveyellowcross import *

def test_solveyellowcross():
    cube = scramble(start_cube)
    print('')
    print('SCRAMBLED CUBE:')
    print('')

    print_cube(cube)

    new_cube, rotations1, rotations2 = make_a_2nd_layer(cube)

    print('')
    print('CUBE WITH 2 LAYERS SOLVED:')
    print('')

    print_cube(new_cube)

    new_cube, rotations1, rotations2 = make_a_yellow_cross(new_cube)

    print('')
    print('CUBE WITH YELLOW CROSS SOLVED:')
    print('')

    print(str(yellow_cross_solved(new_cube)))
    print('')
