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
    if(board == initial_state()):
        return X
    count_x=0
    count_o=0
    for row in board:
        for cell in row:
            if(cell == X):
                count_x+=1
            if(cell == O):
                count_o+=1
    
    if(count_x <= count_o):
        return X
    else:
        return O
            
    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column]== EMPTY:
                possible_actions.add((row, column))
                
    return possible_actions
                


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    
    
     
    if new_board[action[0]][action[1]] != None:
        raise ValueError("Can not perform this action on this current state")
    
    if action[0]<0 or action[0]>2 or action[1]<0 or action[1]>2:
        raise ValueError("out out bound")
            
    new_board[action[0]][action[1]] = player(board)
    return new_board
            
            
def check_columns(board):
    for row in board:
        if(len(set(row)) ==1 and row[0] is not None):
            return row[0]
    return None

def check_rows(board):
    return check_columns(zip(*reversed(board)))

def check_diagonal(board):
    if( (board[0][0] == board[1][1] == board[2][2]) or 
       (board[0][2] == board[1][1] == board[2][0])):
        if(board[1][1] != None):
            return board[1][1]
    return None


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for check in [check_columns , check_rows , check_diagonal]:
        result = check(board)
        if(result != None):
            return result
    
            
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    result = winner(board)
    if(result != None):
        return True
    
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column]== EMPTY:
                return False
            
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if(result == X):
        return 1
    elif (result == O):
        return -1
    else:
        return 0

def max_value(board):
    if(terminal(board)):
        return utility(board)
    value = -99999999999
    for action in actions(board):
        value=max(value , min_value(result(board , action)))
    return value

def min_value(board):
    if(terminal(board)):
        return utility(board)
    value = 99999999999
    for action in actions(board):
        value=min(value , max_value(result(board , action)))
    return value
    
    
    
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    
    player_turn = player(board)
    
    if(player_turn == X):
        best_value = -math.inf
        best_action = None
        
        for action in actions(board):
            # After X moves, O will play (minimizing)
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
        return best_action
           
                
    if(player_turn == O):
       
        best_value = math.inf
        best_action = None
        
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
        return best_action