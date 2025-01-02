"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O


def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    if action not in actions(board):
        raise ValueError("Invalid action")
    
    new_board = [row[:] for row in board]
    i, j = action
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None


def terminal(board):
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)

def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0

def minimax(board):
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        value, move = max_value(board)
    else:
        value, move = min_value(board)
    return move

def max_value(board):
    """
    Maximizing player (X).
    """
    if terminal(board):
        return utility(board), None

    value = -math.inf
    best_action = None
    for action in actions(board):
        new_value, _ = min_value(result(board, action))
        if new_value > value:
            value = new_value
            best_action = action
    return value, best_action


def min_value(board):
    """
    Minimizing player (O).
    """
    if terminal(board):
        return utility(board), None

    value = math.inf
    best_action = None
    for action in actions(board):
        new_value, _ = max_value(result(board, action))
        if new_value < value:
            value = new_value
            best_action = action
    return value, best_action