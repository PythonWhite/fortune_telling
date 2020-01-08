from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy import UniqueConstraint

from monarch.models.base import Base, TimestampMixin


class Lots(Base, TimestampMixin):
    __tablename__ = "lots"

    id = Column(Integer, primary_key=True)
    num = Column(Integer, comment="签号")
    lot_type = Column(String(32), comment="类型")
    content = Column(Text, comment="签文内容")
    created = Column(DateTime, default=datetime.now)
    name = Column(String(64), comment="签名")
    solution = Column(Text, comment="解签内容", nullable=True)
    poetry = Column(Text, comment="诗文", nullable=True)
    p_solution = Column(Text, comment="诗解", nullable=True)
    meaning = Column(Text, comment="签意", nullable=True)

    UniqueConstraint("lot_type", "num", name="type_num")


class PreDestination(Base, TimestampMixin):
    __tablename__ = "pre_destination"

    id = Column(Integer, primary_key=True)
    horoscope = Column(String(64), comment="八字")
    name = Column(Text, comment="星名")
    content = Column(Text)
