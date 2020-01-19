from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy import UniqueConstraint

from monarch.models.base import Base, TimestampMixin
from monarch.utils.lots import gen_numbers


class Lots(Base, TimestampMixin):
    __tablename__ = "lots"

    id = Column(Integer, primary_key=True)
    num = Column(Integer, comment="签号")
    lot_type = Column(String(32), comment="类型")
    content = Column(Text, comment="签文内容")
    name = Column(String(64), comment="签名")
    solution = Column(Text, comment="解签内容", nullable=True)
    poetry = Column(Text, comment="诗文", nullable=True)
    p_solution = Column(Text, comment="诗解", nullable=True)
    meaning = Column(Text, comment="签意", nullable=True)

    UniqueConstraint("lot_type", "num", name="type_num")

    @classmethod
    def exist_num(cls, num, lot_type):
        query = cls.query.filter(
            cls.lot_type == lot_type
        ).filter(
            cls.num == num
        )
        return bool(query.first())

    @classmethod
    def random_gen_lot(cls, lot_type):
        query = cls.query.filter(
            cls.lot_type == lot_type
        ).all()
        return gen_numbers(query)

    @classmethod
    def get_lot_by_num_and_type(cls, lot_type, num):
        query = cls.query.filter(
            cls.lot_type == lot_type
        ).filter(
            cls.num == num
        )
        return query.first()


class PreDestination(Base, TimestampMixin):
    __tablename__ = "pre_destination"

    id = Column(Integer, primary_key=True)
    horoscope = Column(String(64), comment="八字", nullable=False)
    name = Column(Text, comment="星名", nullable=False)
    content = Column(Text, nullable=False)

    @classmethod
    def exist_num(cls, num, lot_type):
        query = cls.query.filter(
            cls.lot_type == lot_type
        ).filter(
            cls.num == num
        )
        return bool(query.first())
