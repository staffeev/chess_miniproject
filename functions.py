import time
import re
from orm.play_move import PlayMove
from orm.play_result import PlayResult


async def get_duration(start_time):
    return int(time.time() - start_time)


def remind_play_time(start_time, period):
    while True:
        time.sleep(period)
        print(f"Игровая партия длится уже {round((time.time() - start_time) / 60, 2)} минут")


def get_all_moves(session):
    return session.query(PlayMove).all()


def get_all_results(session):
    return session.query(PlayResult).all()


def create_new_game(session):
    play = PlayResult()
    session.add(play)
    session.commit()
    return play


def create_new_move(session, figure, color, pos1, pos2, result_id):
    move = PlayMove(figure=figure, color=color, prev_pos=str(pos1), new_pos=str(pos2),
                    result_id=result_id)
    session.add(move)
    session.commit()
    return move


def update_result_by_id(session, play_id, duration, win):
    result = session.query(PlayResult).filter(PlayResult.id == play_id).first()
    result.duration = duration
    result.win = win
    session.commit()