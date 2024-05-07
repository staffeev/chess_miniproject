class Dot:
    """Класс для точки на игровом поле"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def coords(self):
        return self.x, self.y
    
    def argsign(self):
        x = 0 if self.x == 0 else self.x // abs(self.x)
        y = 0 if self.y == 0 else self.y // abs(self.y)
        return Dot(x, y) 
    
    def __abs__(self):
        return Dot(abs(self.x), abs(self.y))
    
    def __add__(self, other):
        return Dot(self.x + other.x, self.y + other.y)
    
    def __mul__(self, value):
        return Dot(self.x * value, self.y * value)
    
    def __sub__(self, other):
        return Dot(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return str(self)

