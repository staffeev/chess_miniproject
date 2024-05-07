import sys
from PyQt5.QtCore import QObject, pyqtSignal



class OutOfBoundsException(Exception):
    def __init__(self, message="Нельзя ходить за пределы поля"):
        super().__init__(message)


class IncorrectMovePatternError(Exception):
    def __init__(self, fig, pos2, message="Фигура {} в позиции {} не может походить в позицию {}"):
        super().__init__(message.format(fig.__class__.__name__, fig.pos, pos2))


class WrongTurnColorError(Exception):
    color_to_word = {1: "белого", 0: "черного"}
    def __init__(self, cur_color, message="Сейчас должна ходить фигура {} цвета"):
        super().__init__(message.format(cur_color))


class InvalidDataForDBError(Exception):
    def __init__(self, message="Предотвращена попытка ввести недопустимые данные в БД"):
        super().__init__(message)


class ExceptionHandler(QObject):
    errorSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def handler(self, exctype, value, traceback):
        self.errorSignal.emit(exctype)
        sys._excepthook(exctype, value, traceback)
    