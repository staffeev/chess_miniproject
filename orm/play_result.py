from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import relation, validates
from .db_session import SqlAlchemyBase
from exceptions import InvalidDataForDBError 
import datetime


class PlayResult(SqlAlchemyBase):
    """Класс для ORM-модели результата партии"""
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, autoincrement=True)
    win = Column(Integer)
    duration = Column(Integer)
    date = Column(DateTime, default=datetime.datetime.now)

    @validates("win")
    def validate_win(self, _, value):
        if not value in (0, 1):
            raise InvalidDataForDBError()
        return value
    
    @validates("duration")
    def validate_duration(self, _, value):
        if value < 0:
            raise InvalidDataForDBError()
        return value
    
    def __repr__(self):
        return f"PlayResult(date={self.date}, win={self.win})"
    
    def __str__(self):
        return self.name



    