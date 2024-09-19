from tictactoe import terminal

X = "X"
O = "O"
EMPTY = None

board = [
    [None, O, X],
    [O, X, O],
    [X, X, O]
]

print(terminal(board=board))