"""Contains constants used to describe a sudoku game."""
from itertools import product


def cross(A, B):
    """Cross product of elements in A and elements in B."""
    return ["".join(item)for item in product(A, B)]


# Definition of rows and columns in the sudoku.
ROWS = 'ABCDEFGHI'
COLS = '123456789'

# Boxes in the sodoku grid
BOXES = cross(ROWS, COLS)

# Units are related cells that contain a set of 9 numbers.
ROW_UNITS = [cross(r, COLS) for r in ROWS]
COL_UNITS = [cross(ROWS, c) for c in COLS]
DIAG_UNITS = [
    [item for sublist in (cross(r, c) for r, c in zip(ROWS, COLS))
        for item in sublist],
    [item for sublist in (cross(r, c) for r, c in zip(ROWS, COLS[::-1]))
        for item in sublist]
]

SQUARE_UNITS = [
    cross(rs, cs) for rs, cs in
    product(('ABC', 'DEF', 'GHI'), ('123', '456', '789'))
]
UNITLIST = ROW_UNITS + COL_UNITS + SQUARE_UNITS + DIAG_UNITS

# Peers are all associated cells that related to a certain cell.
PEERS = {box: set(
    [peer for unit in UNITLIST for peer in unit if box in unit if peer != box])
    for box in BOXES}
