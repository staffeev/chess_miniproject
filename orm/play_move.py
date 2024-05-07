from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relation, validates
from .db_session import SqlAlchemyBase
from exceptions import InvalidDataForDBError


class PlayMove(SqlAlchemyBase):
    """Класс для ORM-модели для хода"""
    __tablename__ = "moves"
    id = Column(Integer, primary_key=True, autoincrement=True)
    figure = Column(String)
    color = Column(Integer)
    prev_pos = Column(String)
    new_pos = Column(String)
    result_id = Column(Integer, ForeignKey('results.id'))

    @validates("color")
    def validate_color(self, _, value):
        """Проверка допустимых значений для цвета"""
        if not value in (0, 1):
            raise InvalidDataForDBError()
        return value
    
    def __repr__(self):
        return f"PlayMove(fig={self.figure}, color={self.color}, prev_pos={self.prev_pos}, new_pos={self.new_pos})"
    
    def __str__(self):
        return self.name



    