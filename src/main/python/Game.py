import random

from ASCIIRenderer import ASCIIRenderer

class Game():

    def __init__(self):
        self.player = Player()
        self.robot = AI()
        if(random.randint(0, 1)):
            self.config = Configuration(player)
        else:
            self.config = Configuration(robot)

    def play(self):
        while not config.is_board_full():
            ASCIIRenderer.print_board(config.get_board())

            coord = self.config.get_active_player().play()
            self.config.add_marker(coord, self.config.get_active_player().symbol)

            # Switch on player
            if(self.config.get_active_player() == self.player):
                self.config.set_active_player(self.robot)
            else:
                self.config.set_active_player(self.player)

        # TODO : Who won ?
