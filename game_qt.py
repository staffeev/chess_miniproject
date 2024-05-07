from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsView
from PyQt5 import uic
import sys
from gui.canvas_widget import Canvas
from board import Board
from decorators import echo_which_turn, check_wrong_fig_for_turn
from exceptions import IncorrectMovePatternError
from dot import Dot


class GameHandler(QWidget):
    def __init__(self):
        super().__init__()
        self.board = Board()
        self.canvas = Canvas(self.board, self)
        self.canvas.itemMovedEvent.connect(self.__accept_command)
        self.move_color = 1
    
    @echo_which_turn
    def __accept_command(self, args):
        canvas_figure, old_pos, new_pos, event = args
        print("AAAA")
        fig = self.board.get_figure(old_pos)
        if self.__make_move(fig, new_pos):
            canvas_figure.acceptReleaseEvent(event)
        else:
            self.canvas.draw()
    
    @check_wrong_fig_for_turn
    def __make_move(self, fig, pos2):
        if not fig.can_move(pos2):
            raise IncorrectMovePatternError(fig, pos2)
        self.board.del_figure(pos2)
        fig.move(pos2)
        return True

    def start(self):
        self.board.fill_start_field()
        self.canvas.draw()
        self.canvas.show()
    

    

    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # db_session.global_init("db/plays.db")
    # session = db_session.create_session()
    g = GameHandler()
    g.start()
    sys.exit(app.exec())