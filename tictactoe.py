"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

s = 0

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
    x_counter = 0
    o_counter = 0
    for row in board:
        for cell in row:
            if cell == 'X':
                x_counter = x_counter + 1
            elif cell == 'O':
                o_counter = o_counter + 1
    if x_counter <= o_counter:
        return 'X'
    else:
        return 'O'

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i,j))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    new_board = copy.deepcopy(board)
    turn = player(board)
    if new_board[i][j] != EMPTY:
        raise Exception 
    else:
        new_board[i][j] = turn
    return new_board
    
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #there should be at least 5 filled squares, to obtain a winning position.
    if filled_cells_counter(board) <= 4:
        return None
    #check horizontal win
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
    #check vertical win
    for i in range(3):
        if (board[0][i] != EMPTY and
            board[0][i] == board[1][i] and
            board[1][i] == board[2][i]):
            return board[0][i]
    #check diagonal win
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0] :
        return board[1][1]
    return None 

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for row in board:
        if EMPTY in row:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    t = terminal2(board)
    if w != None:
        if w == X:
            return 1
        elif w == O:
            return -1
    if t:
        return 0
    else:
        return None

def minimax(board): #Minimum time: 15.7 seconds
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else: 
        if player(board) == X:
            v,action = max(board)
        else:
            v,action = min(board)
    return action

def max(board):
    """
    Returns the optimal move if it's X to play.
    """
    opt = None
    M = -99999999
    utlty = utility(board)
    if utlty is not None:
        return utlty ,(0,0)
    actns = actions(board)
    for action in actns :
        m, a = min(result(board,action))
        if m > M:
            M = m
            opt = action
    return M,opt
def min(board):
    """
    Returns the optimal move if it's O to play.
    """
    opt = None
    M = 99999999
    utlty = utility(board)
    if utlty is not None:
        return utlty ,(0,0)
    actns = actions(board)
    for action in actns :
        m, a = max(result(board,action))
        if m < M:
            M = m
            opt = action
    return M,opt

def filled_cells_counter(board):
    """
    Returns how many empty cells are on the board.
    """
    counter = 0
    for row in board:
        for cell in row:
            if cell is not EMPTY:
                counter = counter + 1
    return counter

def check_win(board):
    """
    Returns the winner of the game, if there is any, version 2.
    actually version 1, I made this one first but it was a bit slow because
    of the function calls maybe, so I included all of them in one function, which
    affected positively the speed of execution, the other function is the one used, 
    but I decided to keep it anyways.
    """
    if filled_cells_counter(board) <= 4:
        return None
    else:
        hrnztl = check_horizontal_pattern(board)
        if hrnztl is not None:
            return hrnztl
        else:
            vrtcl = check_vertical_pattern(board)
            if vrtcl is not None:
                return vrtcl
            else:
                diag = check_diagonal_pattern(board)
                if diag is not None:
                    return diag
    return None
        

def check_horizontal_pattern(board):
    """
    Returns whether there is a horizontal winning pattern or not.
    """
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
    return None

def check_vertical_pattern(board):
    """
    Returns whether there is a vertical winning pattern or not.
    """
    for j in range(3):
        counter = 0
        cell = None
        if board[0][j] != EMPTY:
            counter = counter + 1
            cell = board[0][j]
        else:
            continue
        for i in range(1,3):
            if board[i][j] == cell:
                counter = counter + 1
            if counter == 3:
                return cell
    return None

def check_diagonal_pattern(board):
    """
    Returns whether there is a diagonal winning pattern or not.
    """
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0] :
        return board[1][1]
    else:
        return None

def terminal2(board):
    """
    Returns whether the board is full or not.
    """
    for row in board:
        if EMPTY in row:
            return False
    return True

def minimax2(board):#Minimum time: 3.6 seconds
    """
    Returns the optimal move for the current player on the board, to complete
    the assignement, I thought I had to use the functions given to be implemented
    which I did in 'minimax()', but it was taking a bit too long to calculate the first 
    move when it's the AI to make the first move.
    it was taking around 15 seconds, but the average time decreases dramatically move after move.
    I used some online resources to optimize the function which led to not using some of the provided functions(to implement).
    this function is connected, to max2() and min2().
    and the time of the AI's first move as X was reduced from 15 seconds to 4.6 seconds in average.
    but I thought of another modification in the code that would make it faster, and it's not the Alpha-beta prunning, but something similar nonetheless.
    so I created minimax3(), max3() and min3() to implement the modification.
    """
    if terminal(board):
        return None
    else: 
        if player(board) == X:
            v,action = max2(board)
        else:
            v,action = min2(board)
    return action

def max2(board):
    """
    Returns the optimal move if it's X to play.
    """
    opt = None
    M = -99999999
    utlty = utility(board)
    if utlty is not None:
        return utlty ,(0,0)
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                board[i][j] = X
                m, a = min2(board)
                if m > M:
                    M = m
                    opt = (i,j)
                board[i][j] = EMPTY
    return M,opt

def min2(board):
    """
    Returns the optimal move if it's O to play.
    """
    opt = None
    M = 99999999
    utlty = utility(board)
    if utlty is not None:
        return utlty ,(0,0)
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                board[i][j] = O
                m, a = max2(board)
                if m < M:
                    M = m
                    opt = (i,j)
                board[i][j] = EMPTY
    return M,opt

    
def minimax3(board):#Minimum time: 0.6 seconds
    """
    here I applied the modification talked about in minimax2(), which is something similar to the alpha-beta prunning which is implemented later.
    instead of using alpha and beta values, I used the maximum and minimum values.
    when the max3() function reaches a position where the utility() function returns 1, it doesn't keep comparing it to other values since it's the largest possible value.
    same thing with min3(), except that it returns -1 when reached without comparing it to other values.
    after thinking about it, it's pretty much the same thing as the alpha-beta prunning,
    except that here we already know what are the possible values and there is no need to wait to check other ones.
    and here it's even easier to implement, but it porbably won't work in more complex games.
    """
    if terminal(board):
        return None
    else: 
        if player(board) == X:
            v,action = max3(board)
        else:
            v,action = min3(board)
    return action

def max3(board):
    opt = None
    M = -99999999
    utlty = utility(board)
    if utlty is not None:
        return utlty ,(0,0)
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                board[i][j] = X
                m, a = min3(board)
                if m == 1:
                    board[i][j] = EMPTY
                    return m,(i,j)
                if m > M:
                    M = m
                    opt = (i,j)
                board[i][j] = EMPTY
    return M,opt

def min3(board):
    opt = None
    M = 99999999
    utlty = utility(board)
    if utlty is not None:
        return utlty ,(0,0)
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                board[i][j] = O
                m, a = max3(board)
                if m == -1:
                    board[i][j] = EMPTY
                    return m,(i,j)
                if m < M:
                    M = m
                    opt = (i,j)
                board[i][j] = EMPTY
    return M,opt

def minimax_alpha_beta_prunning(board):#Minimum time: 0.12 seconds
    """
    I included the alpha-beta and the modification I added the previous minimax3().
    it didn't change anything I think, the results before and after adding the modification were alike, with average of 1.4 seconds.
    """
    if terminal(board):
        return None
    else:
        alpha = -9999999
        beta = 9999999 
        if player(board) == X:
            v,action = max_alpha_beta_prunning(board, alpha, beta)
        else:
            v,action = min_alpha_beta_prunning(board, alpha, beta)
    return action

def max_alpha_beta_prunning(board, alpha, beta):
    opt = None
    M = -99999999
    utlty = utility(board)
    if utlty is not None:
        return utlty ,(0,0)
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                board[i][j] = X
                m, a = min_alpha_beta_prunning(board,alpha,beta)
                if m == 1:
                    board[i][j] = EMPTY
                    return m,(i,j)
                if m > M:
                    M = m
                    opt = (i,j)
                board[i][j] = EMPTY
                if M >= beta:
                    return M,(i,j) 
                if M > alpha:
                    alpha = M
    return M,opt

def min_alpha_beta_prunning(board, alpha, beta):
    opt = None
    M = 99999999
    utlty = utility(board)
    if utlty is not None:
        return utlty ,(0,0)
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                board[i][j] = O
                m, a = max_alpha_beta_prunning(board,alpha,beta)
                if m == -1:
                    board[i][j] = EMPTY
                    return m,(i,j)
                if m < M:
                    M = m
                    opt = (i,j)
                board[i][j] = EMPTY
                if M <= alpha:
                    return M,(i,j) 
                if M < beta:
                    beta = M
    return M,opt