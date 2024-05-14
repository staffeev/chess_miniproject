from PyQt5.QtWidgets import QApplication, QWidget
import sys
from gui.canvas_widget import Canvas
from board import Board
from decorators import echo_which_turn, check_wrong_fig_for_turn, except_errors
from exceptions import IncorrectMovePatternError


class GameHandler(QWidget):
    def __init__(self, ):
        super().__init__()
        self.board = Board()
        self.canvas = Canvas(self.board, self)
        self.canvas.itemMovedEvent.connect(self.__accept_command)
        self.move_color = 1
    
    def start(self):
        self.board.fill_start_field()
        self.canvas.draw()
        self.canvas.show()
    
    @except_errors()
    @echo_which_turn
    def __accept_command(self, args):
        old_pos, new_pos = args
        fig = self.board.get_figure(old_pos)
        self.__make_move(fig, new_pos)
        self.move_color = 1 - self.move_color
    
    @check_wrong_fig_for_turn
    def __make_move(self, fig, pos2):
        if not fig.can_move(pos2):
            fig.move(fig.pos)
            raise IncorrectMovePatternError(fig, pos2)
        self.board.del_figure(pos2)
        fig.move(pos2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # db_session.global_init("db/plays.db")
    # session = db_session.create_session()
    g = GameHandler()
    g.start()
    sys.exit(app.exec())