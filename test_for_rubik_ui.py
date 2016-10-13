from pointsandrotations import *
from sidesandprinting import *
from scramblecube import *
from solvingstatecheck import *

def test_ui(num):
    results = []
    for i in range(num):
        cube = scramble(start_cube)
        state_num = 7 # Default: cube scrambled.
        count = 0 # How many times a state lower than 5 is countered.

        solver_functions = [make_correct_edges, make_correct_corners,
            make_yellow_corners, make_a_yellow_cross, make_a_2nd_layer,
            make_a_top_layer, make_a_cross]

        while state_num != 0:
            s_state = check_state(cube)
            cube = s_state[0]
            state_num = s_state[1]
            if state_num == 0:
                break
            solver = solver_functions[state_num - 1]
            if state_num < 5:
                cube = start_orientation(cube)
            next_step = solver(cube)
            old_cube = cube
            cube = next_step[0]
            if state_num > 4:
                instructions = next_step[1]
                test_cube = rotate(old_cube, instructions, [])
            else:
                instructions = next_step[2]
                test_cube = rotate(turn(old_cube, x, 180), [], instructions)
            results.append(cube == test_cube)
    return # Number of (num True) out of num iterations.

# TODO: Test and debug.
