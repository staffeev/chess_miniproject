from PyQt5.QtWidgets import QDialog, QLabel, QDialogButtonBox, QLineEdit, \
    QVBoxLayout, QListWidget, QMessageBox
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt


class ChooseGameForm(QDialog):
    """Класс формы для выбора игры"""
    def __init__(self, games, parent=None) -> None:
        super().__init__(parent)
        self.games = games
        self.name_to_return = None
        self.setWindowTitle("Выбрать игру")
        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.list = QListWidget()
        self.list.addItems([f"{i.id}\t{i.date}" for i in games])
        self.list.itemDoubleClicked.connect(self.accept)
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("Выберите игру для продолжения:"))
        self.layout.addWidget(self.list)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def accept(self, item) -> None:
        """Метод обработки события нажатия на кнопку ОК"""
        text = item.text().split("\t")
        self.selected_game = [i for i in self.games if str(i.id) == text[0] and str(i.date) == text[1]][0]
        self.done(1)