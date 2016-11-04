from scramblecube import *
from solvecorners import *
from test2_for_solvecorners import *

def test_solvecorners():
    cube = scramble(start_cube)
    print('')
    print('SCRAMBLED CUBE:')
    print('')

    print_cube(cube)

    new_cube, rotations = make_a_cross(cube)

    print('')
    print('CUBE WITH CROSS SOLVED:')
    print('')

    print_cube(new_cube)

    for order in range(4):
        res1 = place_corner(new_cube, order)
        new_cube = res1[0]
        rotations += res1[1]
        res2 = fit_top_corner(new_cube, order)
        new_cube = res2[0]
        rotations += res2[1]

        print('NEW CUBE AT THE SOLVING PHASE OF ORDER ' + str(order) + ':')
        print('')
        print_cube(new_cube)
        print('')

        print('ROTATIONS FOR ORDER ' + str(order) + ':')
        print(res1[1] + res2[1])

        print('')
        print('####')
        print('')

    print(str(corners_solved(new_cube)))
    print('')
