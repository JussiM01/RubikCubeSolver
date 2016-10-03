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

# print: you currently have (solving state) solved
# print: do you want instruction for the next state?
# if yes print them and how the cube should look after that
# repeat until solved.
