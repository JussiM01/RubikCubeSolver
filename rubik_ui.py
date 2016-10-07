from pointsandrotations import *
from sidesandprinting import *
from scramblecube import *
from solvingstatecheck import *

"""Temporary user interface. To be replaced with a graphical version."""

print('Give the colors of the stickers in your cube as follows:')
print('')
print('Each side is represented as a 9 character string where single')
print('character represents a color of the given square.')
print('')
print('For the front, left, back and right sides the indexing starts from')
print('the top most square on the left corner of the given side.')
print('')
print('For the top side, it starts from the corner which touches the left side')
print('and the back side.')
print('')
print('And for the bottom side from the corner which touches the left side')
print('and the front side.')
print('')
print('Colors are reperesented as follows: r, g, o, b, w, y (which stand')
print('for: red, green, orange, blue, white and yellow).')
print('')
print('Example: the string "gggooorrr" represents a side where first row')
print('is green, second row is orange and third row is red.')
print('')
print('This program can also scramble a cube for you.')
print('')
print('Do you want to give your own cube settings or let us give you a cube?')
print('')

answer = input("Write 'y' if you use your own cube and 'n' if otherwiswe : ")

print('')

while answer not in {'y', 'n'}:
    answer = input("Please try again. Write 'y' or 'n' (without citation): ")

def proper_char(char): return char in {'r', 'g', 'o', 'b', 'w', 'y'}

def proper_side_string(side_str):
    if len(side_str) != 9: return False
    if {proper_char(side_str[i]) for i in range(9)} != {True}: return False
    return True

def s_input(request1, request2):
    side_str = input(request1)
    while not proper_side_string(side_str):
        side_str = input(request2)
    return side_str

def ask_input():
    users_cube = {}
    request = 'Please try again. String of 9 characters (g, r, o, b, w, y): '
    front_string = s_input('Give the string for the front side: ', request)
    left_string = s_input('Same for the left side: ', request)
    back_string = s_input('Same for the back side: ', request)
    right_string = s_input('Same for the right side: ', request)
    top_string = s_input('Same for the top side: ', request)
    bottom_string = s_input('Same for the bottom side: ', request)

    side_strings = [front_string, left_string, back_string, right_string,
        top_string, bottom_string]

    for n in range(6):
        for m in range(9): users_cube[sides[n][m]] = side_strings[n][m]
    return users_cube

if answer == 'y':
    cube = ask_input()
elif answer == 'n':
    cube = scramble(start_cube)

print('')
print('So your cube looks like this:')
print('')

print_cube(cube)

s_state = check_state(cube)
cube = s_state[0]
state_num = s_state[1]
last_rot_num1 = 0
last_rot_num2 = 0

solver_functions = [make_correct_edges, make_correct_corners,
    make_yellow_corners, make_a_yellow_cross, make_a_2nd_layer,
    make_a_top_layer, make_a_cross]

while state_num != 0: # state_num should maybe checked in the loop?
# Since some steps might be unnecessary (if more gets solved in one step).
    if answer == 'y' and state_num == 4:
        print('You should now turn the cube upside down. That is, white side')
        print('should be on the bottom, yellow center on the top, and red rows')
        print('should be to two lowest rows on the front side.')
    if answer == 'n' and state_num == 4:
        print('The cube will be now turned upside down.')

    print('You currently have ' + string_rep[state_num] + ' solved.')
    print('Do you want the instructions for next stage?')
    print("Write 'y' if you want instructions for the next stage.")
    print('Any other key will let you to exit this program.')
    reply = input('Write your answer here: ')

    if reply == 'y':
        solver = solver_functions[state_num - 1]
        if state_num < 5:
            cube = start_orientation(cube)
        next_step = solver(cube)
        cube = next_step[0]
        if state_num > 4: # Is this correct?
            instructions = next_step[1][last_rot_num1:] # Check that this is
            last_rot_num1 += len(instructions) # correct.
        else:
            instructions = next_step[2][last_rot_num2:] # Same here.
            last_rot_num2 += len(instructions)
        state_num -= 1

        print('Rotations for the next stage are:')
        print('')
        rot_string = ', '.join(instructions)
        print(rot_string)

        print('')
        print('After doing these rotations your cube should look like this:')
        if state_num < 4:
            print_cube(cube)
        else:
            print_cube(start_orientation(cube))
        print('')

    else: exit(0)

print('Gongratulations! You have solved the cube.')

# TODO: Test and debug.
