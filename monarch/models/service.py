from sqlalchemy import Column, Index, UniqueConstraint, Integer, String, JSON

from monarch.models.base import Base, TimestampMixin, gen_uuid
from monarch.corelibs.store import db
from monarch.exc.consts import DEFAULT_SERVICES, ServiceType
from monarch.utils import logger


class Service(Base, TimestampMixin):
    '''服务表'''
    __tablename__ = "service"

    __table_args__ = (
        UniqueConstraint("key"),
    )

    id = Column(String(64), default=gen_uuid, nullable=False, primary_key=True)
    key = Column(String(64), comment="服务中文名称")
    name = Column(String(64), nullable=False)
    url = Column(String(128), nullable=False)

    @classmethod
    def create_default_services(cls):
        for item in DEFAULT_SERVICES:
            cls.create(_commit=False, **item)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(e, exc_info=True)

    @classmethod
    def get_by_name(cls, key):
        return cls.query.filter(cls.key == key).first()


class ServiceLog(Base, TimestampMixin):
    __tablename__ = "service_log"

    __tanle_args__ = (
        Index("idx_user_id", "user_id"),
        Index("idx_sid", "sid"),
    )

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    sid = Column(String(64), nullable=False, comment="服务ID")
    user_id = Column(String(32), nullable=False, comment="用户ID")
    content = Column(JSON, nullable=False, comment="内容")

    @classmethod
    def get_logs_by_user_id(cls, user_id, sid):
        query = cls.query.filter(
            cls.user_id == user_id,
            cls.sid == sid
        )
        return query.all()

    @classmethod
    def create_by_lots(cls, user_id, content):
        service = Service.get_by_name(ServiceType.LOTS)
        cls.create(
            sid=service.id,
            user_id=user_id,
            content=content
        )
