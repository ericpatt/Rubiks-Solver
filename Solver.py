import cv2
import numpy as np
from FaceletModel import FaceletModel
from copy import deepcopy
import serial
import time


draw_after_moves = True

# b, g, r, o, y, w
ideal_colors = [(255, 50, 0), (0, 255, 0), (0, 0, 255), (0, 140, 255), (0, 235, 235), (255, 255, 255)]
sticker_colors = [(230, 109, 1), (75, 210, 0), (19, 35, 189), (38, 79, 215), (39, 218, 187), (187, 194, 195)]

cube_face_images = ["b.jpg", "g.jpg", "r.jpg", "o.jpg", "y.jpg", "w.jpg"]

all_moves = ["b", "b'", "b2", "g", "g'", "g2", "r", "r'", "r2", "o", "o'", "o2", "y", "y'", "y2", "w", "w'", "w2"]

cube_image = np.zeros((410, 308, 3), np.uint8)

solved_cube = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5]

current_cube_state = FaceletModel(solved_cube)


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


def draw_cube():
    i = 0
    x_offset = 104
    y_offset = 104
    while i < 54:
        for y in range(3):
            for x in range(3):
                cv2.rectangle(cube_image, (x_offset + 33 * x, y_offset + 33 * y), (x_offset + 33 * (x + 1), y_offset + 33 * (y + 1)), ideal_colors[int(current_cube_state.get(i))], -1)
                cv2.rectangle(cube_image, (x_offset + 33 * x, y_offset + 33 * y), (x_offset + 33 * (x + 1), y_offset + 33 * (y + 1)), (0, 0, 0), 2)
                i += 1
        if i == 9:
            x_offset = 104
            y_offset = 308
        elif i == 18:
            x_offset = 206
            y_offset = 104
        elif i == 27:
            x_offset = 2
            y_offset = 104
        elif i == 36:
            x_offset = 104
            y_offset = 2
        elif i == 45:
            x_offset = 104
            y_offset = 206

    cv2.destroyAllWindows()
    cv2.imshow("cube", cube_image)


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


def take_input(prompt=""):
    print(prompt)
    alg = input()
    moves = alg.split()
    for temp in moves:
        current_cube_state.move(temp)
        draw_cube()
        cv2.waitKey(200)


def is_solved(state):
    return state == solved_cube


def valid_moves(prev_move):
    if len(prev_move) == 0:
        return all_moves

    invalid = []
    if prev_move[0] == "b":
        invalid = ["b", "b'", "b2"]
    elif prev_move[0] == "g":
        invalid = ["g", "g'", "g2", "b", "b'", "b2"]
    elif prev_move[0] == "r":
        invalid = ["r", "r'", "r2"]
    elif prev_move[0] == "o":
        invalid = ["o", "o'", "o2", "r", "r'", "r2"]
    elif prev_move[0] == "y":
        invalid = ["y", "y'", "y2"]
    elif prev_move[0] == "w":
        invalid = ["w", "w'", "w2", "y", "y'", "y2"]
    return [m for m in all_moves if m not in invalid]


def search(cube, moves_made, depth):
    if depth <= 0:
        # print(moves_made)
        # print(cube.get_state())
        if is_solved(cube.get_state()):
            return moves_made
        return None

    valid = all_moves

    if len(moves_made) > 0:
        valid = valid_moves(moves_made[-1])

    solutions = []

    for m in valid:
        next_cube = deepcopy(cube)
        next_cube.move(m)
        moves_made.append(m)
        possible_solution = search(next_cube, deepcopy(moves_made), depth - 1)
        if possible_solution is not None:
            solutions.append(possible_solution)
        del moves_made[-1]

    shortest_solution = None
    shortest_len = 100

    for sol in solutions:
        if len(sol) < shortest_len:
            shortest_solution = sol

    return shortest_solution

    # if depth == 0:
    #     if is_solved(cube.get_state()):
    #         # print("solution found:", moves_made)
    #         return moves_made
    #     return None
    # else:
    #     prev_move = ""
    #     if len(moves_made) > 0:
    #         prev_move = moves_made[len(moves_made) - 1]
    #     valid = valid_moves(prev_move)
    #     for m in valid:
    #         # print("previous move: {}  valid moves: {}".format(prev_move, valid))
    #         next_state = deepcopy(current_cube_state)
    #         next_state.move(m)
    #         next_moves = deepcopy(moves_made)
    #         next_moves.append(m)
    #         solution = search(next_state, next_moves, depth - 1)
    #         if solution is not None:
    #             return solution
    #     return None


def main():
    draw_cube()
    cv2.waitKey()

    take_input("Input the scramble for the cube")
    # b2 y' r g o2 y r g b' g r2 o' b

    # take_input("Input the solution for the cube")
    # b' o r2 g' b g' r' y' o2 g' r' y b2

    # print(search(current_cube_state, [], 2))

    for depth in range(22):
        print("starting depth:", depth)
        solution = search(current_cube_state, [], depth)
        if solution is not None:
            print("solution found:", solution)
            break

    cv2.waitKey()

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


