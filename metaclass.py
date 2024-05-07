from abc import ABCMeta


class FigureMeta(type):
    reg = []

    def __new__(cls, name, bases, namespace):
        def move(self, pos2):
            self.pos = pos2
            self.__class__.num_of_moves += 1
            
        new_class = super().__new__(cls, name, bases, namespace)
        setattr(new_class, "num_of_moves", 0)
        setattr(new_class, move.__name__, move)
        cls.reg.append(new_class)
        return new_class


class ABCFigureMeta(ABCMeta, FigureMeta):
    pass

 