from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QApplication, QGraphicsItem, QMainWindow
from PyQt5.QtSvg import QGraphicsSvgItem
import os


class Canvas(QMainWindow):
    def __init__(self, board):
        super().__init__()
        self.board = board
        self.scene = QGraphicsScene()
        self.view = QGraphicsView()
        self.view.setScene(self.scene)
        self.setCentralWidget(self.view)
    
    @staticmethod
    def get_svg_filename(elem):
        """Получение имени файла с изображением фигуры"""
        filename = f"{elem.__class__.__name__.lower()}_{elem.color}.svg"
        path = os.path.join(os.path.dirname(__file__), "svg_icons", filename)
        return path
    
    def draw(self):
        """Отрисовка элементов доски"""
        for i in self.board.field:
            item = QGraphicsSvgItem(self.get_svg_filename(i))
            item.setFlag(QGraphicsItem.ItemIsMovable)
            self.scene.addItem(item)