from solvecorners import *

left_c_pairs = [('b', 'r'), ('r', 'g'), ('g', 'o'), ('o', 'b')]
right_c_pairs = [('g','r'), ('o', 'g'), ('b', 'o'), ('r', 'b')]

up_edges = [((9, 0, 10), (10, 0, 9)), ((0, 9, 10), (0, 10, 9)),
((-9, 0, 10), (-10, 0, 9)), ((0, -9, 10), (0, -10, 9))]
middle_edges = [((10, 9, 0), (9, 10, 0)), ((-9, 10, 0), (-10, 9, 0)),
    ((-10, -9, 0), (-9, -10, 0,)), ((9, -10, 0), (10, -9, 0))]

r_to_right = ['U', 'R', 'Ui', 'Ri', 'Ui', 'Fi', 'U', 'F']
g_to_right = ['U', 'B', 'Ui', 'Bi', 'Ui', 'Ri', 'U', 'R']
o_to_right = ['U', 'L', 'Ui', 'Li', 'Ui', 'Bi', 'U', 'B']
b_to_right = ['U', 'F', 'Ui', 'Fi', 'Ui', 'Li', 'U', 'L']

r_to_left = ['Ui', 'Li', 'U', 'L', 'U', 'F', 'Ui', 'Fi']
g_to_left = ['Ui', 'Fi', 'U', 'F', 'U', 'R', 'Ui', 'Ri']
o_to_left = ['Ui', 'Ri', 'U', 'R', 'U', 'B', 'Ui', 'Bi']
b_to_left = ['Ui', 'Bi', 'U', 'B', 'U', 'L', 'Ui', 'Li']

up_to_right = [r_to_right, g_to_right, o_to_right, b_to_right]
up_to_left = [r_to_left, g_to_left, o_to_left, b_to_left]

upside_down = turn(start_cube, x, 180)

def correct_middle_edge(cube, edge):
    return {cube[face] == upside_down[face] for face in edge} == {True}

def all_m_edges_correct(cube):
    return {correct_middle_edge(cube, edge) for edge in middle_edges} == {True}

def no_y_in(cube, edge): return 'y' not in {cube[face] for face in edge}

def place_right_edges(cube):
    new_cube, rotations = cube, []
    for i in range(4):
        for edge in up_edges:
            if tuple(cube[face] for face in edge) == right_c_pairs[i]:
                n = up_edges.index(edge) - i
                if n > 0:
                    new_cube = rotate(new_cube, ['U'] * n)
                    rotations += (['U'] * n)
                if n < 0:
                    new_cube = rotate(new_cube, ['Ui'] * -n)
                    rotations += (['Ui']  * -n)
                new_cube = rotate(new_cube, up_to_right[i])
                rotations += up_to_right[i]
    return (new_cube, rotations)

def place_left_edges(cube):
    new_cube, rotations = cube, []
    for i in range(4):
        for edge in up_edges:
            if tuple(cube[face] for face in edge) == left_c_pairs[i]:
                n = up_edges.index(edge) - i
                if n > 0:
                    new_cube = rotate(new_cube, ['U'] * n)
                    rotations += (['U'] * n)
                if n < 0:
                    new_cube = rotate(new_cube, ['Ui'] * -n)
                    rotations += (['Ui']  * -n)
                new_cube = rotate(new_cube, up_to_left[i])
                rotations += up_to_left[i]
    return (new_cube, rotations)

def edge_up(cube):
    for edge in middle_edges:
        if no_y_in(cube, edge) and not correct_middle_edge(cube, edge):
            n = middle_edges.index(edge)
            return (rotate(cube, up_to_right[n]), up_to_right[n])
    return (cube, [])

def make_a_2nd_layer(cube):
    new_cube, rotations1 = make_a_top_layer(cube)
    new_cube, rotations2 = turn(new_cube, x, 180), []
    while not all_m_edges_correct(new_cube):
        step1 = place_right_edges(new_cube)
        new_cube = step1[0]
        rotations2 += step1[1]
        step2 = place_left_edges(new_cube)
        new_cube = step2[0]
        rotations2 += step2[1]
        step3 = edge_up(new_cube)
        new_cube = step3[0]
        rotations2 += step3[1]
    return (new_cube, rotations1, rotations2)
