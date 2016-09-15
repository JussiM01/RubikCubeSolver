from scramblecube import *
from solvecorrectyellowcorners import *
from test2_for_solvecorrectyellowcorners import *

def test_solvecorrectyellowcorners():
    cube = scramble(start_cube)
    print('')
    print('SCRAMBLED CUBE:')
    print('')

    print_cube(cube)

    new_cube, rotations1, rotations2 = make_correct_corners(cube)

    print('')
    print('CUBE WITH CORRECT YELLOW CORNERS SOLVED:')
    print('')

    print_cube(new_cube)

    print(str(correct_corners_solved(new_cube)))
    print('')
