from figures.figures import *
from dot import Dot
from decorators import check_in_borders


class Board:
    """Класс шахматной доски"""
    def __init__(self):
        self.field = []
    
    @check_in_borders()
    def get_figure(self, dot: Dot):
        """Получение фигуры в позиции dot(x, y)"""
        for i in self.field:
            if i.pos == dot:
                return i
        return None
    
    @check_in_borders()
    def del_figure(self, dot):
        """Удаление фигуры в позиции dot(x, y)"""
        for x, i in enumerate(self.field):
            if i.pos == dot:
                del self.field[x]
                break
    
    def fill_start_field(self):
        """Заполнение поля стандартным игровым набором"""
        order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        self.field = [Pawn(1, i, self, 0) for i in range(8)] + [Pawn(6, i, self) for i in range(8)] + \
            [fig(0, i, self, 0) for i, fig in enumerate(order)] + \
            [fig(7, i, self, 1) for i, fig in enumerate(order)]
    
    def is_under_attack(self, dot, color):
        """Проверка, что точка может быть достижима хотя бы одной фигурой"""
        for fig in self.field:
            if fig.color == color and fig.can_move(dot):
                return True
        return False

if __name__ == "__main__":
    b = Board()
    b.fill_start_field()
    print(b.field)
    
