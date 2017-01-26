# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

### Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?

A: The idea of constrained propagation is to reduce the number of search parameters in the puzzle by using existing rules and information available to us. In the case of the naked twins solution we are able to reduce the search space for the parameters by initially applying elimination and only choice to reduce the number of search parameters. Furthermore we use the knowledge that a naked-twin can be a miximum of 2 digits in length and hence focus only on possibilities with a length of two. Additionally, search for twins only in the assocuated peer units and remove the digits from the peer list. This gradually reduces the number of possible solutions and improves the effectiveness of our search.

### Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?

A: Since we already have a working solution for a regular sudoku puzzle we are only required to add a new constraint to the existing system. i.e. *Diagonals also contain the digits from 1-9*. To do this we add the diagonals to the unitlist(the list of units in the sudoku) and the peerlist(associated peers for a given box.)


*Note:*
- The individual squares at the intersection of rows and columns will be called boxes. These boxes will have labels 'A1', 'A2', ..., 'I9'.
- The complete rows, columns, diagonals, and 3x3 squares, will be called units. Thus, each unit is a set of 9 boxes, and there are 29 units(9 rows, 9 columns, 9 (3x3 squares), 2 diagonals) in total.
- For a particular box (such as 'A1'), its peers will be all other boxes that belong to a common unit (namely, those that belong to the same row, column, diagonal, or 3x3 square). Each box will have 26 peers(8 in rows, 8 in columns, 8 in diagonals 8-(2row boxex + 2 column boxes, 2 diagonal boxes))

## Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

#### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

## Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

## Visualizing

To visualize your solution, please only assign values to the values_dict using the `assign_values` function provided in solution.py

## Data

The data consists of a text file of diagonal sudokus for you to solve.