from sqlalchemy import Column, Integer, String, JSON

from monarch.models.base import Base, TimestampMixin, gen_uuid


class Service(Base, TimestampMixin):
    '''服务表'''
    __tablename__ = "service"

    id = Column(Integer, primary_key=True)
    sid = Column(String(64), default=gen_uuid, nullable=False, index=True)
    service = Column(String(64), comment="服务中文名称")
    name = Column(String(64), nullable=False)
    url = Column(String(128), nullable=False)


class ServiceLog(Base, TimestampMixin):
    __tablename__ = "service_log"

    id = Column(Integer, primary_key=True)
    sid = Column(String(64))
    user_id = Column(Integer, index=True)
    content = Column(JSON)
