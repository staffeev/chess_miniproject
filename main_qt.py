from PyQt5.QtWidgets import QApplication
import sys
from orm import db_session
from game import Game
from gui.canvas_widget import Canvas
from board import Board
from game_qt import GameHandler
from gui.main_window import MainWindow


def except_hook(cls, exception, traceback):
    """Функция для отлова возможных исключений, вознкающих при работе с Qt"""
    sys.__excepthook__(cls, exception, traceback)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow(GameHandler())
    # game = GameHandler()
    # game.start()
    sys.excepthook = except_hook
    w.game.start()
    w.show()
    sys.exit(app.exec())