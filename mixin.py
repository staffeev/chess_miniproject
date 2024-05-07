class FigureMixin:
    """Класс дополнительных методов для фигуры при ее взаимодействии с другими"""
    def is_on_diag_line(self, pos2):
        """Проверка нахождения на диагонали"""
        dx, dy = abs(self.pos - pos2).coords
        return dx == dy
    
    def is_on_vh_line(self, pos2):
        """Проверка нахождения на вертикальной или горизонтальной прямой"""
        dx, dy = abs(self.pos - pos2).coords
        return dx + dy == max(dx, dy)
    
    def get_from_line(self, pos2):
        """Проверка, что на пути к точке pos2 нет других фигур"""
        dir_dot = (pos2 - self.pos).argsign()
        for i in range(1, 8):
            shifted = self.pos + dir_dot * i
            if shifted == pos2:
                return True
            elif self.board.get_figure(shifted) is not None:
                return False
        return True 