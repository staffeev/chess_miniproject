from game import Game
from orm import db_session
from threading import Thread
from functions import remind_play_time
import time
import asyncio


async def main():
    db_session.global_init("db/plays.db")
    session = db_session.create_session()
    g = Game(session)
    g.start()
    g.play()


def between_callback():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    loop.close()


if __name__ == "__main__":
    thread1 = Thread(target=between_callback)
    thread2 = Thread(target=remind_play_time, args=(time.time(), 10))
    tr = [thread1, thread2]
    [i.start() for i in tr]
    [i.join() for i in tr]