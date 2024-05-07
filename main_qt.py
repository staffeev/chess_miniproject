from PyQt5.QtWidgets import QApplication
import sys
from orm import db_session
from game import Game
from gui.canvas_widget import Canvas
from board import Board


def except_hook(cls, exception, traceback):
    """Функция для отлова возможных исключений, вознкающих при работе с Qt"""
    sys.__excepthook__(cls, exception, traceback)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # db_session.global_init("db/plays.db")
    # session = db_session.create_session()
    # g = Game(session, Canvas)
    # g.start()
    # g.canvas.show()
    # g.play()
    b = Board()
    b.fill_start_field()
    canv = Canvas(b)
    canv.draw()
    canv.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())