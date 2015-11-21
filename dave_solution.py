import numpy as np

colums_dict = ['A':0, 'B':1, 'C':2]
player1_turn = True
player2_turn = False

def init_board():
    return np.matrix([
            ['.','.','.'], 
            ['.','.','.'], 
            ['.','.','.']
        ])

def win_test(board):
    diag1 = [board[0,0],board[1,1],board[2,2]]
    diag2 = [board[0,2],board[1,1],board[2,1]]
    
    #We could refactor this into making a list of the joined lists, 
    #and then checking if 'XXX' or 'OOO' is *in* that list. it'd cut out a lot of these conditions
    for i in range(len(board)):
        if ''.join(board[:,i]) == 'XXX' or ''.join(board[:,i]) == 'OOO' or ''.join(board[i:,]) == 'XXX' or ''.join(board[i:,]) == 'OOO' :
            return True
    if ''.join(diag1) == 'XXX' or ''.join(diag1) == 'OOO' or ''.join(diag2) == 'XXX' or ''.join(diag2) == 'OOO':
        return True
        
def display_board(board):
    pass
        
def get_next_move():
    while True:
        col = raw_input("What column would you like to place?").upper()
        if col == 'A' or col == 'B' or col == 'C':
            pass      
        else: print "Please type A B or C"
    
    while True:
        row = raw_input("What row?")
        try:
            row = int(row)
            pass
        except ValueError:
            print "Please enter a number 1-3"
    return (columns_dict[col],row-1)
    
def main_play():
    board = init_board()
    pass
