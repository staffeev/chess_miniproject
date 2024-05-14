from dot import Dot


class OutOfBoundsException(Exception):
    def __init__(self, message="Нельзя ходить за пределы поля"):
        super().__init__(message)


class IncorrectMovePatternError(Exception):
    def __init__(self, fig, pos2, message="Фигура {} в позиции {} не может походить в позицию {}"):
        super().__init__(message.format(fig.__class__.__name__, fig.pos + Dot(1, 1), pos2 + Dot(1, 1)))


class WrongTurnColorError(Exception):
    color_to_word = {1: "белого", 0: "черного"}
    def __init__(self, cur_color, message="Сейчас должна ходить фигура {} цвета"):
        super().__init__(message.format(self.color_to_word[cur_color]))


class InvalidDataForDBError(Exception):
    def __init__(self, message="Предотвращена попытка ввести недопустимые данные в БД"):
        super().__init__(message)


class KingUnderAttackError(Exception):
    def __init__(self, message="Король находится под атакой, нельзя ходить другой фигурой"):
        super().__init__(message)