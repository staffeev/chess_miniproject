from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5 import uic
import os
from sys import exit
from game_qt import GameHandler
from gui.choose_game_form import ChooseGameForm
from functions import get_all_results



class MainWindow(QMainWindow):
    def __init__(self, session=None):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui_files", "main_window.ui"), self)
        self.game = None
        self.session = session
        self.new_game_act.triggered.connect(self.create_new_game)
        self.load_game_act.triggered.connect(self.load_game)
    
    def create_new_game(self):
        """Новая игра"""
        game = GameHandler(self, self.session)
        self.connect_to_game_handler(game)
        self.game.start()
    
    def load_game(self):
        """Загрузка игры"""
        form = ChooseGameForm(get_all_results(self.session))
        if not form.exec():
            return
        game = GameHandler(self, self.session, form.selected_game)
        self.connect_to_game_handler(game)
        self.game.start()

    
    def connect_to_game_handler(self, game):
        """Подключение хэндлера игры"""
        self.game = game
        self.setCentralWidget(self.game.canvas.view)
        self.game.gameMessageEvent.connect(self.__process_message)

    def __process_message(self, args):
        """Обработка игровых сообщений"""
        msg, back_color = args
        self.statusbar.setStyleSheet(f"background-color: {back_color}")
        self.statusbar.showMessage(msg, 2000)
        QTimer.singleShot(2000, lambda: self.statusbar.setStyleSheet("background-color: white"))
    
    def closeEvevent(self, _):
        """Закрытие"""
        if self.game.session is not None:
            self.game.session.close()
        exit(0)
    

