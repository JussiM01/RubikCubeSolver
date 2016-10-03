from pointsandrotations import *
from sidesandprinting import *
from scramblecube import *
# from solvingstatecheck import * # CHANGE THIS BACK WHEN DEBUGGED.

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

answer = input("Write 'y' if you use your own cube and 'n' if otherwiswe :")

while answer not in {'y', 'n'}:
    answer = input("Please try again. Write 'y' or 'n' (without citation): ")

def ask_input():
    users_cube = {}
    print('Now, choose the front side.')
    front_string = input('Give the string representation of the front side:')
    left_string = input('Same for the left side:')
    back_string = input('Same for the back side:')
    right_string = input('Same for the right side:')
    top_string = input('Same for the top side:')
    bottom_string = input('Same for the bottom side:')

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

# print: you currently have (solving state) solved
# print: do you want instruction for the next state?
# if yes print them and how the cube should look after that
# repeat until solved.
