from solvecorners import *

left_c_pairs = [('b', 'r'), ('r', 'g'), ('g', 'o'), ('o', 'b')]
right_c_pairs = [('g','r'), ('o', 'g'), ('b', 'o'), ('r', 'b')]
# outer_colors = ['g', 'o', 'b', 'r'] # SHOULD THESE BE CHANGED ?

# up_edges = [((-9, 0, 10), (-10, 0, 9)), ((0, -9, 10), (0, -10, 9)),
#     ((9, 0, 10), (10, 0, 9)), ((0, 9, 10), (0, 10, 9))]
middle_edges = [((10, 9, 0), (9, 10, 0)), ((-9, 10, 0), (-10, 9, 0)),
    ((-10, -9, 0), (-9, -10, 0,)), ((9, -10, 0), (10, -9, 0))]
# outer_faces = {p for p in points if p[z] not in [-10, 10]}

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

# def outer_color_fits(cube, edge, order):
#     return ({cube[face] for face in edge if face in outer_faces}
#         == {outer_colors[order]})

def correct_middle_edge(cube, edge):
    return {cube[face] == upside_down[face] for face in edge} == {True}

def all_m_edges_correct(cube):
    return {correct_middle_edge(cube, edge) for edge in middle_edges} == {True}

def no_y_in(cube, edge): return 'y' not in {cube[face] for face in edge}

# def suited_colors(cube, edge, order):
#     return (outer_colors[order] in {cube[face] for face in edge}
#         and no_y_in(cube, edge))

# def edge_to_middle(cube, edge, order):
#     ind1, ind2 = (order + 1) % 4, order - 1
#     rot_sequence1 = (['U'] + side_rot[ind1] + ['Ui'] + side_inv[ind1] + ['Ui']
#         + side_inv[order] + ['U'] + side_rot[order])
#     rot_sequence2 = (['Ui'] + side_inv[ind2] + ['U'] + side_rot[ind2] + ['U']
#         + side_rot[order] + ['Ui'] + side_inv[order])
#     tmp1, tmp2 = rotate(cube, rot_sequence1), rotate(cube, rot_sequence2)
#     if correct_middle_edge(tmp1, middle_edges[ind1]):
#         return (tmp1, rot_sequence1)
#     if correct_middle_edge(tmp2, middle_edges[order]):
#         return (tmp2, rot_sequence2)
#     return (cube, [])
#
# def middle_edge_up(cube, edge):
#     n = middle_edges.index(edge)
#     rot_sequence = (['U'] + side_rot[n] + ['Ui'] + side_inv[n] + ['Ui']
#         + side_inv[n - 1] + ['U'] + side_rot[n - 1]) # IS THIS CORRECT ?
#     return (rotate(cube, rot_sequence), rot_sequence)
#
# def top_edge_to_inline(cube, edge, order):
#     new_cube, rotations = cube, []
#     n = order - up_edges.index(edge) # Notice: up_edges, not top_edges
#     if n > 0:
#         new_cube = rotate(new_cube, ['U'] * n)
#         rotations += (['U'] * n)
#     if n < 0:
#         new_cube = rotate(new_cube, ['Ui'] * -n)
#         rotations += (['Ui']  * -n)
#     return (new_cube, rotations)

# def place_middle_edges(cube, order):
#     new_cube, rotations = cube, []
#     for edge in up_edges: # Notice: up_edges, not top_edges
#         if outer_color_fits(new_cube, edge, order) and no_y_in(new_cube, edge):
#             print('1') # FOR DEBUGGING
#             step = top_edge_to_inline(new_cube, edge, order)
#             new_cube = step[0]
#             rotations += step[1]
#             res1 = edge_to_middle(new_cube, edge, order)
#             new_cube = res1[0]
#             rotations += res1[1]
#     for edge in middle_edges:
#         if no_y_in(new_cube, edge):
#             print('2a') # FOR DEBUGGING
#             if not correct_middle_edge(new_cube, edge):
#                 print('2b') # FOR DEBUGGING
#                 res2 = middle_edge_up(new_cube, edge)
#                 new_cube = res2[0]
#                 rotations += res2[1]
#                 return (new_cube, rotations)
#     return (new_cube, rotations)

def place_right_edges(cube):
    new_cube, rotations = cube, []
    for i in range(4):
        for edge in top_edges:
            if tuple(cube[face] for face in edge) == right_c_pairs[i]:
                n = i - top_edges.index(edge)
                if n > 0:
                    new_cube = rotate(new_cube, ['D'] * n)
                    rotations += (['D'] * n)
                if n < 0:
                    new_cube = rotate(new_cube, ['Di'] * -n)
                    rotations += (['Di']  * -n)
                new_cube = rotate(new_cube, up_to_right[i])
                rotations += up_to_right[i]
    return (new_cube, rotations)

def place_left_edges(cube):
    new_cube, rotations = cube, []
    for i in range(4):
        for edge in top_edges:
            if tuple(cube[face] for face in edge) == left_c_pairs[i]:
                n = i - top_edges.index(edge)
                if n > 0:
                    new_cube = rotate(new_cube, ['D'] * n)
                    rotations += (['D'] * n)
                if n < 0:
                    new_cube = rotate(new_cube, ['Di'] * -n)
                    rotations += (['Di']  * -n)
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
        # for order in range(4):
        #     res = place_middle_edges(new_cube, order)
        #     new_cube = res[0]
        #     rotations2 += res[1]
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

# TODO: Test and debug.
