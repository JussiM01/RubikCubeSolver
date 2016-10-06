from sidesandprinting import *
from pointsandrotations import *
from solvefinalstage import *

def cube_solved(cube):
    if {cube[p] == 'r' for p in front} != {True}: return False
    if {cube[p] == 'b' for p in left} != {True}: return False
    if {cube[p] == 'o' for p in back} != {True}: return False
    if {cube[p] == 'g' for p in right} != {True}: return False
    if {cube[p] == 'y' for p in up} != {True}: return False
    if {cube[p] == 'w' for p in down} != {True}: return False
    return True

def cross_solved(cube):
    if not white_cross_up(cube): return False
    if not blue_pieces(cube): return False
    if not orange_pieces(cube): return False
    if not green_pieces(cube): return False
    if not red_pieces(cube): return False
    return True

up_cross = {(0, 0, 10), (0, 9, 10), (-9, 0, 10), (0, -9, 10), (9, 0, 10)}
segment_R = {(0, 10, 9), (0, 10, 0)}
segment_B = {(-10, 0, 9), (-10, 0, 0)}
segment_L = {(0, -10, 9), (0, -10, 0)}
segment_F = {(10, 0, 9), (10, 0, 0)}

def white_cross_up(cube): return {cube[p] for p in up_cross} == {'w'}
def blue_pieces(cube): return {cube[p] for p in segment_R} == {'b'}
def orange_pieces(cube): return {cube[p] for p in segment_B} == {'o'}
def green_pieces(cube): return {cube[p] for p in segment_L} == {'g'}
def red_pieces(cube): return {cube[p] for p in segment_F} == {'r'}

def corners_solved(cube):
    if not white_side_up(cube): return False
    if not blue_triangle(cube): return False
    if not orange_triangle(cube): return False
    if not green_triangle(cube): return False
    if not red_triangle(cube): return False
    return True

triangle_R = {(9, 10, 9), (0, 10, 9), (-9, 10, 9), (0, 10, 0)}
triangle_B = {(-10, 9, 9), (-10, 0, 9), (-10, -9, 9), (-10, 0, 0)}
triangle_L = {(-9, -10, 9), (0, -10, 9), (9, -10, 9), (0, -10, 0)}
triangle_F = {(10, -9, 9), (10, 0, 9), (10, 9, 9), (10, 0, 0)}

def white_side_up(cube): return {cube[p] for p in up} == {'w'}
def blue_triangle(cube): return {cube[p] for p in triangle_R} == {'b'}
def orange_triangle(cube): return {cube[p] for p in triangle_B} == {'o'}
def green_triangle(cube): return {cube[p] for p in triangle_L} == {'g'}
def red_triangle(cube): return {cube[p] for p in triangle_F} == {'r'}

def twolayers_solved(cube):
    if not white_side_down(cube): return False
    if not green_2layers(cube): return False
    if not orange_2layers(cube): return False
    if not blue_2layers(cube): return False
    if not red_2layers(cube): return False
    return True

twolayers_R = {p for p in points if p[y] == 10 and p[z] < 9}
twolayers_B = {p for p in points if p[x] == -10 and p[z] < 9}
twolayers_L = {p for p in points if p[y] == -10 and p[z] < 9}
twolayers_F = {p for p in points if p[x] == 10 and p[z] < 9}

def white_side_down(cube): return {cube[p] for p in down} == {'w'}
def green_2layers(cube): return {cube[p] for p in twolayers_R} == {'g'}
def orange_2layers(cube): return {cube[p] for p in twolayers_B} == {'o'}
def blue_2layers(cube): return {cube[p] for p in twolayers_L} == {'b'}
def red_2layers(cube): return {cube[p] for p in twolayers_F} == {'r'}

solved_state = [cube_solved, correct_yellow_corners, yellow_top, yellow_cross,
    twolayers_solved, corners_solved, cross_solved]

string_rep = ['the cube', 'correct yellow corners', 'yellow top',
    'yellow cross', 'two layers', 'white corners', 'white cross',
    'not yet any state']

def start_orientation(cube):
    for deg1 in [0, 90, 180, 270]:
        for deg2 in [0, 90, 180, 270]:
            turned = turn(turn(cube, x, deg1), y, deg2)
            if turned[(10, 0, 0)] == 'r' and turned[(0, 0, 10)] == 'w':
                return turned

def check_state(cube):
    for deg1 in [0, 90, 180, 270]:
        for deg2 in [0, 90, 180, 270]:
            for i in range(7):
                turned = turn(turn(cube, x, deg1), y, deg2)
                if solved_state[i](turned): return (turned, i)
    return (start_orientation(turned), 7)

# TODO: Test and debug.
