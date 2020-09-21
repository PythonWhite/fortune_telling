from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy import UniqueConstraint

from monarch.models.base import Base, TimestampMixin
from monarch.utils.lots import gen_numbers


class LotsType(Base, TimestampMixin):
    __tablename__ = "lots_type"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)


class Lots(Base, TimestampMixin):
    __tablename__ = "lots"

    id = Column(Integer, primary_key=True)
    num = Column(Integer, comment="签号")
    lot_type = Column(Integer, comment="类型")
    content = Column(Text, comment="签文内容")
    name = Column(String(64), comment="签名")
    solution = Column(Text, comment="解签内容", nullable=True)
    poetry = Column(Text, comment="诗文", nullable=True)
    p_solution = Column(Text, comment="诗解", nullable=True)
    meaning = Column(Text, comment="签意", nullable=True)

    __table_args__ = (
        UniqueConstraint("lot_type", "num", name="type_num"),
    )

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


class Numerology(Base, TimestampMixin):
    __tablename__ = "numerology"

    __table_args__ = (
        UniqueConstraint("day_gan", "hour_gan", name="day_hour_gan"),
    )

    id = Column(Integer, primary_key=True)
    day_gan = Column(String(32), nullable=False, comment="天干")
    hour_gan = Column(String(32), nullable=False, comment="时干")
    hexagram_name = Column(String(32), nullable=False, comment="卦名")
    fate_name = Column(String(64), nullable=False, comment="格名")
    fate_desc = Column(Text(), nullable=False, comment="解释")
    fate_poetry = Column(Text(), nullable=False, comment="格诗")
    detail = Column(JSON(), nullable=False, comment="详情")
    star_desc = Column(Text(), nullable=False, comment="星宿解释")

    @classmethod
    def get_by_day_hour_gan(cls, day_gan, hour_gen):
        return cls.query.filter(
            cls.day_gan == day_gan
        ).filter(
            cls.hour_gen == hour_gen
        ).first()

    def delete_numerology(self):
        PreDestination.delete_by_numerology_id(self.id)
        self.delete(_commit=False, _hard=True)
        try:
            db.session.commit()
            return True
        except Exception as e:
            logger.error("删除Numerology失败:{}".format(e), exc_info=True)
            db.session.rollback()
            return False

class PreDestination(Base, TimestampMixin):
    __tablename__ = "pre_destination"

    id = Column(Integer, primary_key=True)
    hour_gz = Column(String(64), comment="时干支", nullable=False)
    numerology_id = Column(Integer(), nullable=False)
    name = Column(Text, comment="星名", nullable=False)

    @classmethod
    def delete_by_numerology_id(cls, numerology_id):
        db.session.query(cls).filter(cls.numerology_id==numerology_id).delete(synchronize_session=False)
