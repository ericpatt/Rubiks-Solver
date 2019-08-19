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