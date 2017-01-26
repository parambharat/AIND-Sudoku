"""Contains functions for the sodoku solver."""
from constants import *

# Assignments needed for pygame display
assignments = []


def assign_value(values, box, value):
    """Assigns a value to a given box. If it updates the board record it.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
        box(string): The key where the value needs to be updated.
        value(string): The value to be updated.

    Returns:
        The values dictionary with the naked twins eliminated from peers.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


def naked_twins(values):
    """Eliminates values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    doubles = {box: values[box] for unit in UNITLIST for box in unit if (
        box not in get_solved(values) and len(values[box]) == 2)}
    twins = {tuple(sorted((box, peer))) for box in doubles for peer in PEERS[
        box] if values[peer] == values[box]}

    untwin = [(box, peer) for box, peer in twins for box in (PEERS[
        box] & PEERS[peer]) if len(values[box]) > 1]

    # Eliminate the naked twins as possibilities for their peers

    for box, peer in untwin:
        for digit in values[peer]:
            values = assign_value(values, box, values[box].replace(digit, ""))
    return values


def grid_values(grid):
    """Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The BOXES, e.g., 'A1'
            Values: The value in each box, e.g., '8'.
                If the box has no value, then the value will be '123456789'.
    """
    default = '123456789'
    dict_grid = {
        k: (default if v == '.' else v) for k, v in (zip(BOXES, grid))
    }
    return dict_grid


def display(values):
    """Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1 + max(len(values[s]) for s in BOXES)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in ROWS:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in COLS))
        if r in 'CF':
            print(line)


def get_solved(values):
    """ Get a list of solved keys in the values dictionary.
    Args:
        values(dict): The sudoku in dictionary form.
    Returns:
        (list): The list of keys of solved values in the dictionary.
    """
    return [key for key, value in values.items() if len(value) == 1]


def eliminate(values):
    """Go through all the boxes, and whenever there is a box with a value,
    eliminate this value from the values of all its peers.
    Args:
        values(dict): The sudoku in dictionary form.
    Returns:
        The resulting sudoku in dictionary form.
    """
    for key in get_solved(values):
        for peer_key in PEERS[key]:
            values = assign_value(values, peer_key, values[
                                  peer_key].replace(values[key], ''))
    values = naked_twins(values)
    return values


def only_choice(values):
    """Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.
    Args:
        values(dict): A sudoku in dictionary form.
    Returns:
        The resulting sudoku in dictionary form.
    """
    for unit in UNITLIST:
        for i in '123456789':
            blist = [box for box in unit if i in values[box]]
            if len(blist) == 1:
                values = assign_value(values, blist[0], i)
    return values


def reduce_puzzle(values, stall=False):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box
    with no available values, return False. If the sudoku is solved, return the
    sudoku. If after an iteration of both functions, the sudoku remains the
    same, return the sudoku.
    Args:
        values(dict): The sudoku in dictionary form.
        stall(bool): The stalled state of the sudoku puzzle.
    Returns:
        The resulting sudoku in dictionary form.
    """
    if not stall:
        before_len = len(get_solved(values))
        values = eliminate(values)
        values = only_choice(values)
        after_len = len(get_solved(values))
        stall = before_len == after_len
        return reduce_puzzle(values, stall)
    else:
        return values


def solve(grid):
    """The main sudoku solver.
    Args:
        grid(string): The sudoku initial state as a string.
    Returns:
        The resulting solved sudoku, or the corresponding stalled response.
    """
    values = grid_values(grid)
    values = search(values)
    return values


def search(values):
    """Using depth-first search and propagation, try all possible values.
    First, reduce the puzzle using the previous function
    Chose one of the unfilled square s with the fewest possibilities
    Now use recurrence to solve each one of the resulting sudokus, and
    Args:
        values(dict): The sudoku in dictionary form.
    Returns:
        The resulting solved sudoku, or the corresponding stalled response.
    """
    values = reduce_puzzle(values, stall=False)
    if not values:
        return False
    if max(values.values(), key=len) == 1:
        return values
    unsolved = [(box, values[box])
                for box in BOXES if box not in set(get_solved(values))]
    if unsolved:
        u_box = min(unsolved, key=lambda x: len(x[1]))[0]
        for value in values[u_box]:
            new_grid = assign_value(values, u_box, value)
            branch = search(new_grid)
            if branch:
                return branch
    else:
        return values


if __name__ == '__main__':
    # Input sudoku puzzle in string form.
    diag_sudoku_grid = """2.............62....1....7...6..8...3...9...7...
    6..4...4....8....52.............3""".replace('\n', '')

    # Solve and display the solution.
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)
    except:
        print("""We could not visualize your board due to a pygame issue.
         Not a problem! It is not a requirement.""".replace('\n', ''))
