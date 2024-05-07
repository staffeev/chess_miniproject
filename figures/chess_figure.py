from abc import ABC, abstractmethod, ABCMeta
from dot import Dot
from decorators import check_in_borders, logging_move


class Figure(ABC):
    """Абстрактный класс шахматной фигуры"""
    def __init__(self, x: int, y: int, board, color=1):
        self.pos = Dot(x, y)
        self.color = color
        self.board = board
    
    def __str__(self):
        return f"{self.__class__.__name__}(pos={self.pos}, color={self.color})"
    
    def __repr__(self):
        return str(self)
    
    @abstractmethod
    def check_if_fits_move_pattern(self, pos2: Dot):
        pass
    
    @logging_move
    @check_in_borders()
    def can_move(self, pos2: Dot):
        if self.pos == pos2:
            return False
        if not self.check_if_fits_move_pattern(pos2):
            return False
        fig = self.board.get_figure(pos2)
        if fig is None or fig.color != self.color:
            return True
        return False
    
    def move(self, pos2):
        self.pos = pos2
