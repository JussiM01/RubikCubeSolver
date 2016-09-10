from solve2layers import *

def yellow_cross(cube): return {cube[p] for p in up_cross} == {'y'}
def yellow_angle_back_left(cube): return {cube[p] for p in b_left} == {'y'}
def yellow_angle_back_right(cube): return {cube[p] for p in b_right} == {'y'}
def yellow_angle_front_left(cube): return {cube[p] for p in f_left} == {'y'}
def yellow_angle_front_right(cube): return {cube[p] for p in f_right} == {'y'}
def yellow_line_horizontal(cube): return {cube[p] for p in horizontal} = {'y'}
def yellow_line_vertical(cube): return {cube[p] for p in vertical} = {'y'}



def make_a_yellow_cross(cube):
    new_cube, rotations1, rotations2 = make_a_2nd_layer(cube)
    if yellow_cross(new_cube): return (new_cube, rotations1, rotations2)
    if
