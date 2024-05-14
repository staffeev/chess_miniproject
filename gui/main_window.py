from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer
from PyQt5 import uic
import os
from sys import exit
from game_qt import GameHandler
from gui.choose_game_form import ChooseGameForm
from functions import get_all_results, get_all_moves



class MainWindow(QMainWindow):
    def __init__(self, session=None):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui_files", "main_window.ui"), self)
        self.game = None
        self.session = session
        self.new_game_act.triggered.connect(self.create_new_game)
        self.load_game_act.triggered.connect(self.load_game)
        self.stats_act.triggered.connect(self.show_stats)
    
    def show_stats(self):
        """Выводит статистику по играм"""
        moves = get_all_moves(self.session)
        results = get_all_results(self.session)
        stats1 = {}
        for move in moves:
            key = (move.figure, {1: "белый", 0: "черный"}[move.color])
            stats1[key] = stats1.get(key, 0) + 1
        stats2 = {}
        for res in results:
            if res.win is None:
                continue
            key = {1: "белые", 0: "черные"}[res.win]
            stats2[key] = stats2.get(key, 0) + 1
        text = ""
        text += "Стастистика по победам:\n"
        for key, val in stats2.items():
            text += f"{key}: {val}\n"
        text += "\n\n"
        text += "Стастистика по ходам (фигура, цвет, количество):\n"
        for key, val in stats1.items():
            text += f"{key[0]}, {key[1]}: {val}\n"
        QMessageBox.about(self, "Статистика", text)
        
    
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
    

