from PyQt5.QtWidgets import QGraphicsScene, QGraphicsSceneMouseEvent, QGraphicsView, QGraphicsItem, QMainWindow
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtCore import pyqtSignal, Qt
from dot import Dot
import os


CANVAS_SIZE = (480, 480)


class Scene(QGraphicsScene):
    itemMovedEvent = pyqtSignal(object)

    def get_item_coords(self, scene_item, old_pos=False):
        """Получение координат фигуры на холсте"""
        width = self.sceneRect().width()
        cell_size = width // 8
        item_width = scene_item.boundingRect().width()
        if old_pos:
            ix, iy = scene_item.old_pos.coords
        else:
            ix, iy = scene_item.dot.coords
        x = cell_size * ix + cell_size // 2 - item_width // 2
        y = cell_size * iy + cell_size // 2 - item_width // 2
        return y, x
    
    def get_item_cell(self, scene_item, old_pos=False):
        """Получение клетки, в которой находится фигура"""
        width = self.sceneRect().width()
        cell_size = width // 8
        item_width = scene_item.boundingRect().width()
        if old_pos:
            ix, iy = scene_item.old_dot.coords
        else:
            ix, iy = scene_item.dot.coords
        x, y = scene_item.scenePos().x(), scene_item.scenePos().y()
        ix = (x + item_width // 2) // cell_size
        iy = (y + item_width // 2) // cell_size
        return Dot(iy, ix)


class SceneItem(QGraphicsSvgItem):
    """Класс фигуры на сцене"""
    def __init__(self, filename, dot):
        super().__init__(filename)
        self.old_dot = None
        self.dot = dot
    
    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if event.button() != Qt.LeftButton:
            return
        self.old_dot = self.scene().get_item_cell(self)
        return super().mousePressEvent(event)
    
    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if event.button() != Qt.LeftButton:
            return
        new_dot = self.scene().get_item_cell(self, True)
        print(self.old_dot, new_dot)
        return super().mouseReleaseEvent(event)


class Canvas(QMainWindow):
    def __init__(self, board):
        super().__init__()
        self.board = board
        self.scene = Scene(self)
        self.scene.setSceneRect(0, 0, *CANVAS_SIZE)
        self.view = QGraphicsView()
        self.view.setScene(self.scene)
        self.setCentralWidget(self.view)
    
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
            item = SceneItem(self.__get_svg_filename(i), i.pos)
            item.setFlag(QGraphicsItem.ItemIsMovable)
            x, y = self.scene.get_item_coords(item)
            item.setPos(x, y)
            self.scene.addItem(item)