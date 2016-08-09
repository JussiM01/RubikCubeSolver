from rubiksolver import *
from rotationtest import *
from solvingstatecheck import *

"""Temporary user interface. To be replaced with a graphical version."""

cube = {}

print('Give the colors of the stickers in your cube as follows:')
print('Each side is represented as a 9 character string where single')
print('character represents a color of the given square starting from')
print('top most square on the left corner for front side, left side,')
print('back side and right side. And for the top side, from the corner which')
print('touches the left side and the back side. And for the bottom side')
print('from the corner which touches the left side and the front side.')
print('Colors are reperesented as follows: r, g, o, b, w, y (which stand')
print('for: red, green, orange, blue, white and yellow).')
print('Example: the string "gggooorrr" represents a side where first row')
print('is green, second row is orange and third row is red.')
print('')
print('Now, choose the front side.')

front_string = input('Give the string representation of the front side:')
left_string = input('Same for the left side:')
back_string = input('Same for the back side:')
right_string = input('Same for the right side:')
top_string = input('Same for the top side:')
bottom_string = input('Same for the bottom side:')

string_pres = [front_string, left_string, back_string, right_string, top_string,
    bottom_string]

for n in range(6):
    for m in range(9): cube[sides[n][m]] = string_pres[n][m]
