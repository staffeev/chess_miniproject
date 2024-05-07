import os
from figures.chess_figure import Figure
from figures.mixin import FigureMixin
from dot import Dot
from figures.metaclass import ABCFigureMeta



class Knight(Figure, metaclass=ABCFigureMeta):
    """Класс фигуры коня"""
    def check_if_fits_move_pattern(self, pos2: Dot):
        dx, dy = abs(self.pos - pos2).coords
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)


class King(Figure):
    """Класс фигуры короля"""
    def check_if_fits_move_pattern(self, pos2: Dot):
        dx, dy = abs(self.pos - pos2).coords
        return dx <= 1 and dy <= 1
    
    def is_check(self):
        """Проверка, что поставлен шах"""
        return self.board.is_under_attack(self.pos, 1 - self.color)
    
    def is_mate(self):
        """Проверка, что поставлен мат"""
        if not self.is_check():
            return False
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                try:
                    if self.can_move(Dot(x, y)) and not \
                        self.board.is_under_attack(Dot(x, y), 1 - self.color):
                        return False
                except IndexError:
                    continue
        return True


class Rook(Figure, FigureMixin):
    """Класс фигуры ладьи"""
    def check_if_fits_move_pattern(self, pos2: Dot):
        if not self.is_on_vh_line(pos2):
            return False
        return self.get_from_line(pos2)


class Bishop(Figure, FigureMixin):
    """Класс фигуры слона"""
    def check_if_fits_move_pattern(self, pos2: Dot):
        if not self.is_on_diag_line(pos2):
            return False
        return self.get_from_line(pos2)


class Queen(Figure, FigureMixin, metaclass=ABCFigureMeta):
    """Класс фигуры ферзя"""
    def check_if_fits_move_pattern(self, pos2: Dot):
        if not self.is_on_diag_line(pos2) and not self.is_on_vh_line(pos2):
            return False
        return self.get_from_line(pos2)


class Pawn(Figure, FigureMixin, metaclass=ABCFigureMeta):
    """Класс фигуры пешки"""
    def check_if_fits_move_pattern(self, pos2: Dot):
        dx, dy = (pos2 - self.pos).coords
        big_step_flag = (self.pos.x == 1 and self.color == 0) or (self.pos.x == 6 and self.color == 1)
        if abs(dy) > 1 or abs(dx) > 1 + int(big_step_flag):
            return False
        if (self.color == 0 and dx < 0) or (self.color == 1 and dx > 0):
            return False
        fig = self.board.get_figure(pos2)
        if dy != 0:
            return self.board.get_figure(pos2) is not None
        return self.get_from_line(pos2 + (pos2 - self.pos).argsign())