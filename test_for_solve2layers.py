from scramblecube import *
from solve2layers import *
from test2_for_solve2layers import *

def test_solve2layers():
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

    for i in range(10):
    # while not al_m_edges_correct(new_cube):
        # for order in range(4):
        #     res = place_middle_edges(new_cube, order)
        #     new_cube = res[0]
        #     rotations2 += res[1]
        step1 = place_right_edges(new_cube)
        new_cube = step1[0]
        rotations2 += step1[1]

        print('NEW CUBE AFTER 1ST STEP:')
        print('')
        print_cube(new_cube)
        print('')

        print('ROTATIONS:')
        print(step1[1])

        print('')
        print('####')
        print('')

        step2 = place_left_edges(new_cube)
        new_cube = step2[0]
        rotations2 += step2[1]

        print('NEW CUBE AFTER 2ND STEP:')
        print('')
        print_cube(new_cube)
        print('')

        print('ROTATIONS:')
        print(step2[1])

        print('')
        print('####')
        print('')

        step3 = edge_up(new_cube)
        new_cube = step3[0]
        rotations2 += step3[1]

        print('NEW CUBE AFTER 3RD STEP:')
        print('')
        print_cube(new_cube)
        print('')

        print('ROTATIONS:')
        print(step3[1])

        print('')
        print('####')
        print('')

    print(str(twolayers_solved(new_cube)))
    print('')
