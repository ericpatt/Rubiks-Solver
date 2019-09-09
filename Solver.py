# import cv2
import pickle
import numpy as np
from FaceletModel import FaceletModel
from CubieModel import CubieModel
from RubiksModel import RubiksModel
from copy import deepcopy
# import serial
import time
# import pyximport; pyximport.install()

# draw_after_moves = True

# b, g, r, o, y, w
# ideal_colors = [(255, 50, 0), (0, 255, 0), (0, 0, 255), (0, 140, 255), (0, 235, 235), (255, 255, 255)]
# sticker_colors = [(230, 109, 1), (75, 210, 0), (19, 35, 189), (38, 79, 215), (39, 218, 187), (187, 194, 195)]

phase1_moves = ["b", "b'", "b2", "g", "g'", "g2", "r", "r'", "r2", "o", "o'", "o2", "y", "y'", "y2", "w", "w'", "w2"]
phase2_moves = ["b", "b'", "b2", "g", "g'", "g2", "r2", "o2", "y2", "w2"]

p1_edge_prune = np.full(2048, -1)
p1_corner_prune = np.full(2187, -1)
p1_ud_prune = np.full(496, -1)

solved_cube = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5]

facelet_model = FaceletModel(solved_cube)

cubie_model = CubieModel()

current_cube = RubiksModel(facelet_model, cubie_model)

max_length = 30
current_depth = 0

# def set_face_from_image(face_img, face_ind):
#     image = cv2.imread(face_img)
#     image = imutils.resize(image, width=500)
#     (h, w, d) = image.shape
#     # cv2.imshow("Image", image)
#     # cv2.waitKey(0)
#
#     output = image.copy()
#     yi = 0
#     y = h // 6
#     while y < h:
#         xi = 0
#         x = w // 6
#         while x < w:
#             (b, g, r) = image[y, x]
#             cv2.circle(output, (x, y), 5, (230, 90, 255), -1)
#             (b1, g1, r1) = sticker_colors[0]
#             min_diff = abs(r1 - r) + abs(g1 - g) + abs(b1 - b)
#             minind = 0
#             for i in range(1, len(sticker_colors)):
#                 (b1, g1, r1) = sticker_colors[i]
#                 diff = abs(r1 - r) + abs(g1 - g) + abs(b1 - b)
#                 if diff < min_diff:
#                     min_diff = diff
#                     minind = i
#              faces[face_ind][yi][xi] = minind
#             x += w // 3
#             xi += 1
#         y += h // 3
#         yi += 1
#     # print(faces[sideind])
#     # cv2.imshow("Circle", output)
#     # cv2.waitKey(0)


# def draw_cube():
#     i = 0
#     x_offset = 104
#     y_offset = 104
#     while i < 54:
#         for y in range(3):
#             for x in range(3):
#                 cv2.rectangle(cube_image, (x_offset + 33 * x, y_offset + 33 * y), (x_offset + 33 * (x + 1), y_offset + 33 * (y + 1)), ideal_colors[int(current_cube_state.get(i))], -1)
#                 cv2.rectangle(cube_image, (x_offset + 33 * x, y_offset + 33 * y), (x_offset + 33 * (x + 1), y_offset + 33 * (y + 1)), (0, 0, 0), 2)
#                 i += 1
#         if i == 9:
#             x_offset = 104
#             y_offset = 308
#         elif i == 18:
#             x_offset = 206
#             y_offset = 104
#         elif i == 27:
#             x_offset = 2
#             y_offset = 104
#         elif i == 36:
#             x_offset = 104
#             y_offset = 2
#         elif i == 45:
#             x_offset = 104
#             y_offset = 206
#
#     cv2.destroyAllWindows()
#     cv2.imshow("cube", cube_image)


# def set_all_faces_from_images():
#     for i in range(len(faces)):
#         set_face_from_image(cube_face_images[i], i)
#
#
# def set_solved_cube():
#     count = 0
#     for face in faces:
#         for x in range(len(face)):
#             for y in range(len(face[0])):
#                 face[x][y] = count
#         count += 1


# def take_input(prompt=""):
#     print(prompt)
#     alg = input()
#     moves = alg.split()
#     for temp in moves:
#         current_cube_state.move(temp)
#         draw_cube()
#         cv2.waitKey(200)

def is_solved(state):
    return state == solved_cube


def valid_moves(prev_move):
    if len(prev_move) == 0:
        return phase1_moves

    invalid = []
    if prev_move[0] == "b" or prev_move[0] == "b'" or prev_move[0] == "b2":
        invalid = ["b", "b'", "b2"]
    elif prev_move[0] == "g" or prev_move[0] == "g'" or prev_move[0] == "g2":
        invalid = ["g", "g'", "g2", "b", "b'", "b2"]
    elif prev_move[0] == "r" or prev_move[0] == "r'" or prev_move[0] == "r2":
        invalid = ["r", "r'", "r2"]
    elif prev_move[0] == "o" or prev_move[0] == "o'" or prev_move[0] == "o2":
        invalid = ["o", "o'", "o2", "r", "r'", "r2"]
    elif prev_move[0] == "y" or prev_move[0] == "y'" or prev_move[0] == "y2":
        invalid = ["y", "y'", "y2"]
    elif prev_move[0] == "w" or prev_move[0] == "w'" or prev_move[0] == "w2":
        invalid = ["w", "w'", "w2", "y", "y'", "y2"]
    return [m for m in phase1_moves if m not in invalid]


def pruning_helper(cube, depth, max_depth):
    depth += 1
    for m in phase1_moves:
        c = deepcopy(cube)
        c.move(m)
        coords = c.phase1_coords()
        if p1_corner_prune[coords[0]] == -1:
            p1_corner_prune[coords[0]] = depth
        if p1_edge_prune[coords[1]] == -1:
            p1_edge_prune[coords[1]] = depth
        if p1_ud_prune[coords[2]] == -1:
            p1_ud_prune[coords[2]] = depth
        if depth < max_depth:
            pruning_helper(c, depth, max_depth)


def generate_pruning_tables(depth):
    p1_corner_prune[0] = 0
    p1_edge_prune[0] = 0
    p1_ud_prune[0] = 0
    pruning_helper(current_cube, 0, depth)
    pickle.dump(p1_corner_prune, open("p1_corner_pruning_table.p", "wb"))
    pickle.dump(p1_edge_prune, open("p1_edge_pruning_table.p", "wb"))
    pickle.dump(p1_ud_prune, open("p1_ud_pruning_table.p", "wb"))


def load_pruning_tables():
    global p1_corner_prune, p1_edge_prune, p1_ud_prune
    p1_corner_prune = pickle.load(open("p1_corner_pruning_table.p", "rb"))
    p1_edge_prune = pickle.load(open("p1_edge_pruning_table.p", "rb"))
    p1_ud_prune = pickle.load(open("p1_ud_pruning_table.p", "rb"))


def check_pruning_tables():
    count = 0
    for i in range(len(p1_corner_prune)):
        if p1_corner_prune[i] != -1:
            count += 1
    print("corner table:", count)
    count = 0
    for i in range(len(p1_edge_prune)):
        if p1_edge_prune[i] != -1:
            count += 1
    print("edge table:", count)
    count = 0
    for i in range(len(p1_ud_prune)):
        if p1_ud_prune[i] != -1:
            count += 1
    print("ud table:", count)


def phase1_search(cube, moves_made, depth):
    if depth <= 0:
        # print(moves_made)
        # print(cube.get_state())
        if cube.phase1_coords() == (0, 0, 0) and (len(moves_made) == 0 or moves_made[-1] in ["r", "r'", "o", "o'", "y", "y'", "w", "w'"]):
            return moves_made
            # return phase2_start(cube, moves_made, depth)
        return None

    valid = phase1_moves

    if len(moves_made) > 0:
        valid = valid_moves(moves_made[-1])

    solutions = []

    (c1, c2, c3) = cube.phase1_coords()

    if max(p1_corner_prune[c1], p1_edge_prune[c2], p1_ud_prune[c3]) <= depth:
        for m in valid:
            next_cube = deepcopy(cube)
            next_cube.move(m)
            moves_made.append(m)
            possible_solution = phase1_search(next_cube, deepcopy(moves_made), depth - 1)
            if possible_solution is not None:
                solutions.append(possible_solution)
            del moves_made[-1]

    shortest_solution = None
    shortest_len = 100

    for sol in solutions:
        if len(sol) < shortest_len:
            shortest_solution = sol
            shortest_len = len(sol)

    return shortest_solution


def phase2_search(cube, moves_made, depth):
    if depth <= 0:
        # print(moves_made)
        # print(cube.get_state())
        if is_solved(cube.get_facelets().get_state()):
            return moves_made
        return None

    valid = phase2_moves

    # if len(moves_made) > 0:
    #     valid = valid_moves(moves_made[-1])

    solutions = []

    for m in valid:
        next_cube = deepcopy(cube)
        next_cube.move(m)
        moves_made.append(m)
        possible_solution = phase2_search(next_cube, deepcopy(moves_made), depth - 1)
        if possible_solution is not None:
            solutions.append(possible_solution)
        del moves_made[-1]

    shortest_solution = None
    shortest_len = 100

    for sol in solutions:
        if len(sol) < shortest_len:
            shortest_solution = sol
            shortest_len = len(sol)

    return shortest_solution


def kociemba_start():
    for depth in range(max_length):
        print("Phase 1, depth:", depth)
        solution = phase1_search(current_cube, [], depth)
        if solution is not None:
            print("solution found:", solution)
            break


def phase2_start(cube, prev_moves, d):
    print(prev_moves)
    for depth in range(max_length - d):
        print("Phase 2, depth:", depth)
        solution = phase2_search(cube, prev_moves, depth)
        if solution is not None:
            return solution


def scramble(moves):
    moves = moves.split()
    for m in moves:
        current_cube.move(m)


def main():
    # draw_cube()
    # cv2.waitKey()

    # take_input("Input the scramble for the cube")
    # b2 y' r g o2 y r g b' g r2 o' b

    # take_input("Input the solution for the cube")
    # b' o r2 g' b g' r' y' o2 g' r' y b2

    # print(search(current_cube_state, [], 2))

    start_time = time.time()

    load_pruning_tables()

    print("Runtime to generate tables: {}".format(time.time() - start_time))

    check_pruning_tables()
    print(p1_corner_prune)
    print(p1_edge_prune)
    print(p1_ud_prune)

    scramble("b2 r' w2 g y'")

    start_time = time.time()

    kociemba_start()

    print("Runtime: {}".format(time.time() - start_time))

    # ser = serial.Serial('COM4', 9600)
    #
    # time.sleep(1)
    #
    # print("sending now")
    #
    # while True:
    #     ser.write(b'b')
    #
    #     time.sleep(0.5)
    #
    #     ser.write(b'B')
    #
    #     time.sleep(1)


main()


