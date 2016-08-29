from scramblecube import *
from solvecross import *
from test2_for_solvecross import *

def test_solvecross():
    cube = scramble(start_cube)
    print('')
    print('SCRAMBLED CUBE:')
    print('')

    print_cube(cube)

    new_cube, rotations = cube, []
    for order in range(4):
        new_step = fit_edge(new_cube, order)
        new_cube = new_step[0]
        rotations += new_step[1]

        print('NEW CUBE AT THE SOLVING PHASE OF ORDER ' + str(order) + ':')
        print('')
        print_cube(new_cube)
        print('')

        print('ROTATIONS FOR ORDER ' + str(order) + ':')
        print(new_step[1])

        print('')
        print('####')
        print('')

        print(str(cross_solved(new_cube)))
