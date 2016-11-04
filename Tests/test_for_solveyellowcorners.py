from scramblecube import *
from solveyellowcorners import *
from test2_for_solveyellowcorners import *

def test_solveyellowcorners():
    cube = scramble(start_cube)
    print('')
    print('SCRAMBLED CUBE:')
    print('')

    print_cube(cube)

    new_cube, rotations1, rotations2 = make_yellow_corners(cube)

    print('')
    print('CUBE WITH YELLOW CORNERS SOLVED:')
    print('')

    print_cube(new_cube)

    print(str(yellow_corners_solved(new_cube)))
    print('')
