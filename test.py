import sys
from PyQt5 import QtCore, QtGui

class GraphicsScene(QtGui.QGraphicsScene):
    itemDoubleClicked = QtCore.Signal(object)

class GraphicsRectangle(QtGui.QGraphicsRectItem):
    def mouseDoubleClickEvent(self, event):
        self.scene().itemDoubleClicked.emit(self)

class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.view = QtGui.QGraphicsView()
        self.scene = GraphicsScene(self)
        self.view.setScene(self.scene)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.view)
        for i in range(1, 4):
            self.scene.addItem(GraphicsRectangle(50 * i, 50 * i, 20, 20))
        self.scene.itemDoubleClicked.connect(self.handleItemDoubleClicked)

    def handleItemDoubleClicked(self, item):
        print(item.boundingRect())

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.setGeometry(600, 100, 300, 200)
    window.show()
    sys.exit(app.exec_())