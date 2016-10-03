from pointsandrotations import *
from sidesandprinting import *
# from solvingstatecheck import * # CHANGE THIS BACK WHEN DEBUGGED.

"""Temporary user interface. To be replaced with a graphical version."""

cube = {}

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
print('Now, choose the front side.')

##### Here should be a block which asks the user if he/she wants to use own
# cube or let the program to scramble a cube for him/her. #####

# the followin code should be then inside a function which is only executed
# if the answer is yes.

# Add also code that checks wheter the input is in correct format?

front_string = input('Give the string representation of the front side:')
left_string = input('Same for the left side:')
back_string = input('Same for the back side:')
right_string = input('Same for the right side:')
top_string = input('Same for the top side:')
bottom_string = input('Same for the bottom side:')

side_strings = [front_string, left_string, back_string, right_string,
    top_string, bottom_string]

for n in range(6):
    for m in range(9): cube[sides[n][m]] = string_rep[n][m]

# (end of the function, which returns the cube.)

print('So your cube looks like this:')

print_cube(cube)

# print: you currently have (solving state) solved
# print: do you want instruction for the next state?
# if yes print them and how the cube should look after that
# repeat until solved.
