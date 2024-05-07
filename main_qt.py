from PyQt5.QtWidgets import QWidget, QApplication
import sys
import os
# os.chdir("..")
from board import Board
from gui.canvas_widget import Canvas


def except_hook(cls, exception, traceback):
    """Функция для отлова возможных исключений, вознкающих при работе с Qt"""
    sys.__excepthook__(cls, exception, traceback)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    b = Board()
    b.fill_start_field()
    programme = Canvas(b)
    programme.show()
    programme.draw()
    sys.excepthook = except_hook
    sys.exit(app.exec())