from dot import Dot
from exceptions import OutOfBoundsException, WrongTurnColorError, IncorrectMovePatternError
import re


def logging_move(func):
    def __move(self, dot):
        res = func(self, dot)
        if res:
            print(f"Фигура {self.__class__.__name__} цвета {self.color} походила с клетки {self.pos} на клетку {dot + Dot(1, 1)}")
        return res
    return __move


def except_errors(errors_to_handle=(OutOfBoundsException, WrongTurnColorError, IncorrectMovePatternError)):
    def __inner(func):
        def __inner2(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except errors_to_handle as e:
                print(e)
        return __inner2
    return __inner


def check_wrong_fig_for_turn(func):
    def __inner(self, fig, pos):
        if fig.color != self.move_color:
            raise WrongTurnColorError(self.move_color)
        return func(self, fig, pos)
    return __inner


def echo_which_turn(func):
    def __inner(self, *args, **kwargs):
        print("Сейчас ход", "белых" if self.move_color == 1 else "черных")
        return func(self, *args, **kwargs)
    return __inner


def check_in_borders(lu=Dot(0, 0), rd=Dot(7, 7)):
    def __inner(func):
        def __inner2(self, dot):
            if not (lu <= dot <= rd):
                raise OutOfBoundsException()
            return func(self, dot)
        return __inner2
    return __inner