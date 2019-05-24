from math import inf as infinity
from random import choice
import platform
import time
from os import system

from IA import IA
from random import choice

class IAExpert(IA):


    def minimax(self, board, depth, player):
        
        if player == 1: # COMPUTER
            best = [-1, -1, -infinity]
        else:           # HUMAN
            best = [-1, -1, +infinity]

        if depth == 0 or board.game_over():
            if board.wins(1):
                score= +1
            elif board.wins(-1):
                score= -1
            else:
                score= 0
            
            return [-1, -1, score]
        
        for cell in board.get_empty_cells():
            x, y = cell[0], cell[1]
            board.get_board()[x,y] = player
            score = self.minimax(board, depth - 1, -player)
            board.get_board()[x,y] = 0
            score[0], score[1] = x, y

            if player == 1:
                if score[2] > best[2]:
                    best = score
            else:
                if score[2] < best[2]:
                    best = score

        return best


    def play(self, boardConfiguration):
        depth = len(boardConfiguration.get_empty_cells())
        if depth == 9:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
        else:
            move = self.minimax(boardConfiguration, depth, 1)
            x, y = move[0], move[1]

        return [x, y]

