from copy import deepcopy

all_moves = ["b", "b'", "b2", "g", "g'", "g2", "r", "r'", "r2", "o", "o'", "o2", "y", "y'", "y2", "w", "w'", "w2"]

# cube_image = np.zeros((410, 308, 3), np.uint8)

solved_cube = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5]


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
