from PyQt5.QtWidgets import QApplication, QWidget
import sys
from gui.canvas_widget import Canvas
from board import Board
from decorators import echo_which_turn, check_wrong_fig_for_turn, except_errors
from exceptions import IncorrectMovePatternError, KingUnderAttackError
from figures import figures
from PyQt5.QtCore import pyqtSignal
from functions import create_new_game, create_new_move, update_result_by_id


class GameHandler(QWidget):
    gameMessageEvent = pyqtSignal(object)

    def __init__(self, parent=None, session=None):
        super().__init__(parent)
        self.cur_play = None
        self.board = Board()
        self.canvas = Canvas(self.board, self)
        self.canvas.itemMovedEvent.connect(self.__accept_command)
        self.move_color = 1
        self.session = session
    
    def start(self):
        self.board.fill_start_field()
        if self.session is not None:
             self.cur_play = create_new_game(self.session)
        self.canvas.draw()
        if (res := self.is_checkmate()) is not None:
            self.game_over(res)
    
    @except_errors()
    @echo_which_turn
    def __accept_command(self, args):
        old_pos, new_pos = args
        fig = self.board.get_figure(old_pos)
        if self.is_check() == fig.color and fig.__class__ != figures.King:
            raise KingUnderAttackError()
        self.__make_move(fig, new_pos)
        self.move_color = 1 - self.move_color
        if (res := self.is_checkmate()) is not None:
            self.game_over(res)
    
    @check_wrong_fig_for_turn
    def __make_move(self, fig, pos2):
        if not fig.can_move(pos2):
            fig.move(fig.pos)
            raise IncorrectMovePatternError(fig, pos2)
        self.board.del_figure(pos2)
        if self.session is not None:
            create_new_move(self.session, fig.__class__.__name__, fig.color, fig.pos, pos2,
                        self.cur_play.id)
        fig.move(pos2)
        self.canvas.draw()
    
    def game_over(self, res):
        self.gameMessageEvent.emit(["Победили " + ("белые" if res == 0 else "черные"), "green"])
        self.canvas.freeze_scene()
        if self.session is not None:
            update_result_by_id(self.session, self.cur_play.id, 1 - res)
    
    def is_check(self):
        for fig in self.board.field:
            if fig.__class__ == figures.King and fig.is_check():
                return fig.color
        return None

    def is_checkmate(self):
        for fig in self.board.field:
            if fig.__class__ == figures.King and fig.is_mate():
                return fig.color
        return None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # db_session.global_init("db/plays.db")
    # session = db_session.create_session()
    g = GameHandler()
    g.start()
    sys.exit(app.exec())