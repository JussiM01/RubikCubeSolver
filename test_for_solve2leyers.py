from scramblecube import *
from solve2layers import *
from test2_for_solve2layers import *

def test_solve2leyers():
    cube = scramble(start_cube)
    print('')
    print('SCRAMBLED CUBE:')
    print('')

    print_cube(cube)

    new_cube, rotations1 = make_a_top_layer(cube)

    print('')
    print('CUBE WITH CORNERS SOLVED:')
    print('')

    print_cube(new_cube)

    new_cube, rotations2 = turn(new_cube, x, 180), []

    print('')
    print('CUBE TURNED 180 AROUND X-AXIS:')
    print('')

    print_cube(new_cube)

    for order in range(4):
        res = place_middle_edges(new_cube, order)
        new_cube = res[0]
        rotations2 += res[1]

        print('NEW CUBE AT THE SOLVING PHASE OF ORDER ' + str(order) + ':')
        print('')
        print_cube(new_cube)
        print('')

        print('ROTATIONS FOR ORDER ' + str(order) + ':')
        print(res[1])

        print('')
        print('####')
        print('')

    print(str(corners_solved(new_cube)))
    print('')
