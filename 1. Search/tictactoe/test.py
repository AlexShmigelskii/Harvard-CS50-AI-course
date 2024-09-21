from tictactoe import terminal, actions, result, winner, minimax

X = "X"
O = "O"
EMPTY = None

board = [
    [None, None, None],
    [X, X, O],
    [None, None, None]
]

print(terminal(board=board))
