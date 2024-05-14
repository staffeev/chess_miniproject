from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
import os



class MainWindow(QMainWindow):
    def __init__(self, game):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui_files", "main_window.ui"), self)
        self.game = game
        self.setCentralWidget(self.game.canvas.view)
