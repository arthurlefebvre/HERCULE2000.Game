from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QComboBox
from PyQt5.QtCore import QThread, QObject, pyqtSignal

import sys

from Configuration import Configuration
from IAExpert import IAExpert
from IADebutant import IADebutant
from Human import Human
from random import *
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.comboBox = QComboBox()
        self.comboBox.addItems(["Débutant", "Intermédiaire", "Expert"])

        self.playBt = QPushButton("Jouer")
        self.playBt.clicked.connect(self.on_clicked_bt)

        # self.thread = QThread()
        # self.worker = Worker()

        # self.thread.started.connect(self.worker.do_task)
        # self.playBt.clicked.connect(self.thread.start)

        self.layout.addWidget(self.comboBox)
        self.layout.addWidget(self.playBt)

        self.main_frame = QWidget()
        self.main_frame.setLayout(self.layout)

        self.setCentralWidget(self.main_frame)
        self.resize(500, 300)

    def on_clicked_bt(self):
        self.play_game()
    

    def play_game(self):
        board = Configuration()
        board.set_active_player(1)
        if self.comboBox.currentText() == "Débutant":
            IA = IADebutant()
        else:
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


        print("GAME OVER")
        print(board.get_board())

class Worker(QObject):
    finished = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)
        self.continue_run = True


    def do_task(self):
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
        while not board.game_over() and len(board.get_empty_cells()) > 0 and self.continue_run:
            
            play = human.play(board)
            board.add_marker(play[0], play[1], -1)

            print(board.get_board())
            time.sleep(1)
            play = IA.play(board)
            print(play)
            board.add_marker(play[0], play[1], 1)
            print(board.get_board())


        print("GAME OVER")
        print(board.get_board())


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    app = MainWindow()
    app.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)