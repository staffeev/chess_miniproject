from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QApplication, QGraphicsItem, QMainWindow
from PyQt5.QtSvg import QGraphicsSvgItem
import os


CANVAS_SIZE = (480, 480)


class Canvas(QMainWindow):
    def __init__(self, board):
        super().__init__()
        self.board = board
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, *CANVAS_SIZE)
        self.view = QGraphicsView()
        self.view.setScene(self.scene)
        self.setCentralWidget(self.view)
    
    def get_item_coords(self, scene_item, coords):
        """Получение координат фигуры на холсте"""
        width = self.scene.sceneRect().width()
        cell_size = width // 8
        item_width = scene_item.boundingRect().width()
        ix, iy = coords.coords
        x = cell_size * ix + cell_size // 2 - item_width // 2
        y = cell_size * iy + cell_size // 2 - item_width // 2
        return x, y

    
    @staticmethod
    def __get_svg_filename(elem):
        """Получение имени файла с изображением фигуры"""
        if isinstance(elem, str):
            filename = f"{elem}.svg"
        else:
            filename = f"{elem.__class__.__name__.lower()}_{elem.color}.svg"
        path = os.path.join(os.path.dirname(__file__), "svg_icons", filename)
        return path
    
    def draw(self):
        """Отрисовка элементов доски"""
        self.scene.clear()
        item = QGraphicsSvgItem(self.__get_svg_filename("chessboard"))
        self.scene.addItem(item)
        for i in self.board.field:
            item = QGraphicsSvgItem(self.__get_svg_filename(i))
            item.setFlag(QGraphicsItem.ItemIsMovable)
            x, y = self.get_item_coords(item, i.pos)
            item.setPos(y, x)
            self.scene.addItem(item)