from Player import Player

class Human(Player):
    
    def play(self, boardConfiguration):
        board = boardConfiguration.get_board()
        moveRow = None
        moveColumn = None

        # While the coordinates are already used
        while [moveRow, moveColumn] not in boardConfiguration.get_empty_cells():
            moveRow = int(input("Choisissez une ligne : "))
            moveColumn = int(input("Choisissez une colonne : "))

        return [moveRow, moveColumn]