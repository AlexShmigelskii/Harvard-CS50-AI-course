"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x, count_o = 0, 0

    for row in board:
        for cell in row:
            if cell == X:
                count_x += 1
            elif cell == O:
                count_o += 1
            
    return X if count_x == count_o else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # check rows
    check_winner_by_rows = any(all(cell == O for cell in row) for row in board) or any(all(cell == X for cell in row) for row in board)

    # check columns
    check_winner_by_columns = any(all(board[row][column] == O for row in range(3)) for column in range(3)) or any(all(board[row][column] == X for row in range(3)) for column in range(3))

    #check diagonals
    check_winner_by_main_diagonal = all(board[i][j] == O for i in range(3) for j in range(3) if i == j) or all(board[i][j] == X for i in range(3) for j in range(3) if i == j)
    check_winner_by_side_diagonal = all(board[i][j] == O for i in range(3) for j in range(3) if i + j == 2) or all(board[i][j] == X for i in range(3) for j in range(3) if i + j == 2)

    # if there is a winner or all cells are full
    is_winner = any([check_winner_by_rows, check_winner_by_columns, check_winner_by_main_diagonal, check_winner_by_side_diagonal])
    is_draw = not any(None in row for row in board)

    return is_winner or is_draw


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
