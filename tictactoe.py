"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    xCount = 0
    oCount = 0
    for row in board:
        for value in row:
            if value == X:
                xCount += 1
            elif value == O:
                oCount += 1
    
    if xCount > oCount:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            if board[i][j] == EMPTY:
                actions.add((i, j))
            j += 1
        i += 1
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise RuntimeError('Not valid action')
    else:
        newBoard = deepcopy(board)
        newBoard[action[0]][action[1]] = player(board)
        return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] != EMPTY and board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    elif board[1][0] != EMPTY and board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    elif board[2][0] != EMPTY and  board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]
    elif board[0][0] != EMPTY and  board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] != EMPTY and  board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] != EMPTY and  board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]
    elif board[0][0] != EMPTY and  board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] != EMPTY and  board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None
    
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    for row in board:
        for value in row:
            if value == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    
    return 0

def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v =  max(v, min_value(result(board, action)))

    return v

def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v =  min(v, max_value(result(board, action)))

    return v


def max_index(arr):
    max = arr[0]
    maximum = 0

    i = 1
    while i < len(arr):
        if arr[i] > max:
            max = arr[i]
            maximum = i
        i += 1
    
    return maximum


def min_index(arr):
    min = arr[0]
    minimum = 0

    i = 1
    while i < len(arr):
        if arr[i] < min:
            min = arr[i]
            minimum = i
        i += 1
    
    return minimum


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    allActions = actions(board)

    actionList = []
    for action in allActions:
        actionList.append(action)

    values = []
    if player(board) == X:
        for action in actionList:
            values.append(min_value(result(board,action)))
        
        return actionList[max_index(values)]
    else:
        for action in actionList:
            values.append(max_value(result(board, action)))
        
        return actionList[min_index(values)]
    
