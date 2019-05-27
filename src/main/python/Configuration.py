import numpy as np
from Human import Human
from IAExpert import IAExpert
from IADebutant import IADebutant
import time
from random import *

class Configuration():

    def __init__(self):
        self.activePlayer = None
        #self.board = ([[0, 0, 0],[0, 0, 0],[0, 0, 0]])
        self.board = np.matrix([[0, 0, 0],
                                [0, 0, 0],
                                [0, 0, 0]])


    def get_active_player(self):
        return self.active_player

    def set_active_player(self, active_player):
        self.active_player = active_player

    def get_board(self):
        return self.board

    def is_board_full(self):
        for i in range(3):
            for j in range(3):
                if(self.board[i,j] == 0):
                    return False
        return True

    def get_empty_cells(self):
        cells = []
        for i in range(3):
            for j in range(3):
                if(self.get_board()[i,j] == 0):
                    cells.append([i,j])
        
        return cells

    def add_marker(self, row, column, value):
        if(0 < row > 2 or 0 < column > 2):
            raise ValueError('The coordinates must be bewteen 0 and 2')
        elif [row, column] in self.get_empty_cells():
            self.board[row, column] = value
        elif len(self.get_empty_cells())== 0 and not self.game_over():
            print("EGALITE")
        
        else:
            raise ValueError('Theses coordinates are already taken')


    def wins(self, player):
        boardConfiguration = self.get_board()
        win = [
            [boardConfiguration[0,0], boardConfiguration[0,1], boardConfiguration[0,2]],
            [boardConfiguration[1,0], boardConfiguration[1,1],boardConfiguration[1,2]],
            [boardConfiguration[2,0], boardConfiguration[2,1], boardConfiguration[2,2]],
            [boardConfiguration[0,0], boardConfiguration[1,0], boardConfiguration[2,0]],
            [boardConfiguration[0,1], boardConfiguration[1,1], boardConfiguration[2,1]],
            [boardConfiguration[0,2], boardConfiguration[1,2], boardConfiguration[2,2]],
            [boardConfiguration[0,0], boardConfiguration[1,1], boardConfiguration[2,2]],
            [boardConfiguration[2,0], boardConfiguration[1,1], boardConfiguration[0,2]],
        ]

        if [player, player, player] in win:
            return True
        else:
            return False

    def game_over(self):
        return self.wins(1) or self.wins(-1)


def main(): # IADEBUTANT
    board = Configuration()
    HUMAN = 1
    human = Human()
    IA = IADebutant()
    print(board.get_board())


    while not board.wins(1) and not board.wins(2):
        play = human.play(board)
        board.add_marker(play[0], play[1], 1)

        print(board.get_board())
        time.sleep(1)
        play = IA.play(board)
        board.add_marker(play[0], play[1], 2)
        print(board.get_board())


    print("GAME OVER")
    print(board.get_board())
#main()

def mainIAExpert():
    board = Configuration()
    board.set_active_player(1)
    IA = IAExpert()
    human = Human()
    whoPlays = randint(0,1)
    if whoPlays == 1: # l'IA commence le tour
        print("IA commence")
        play = IA.play(board)
        print(play)
        board.add_marker(play[0], play[1], 1)
        print(board.get_board())
    else:
        print("Vous commencez")
    while not board.game_over() and len(board.get_empty_cells()) > 0:
        
        play = human.play(board)
        board.add_marker(play[0], play[1], -1)

        print(board.get_board())
        time.sleep(1)
        play = IA.play(board)
        print(play)
        board.add_marker(play[0], play[1], 1)
        print(board.get_board())



    if board.wins(1) == True:
        print("PARTIE PERDUE")
    else:
        print("PARTIE GAGNEE")
    print(board.get_board())

#mainIAExpert()