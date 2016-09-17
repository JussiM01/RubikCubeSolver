from scramblecube import *
from solvefinalstage import *
from test2_for_solvefinalstage import *

def test_solvefinalstage():
    cube = scramble(start_cube)
    print('')
    print('SCRAMBLED CUBE:')
    print('')

    print_cube(cube)

    new_cube, rotations1, rotations2 = make_correct_edges(cube)

    print('')
    print('CUBE CORRECTLY SOLVED:')
    print('')

    print_cube(new_cube)

    print(str(cube_solved(new_cube)))
    print('')
