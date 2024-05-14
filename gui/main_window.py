from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5 import uic
import os
from game_qt import GameHandler



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui_files", "main_window.ui"), self)
        self.game = None
        self.new_game_act.triggered.connect(self.create_new_game)
    
    def create_new_game(self):
        game = GameHandler(self)
        self.connect_to_game_handler(game)
        self.game.start()
    
    def connect_to_game_handler(self, game):
        self.game = game
        self.setCentralWidget(self.game.canvas.view)
        self.game.gameMessageEvent.connect(self.__process_message)

    def __process_message(self, args):
        msg, back_color = args
        self.statusbar.setStyleSheet(f"background-color: {back_color}")
        self.statusbar.showMessage(msg, 2000)
        QTimer.singleShot(2000, lambda: self.statusbar.setStyleSheet("background-color: white"))
    

