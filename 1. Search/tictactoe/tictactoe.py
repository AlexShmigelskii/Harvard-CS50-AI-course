"""
Tic Tac Toe Player
"""

import math
import copy

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

    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                possible_actions.add((i, j))

    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i, j = action
    board_copy = copy.deepcopy(board)

    try:
        if board_copy[i][j] is not None:
            raise ValueError

        else:
            board_copy[i][j] = player(board_copy)

    except ValueError:
        print("Эта клетка занята")

    finally:
        return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if check_winner_by_rows(X, board) or check_winner_by_columns(X, board) or check_winner_by_main_diagonal(X, board) or check_winner_by_side_diagonal(X, board):
        return X
    
    elif check_winner_by_rows(O, board) or check_winner_by_columns(O, board) or check_winner_by_main_diagonal(O, board) or check_winner_by_side_diagonal(O, board):
        return O

    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # check rows
    winner_by_rows = check_winner_by_rows(X, board) or check_winner_by_rows(O, board)

    # check columns
    winner_by_columns = check_winner_by_columns(X, board) or check_winner_by_columns(O, board)

    #check diagonals
    winner_by_main_diagonal =  check_winner_by_main_diagonal(X, board) or check_winner_by_main_diagonal(O, board)
    winner_by_side_diagonal =  check_winner_by_side_diagonal(X, board) or check_winner_by_side_diagonal(O, board)

    # if there is a winner or all cells are full
    is_winner = any([winner_by_rows, winner_by_columns, winner_by_main_diagonal, winner_by_side_diagonal])
    is_draw = not any(None in row for row in board)

    return is_winner or is_draw


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == X:
        return 1
    
    elif winner(board) == O:
        return -1
    
    else: # tie
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None
    
    else:

        if player(board) == X:
            
            if board == initial_state():
                return (1, 1)

            _, action = Max_Value(board)

        else:
            _, action = Min_Value(board)
        
        return action


    

def Min_Value(board):
    
    # if game is over --> return "score of the board"
    if terminal(board):
        return utility(board), None
    
    else:
        move = None
        v = float('inf')

        for action in actions(board):
            # v = min(v, Max_Value(result(board, action)))
            score, _ = Max_Value(result(board, action))
            
            if score < v:
                v = score
                move = action

                if v == -1:
                    return v, move

        return v, move
    

def Max_Value(board):

    # if game is over --> return "score of the board"
    if terminal(board):
        return utility(board), None
    
    else:
        move = None
        v = float('-inf')

        for action in actions(board):
            # v = max(v, Min_Value(result(board, action)))
            score, _ = Min_Value(result(board, action))

            if score > v:
                v = score
                move = action

                if v == 1:
                    return v, move

        return v, move   


def check_winner_by_rows(player, board):
    return any(all(cell == player for cell in row) for row in board)


def check_winner_by_columns(player, board):
    return any(all(board[row][column] == player for row in range(3)) for column in range(3))


def check_winner_by_main_diagonal(player, board):
    return all(board[i][j] == player for i in range(3) for j in range(3) if i == j)


def check_winner_by_side_diagonal(player, board):
    return all(board[i][j] == player for i in range(3) for j in range(3) if i + j == 2)
