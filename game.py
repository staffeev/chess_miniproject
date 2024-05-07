from board import Board
from gui import Canvas
from figures.figures import *
from decorators import check_wrong_fig_for_turn, echo_which_turn
from exceptions import OutOfBoundsException, IncorrectMovePatternError, WrongTurnColorError
from dot import Dot
from figures.metaclass import ABCFigureMeta
from sys import exit
from functions import *
import time


class Game:
    def __init__(self, session, gui_type=Canvas):
        self.board = Board()
        self.canvas = gui_type(self.board)
        self.session = session
        self.start_time = time.time()
        self.cur_play = create_new_game(self.session)
        self.move_color = 1
    
    def start(self):
        self.board.fill_start_field()
        self.canvas.draw()
    
    async def play(self):
        while True:
            try:
                self.__accept_command()
                self.move_color = 1 - self.move_color
            except (OutOfBoundsException, IncorrectMovePatternError, 
                    WrongTurnColorError) as e:
                print(e)
            except ValueError:
                print("Данные введены в неверном формате")
            except Exception as e:
                print(f"Произошла непредвиденная ошибка:\n{e}")
            print()
            self.canvas.draw()
            if (res := self.is_checkmate()) is not None:
                await self.game_over(res)
    
    async def game_over(self, res):
        print("Победили", "белые" if res == 0 else "черные")
        self.print_statistics()
        duration = await get_duration(self.start_time)
        update_result_by_id(self.session, self.cur_play.id, duration, 1 - res)
        self.session.close()
        exit(0)


    @staticmethod
    def print_statistics():
        for cls in ABCFigureMeta.reg:
            print(f"Фигуры {cls.__name__} походили {cls.num_of_moves} раз")
    
    def is_checkmate(self):
        for fig in self.board.field:
            if fig.__class__ == King and fig.is_mate():
                return fig.color
        return None
    
    @echo_which_turn
    def __accept_command(self):
        cmd = input("Введите координаты фигуры и точки для хода через в формате `x1 y1 x2 y2`:\n")
        x_1, y_1, x_2, y_2 = map(int, cmd.split())
        fig = self.board.get_figure(Dot(x_1, y_1) - Dot(1, 1))
        dest = Dot(x_2, y_2) - Dot(1, 1)
        self.__make_move(fig, dest)
    
    @check_wrong_fig_for_turn
    def __make_move(self, fig, pos2):
        if not fig.can_move(pos2):
            raise IncorrectMovePatternError(fig, pos2)
        self.board.del_figure(pos2)
        create_new_move(self.session, fig.__class__.__name__, fig.color, fig.pos, pos2,
                        self.cur_play.id)
        fig.move(pos2)
