from IA import IA
from random import *

class IADebutant(IA):

    def play(self, boardConfiguration):
        board = boardConfiguration.get_board()
        moveRow = randint(0,2)
        moveColumn = randint(0,2)

        # While the coordinates are already used
        while [moveRow, moveColumn] not in boardConfiguration.get_empty_cells():
            moveRow = randint(0,2)
            moveColumn = randint(0,2)

        return [moveRow, moveColumn]
        

        