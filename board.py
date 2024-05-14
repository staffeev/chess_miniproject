from figures.figures import *
from dot import Dot
from decorators import check_in_borders


CLASS_TO_SYMBOL = {
    (Pawn, 0): "♟︎",
    (Pawn, 1): "♙",
    (Rook, 0): "♜",
    (Rook, 1): "♖",
    (Bishop, 0): "♝",
    (Bishop, 1): "♗",
    (Knight, 0): "♞",
    (Knight, 1): "♘",
    (King, 0): "♚",
    (King, 1): "♔",
    (Queen, 0): "♛",
    (Queen, 1): "♕"
}


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
    
    def __str__(self):
        return repr(self)
    
    def __repr__(self):
        m = [[" " for _ in range(8)] for _ in range(8)]
        for fig in self.field:
            x, y = fig.pos.coords
            cl, color = fig.__class__, fig.color
            m[x][y] = CLASS_TO_SYMBOL[cl, color]
        return "\n".join(["".join(i) for i in m])


if __name__ == "__main__":
    b = Board()
    b.fill_start_field()
    print(b.field)
    
