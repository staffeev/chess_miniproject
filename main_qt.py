from PyQt5.QtWidgets import QApplication
import sys
from orm import db_session
from gui.main_window import MainWindow


def except_hook(cls, exception, traceback):
    """Функция для отлова возможных исключений, вознкающих при работе с Qt"""
    sys.__excepthook__(cls, exception, traceback)



if __name__ == "__main__":
    db_session.global_init("db/plays.db")
    session = db_session.create_session()
    app = QApplication(sys.argv)
    w = MainWindow(session)
    sys.excepthook = except_hook
    w.show()
    sys.exit(app.exec())