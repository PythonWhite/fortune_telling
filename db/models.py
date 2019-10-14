import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, BigInteger, DateTime,\
     ForeignKey, Date

Base = declarative_base()  # 声明映射基类


def gen_uuid():
    return uuid.uuid4().hex

class UserModel(Base):
    '''用户表'''
    __tablename__ = "user"

    id = Column('id', Integer, primary_key=True)
    uid = Column('uid', String(64), default=gen_uuid, nullable=False, index=True)
    account = Column('account', String(64), unique=True, index=True, comment="账号")
    password = Column('password', String(64))
    avatar = Column('avatar', String(128), default="", comment="头像")
    nick_name = Column('nick_num', String(64), comment="昵称")
    real_name = Column('real_name', String(64), nullable=True, comment="真实姓名")
    sex = Column('sex', Integer, default=1, comment="1男，0女")
    email = Column('email', String(128), nullable=True)
    phone = Column('phone', String(32), nullable=True)
    integral = Column('integral', BigInteger, default=0, comment="积分")
    ip = Column('ip', String(32), nullable=True)
    last_login = Column('last_login', DateTime, default=datetime.now)
    created = Column('created', DateTime, default=datetime.now)
    updated = Column('updated', DateTime, default=datetime.now, onupdate=datetime.now)
    is_enable = Column('is_enable', Integer, default=0, comment="0启用，1禁用")


class PermissionModel(Base):
    '''用户权限'''
    __tablename__ = "permission"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(64))
    user_id = Column('user_id', Integer, nullable=True)
    created = Column('created', DateTime, default=datetime.now)
    updated = Column('updated', DateTime, default=datetime.now, onupdate=datetime.now)
    is_enable = Column('is_enable', Integer, default=0, comment="0启用，1禁用")

class UserVipModel(Base):
    __tablename__ = "user_vip"

    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', ForeignKey('user.id'))
    start_time = Column('start_time', DateTime, nullable=True)
    end_time = Column('end_time', DateTime, nullable=True)
    vip_len = Column('vip_len', Integer, comment="会员时长")
    vip_grade = Column('vip_grdae', Integer, default=1, comment="会员等级")
    is_expired = Column('is_expired', Integer, default=0, comment="0未过期，1过期")


class ServiceModel(Base):
    '''服务表'''
    __tablename__ = "service"

    id = Column('id', Integer, primary_key=True)
    sid = Column('sid', String(64), default=gen_uuid, nullable=False, index=True)
    service = Column('service', String(64), comment="服务中文名称")
    name = Column('name', String(64))
    url = Column('url', String(128))
    created = Column('created', DateTime, default=datetime.now)
    updated = Column('updated', DateTime, default=datetime.now, onupdate=datetime.now)
    is_enable = Column('is_enable', Integer, default=0, comment="0启用，1禁用")

class ServiceLogModel(Base):
    __tablename__ = "service_log"

    id = Column('id', Integer, primary_key=True)
    sid = Column('sid', String(64))
    user_id = Column('user_id', ForeignKey('user.id'), index=True)
    created = Column('created', DateTime, default=datetime.now)
    content = Column('content', Text)

class OrderModel(Base):
    __tablename__ = "order"

    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', ForeignKey('user.id'))
    created = Column('created', DateTime, default=datetime.now)
    uid = Column('uid', String(64), default=gen_uuid, nullable=False, index=True)
    flow_id = Column('flow_id', String(64), comment="第三方支付id")
    amount = Column('amount', String(32), nullable=False, comment="金额")
    pay_time = Column('pay_time', DateTime, nullable=True, comment="支付时间")
    status = Column('status', Integer, default=1, comment="支付状态1未支付，0支付成功，-1支付失败")

class LotsModel(Base):
    __tablename__ = "lots"

    id = Column('id', Integer, primary_key=True)
    num = Column('num', Integer, comment="签号")
    lot_type = Column('lot_type', String(32), comment="类型")
    content = Column('content', Text, comment="签文内容")
    created = Column('created', DateTime, default=datetime.now)
    name = Column('name', String(64), comment="签名")
    solution = Column('solution', Text, comment="解签内容", nullable=True)
    poetry = Column('poetry', Text, comment="诗文", nullable=True)
    p_solution = Column('p_solution', Text, comment="诗解", nullable=True)
    meaning = Column('meaning', Text, comment="签意", nullable=True)

class PreDestinationModel(Base):
    __tablename__ = "pre_destination"

    id = Column('id', Integer, primary_key=True)
    horoscope = Column('horoscope', String(64), comment="八字")
    name = Column('name', Text, comment="星名")
    content = Column('content', Text)
    created = Column('created', DateTime, default=datetime.now)

class ArticleModel(Base):
    __tablename__ = "article"

    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', ForeignKey('user.id'))
    title = Column('title', String(255))
    introduction = Column('introduction', Text, comment="简介")
    content = Column('content', Text)
    cover = Column('cover', String(255), comment="封面")
    author = Column('author', String(32), comment="作者")
    type = Column('type', Integer, default=0, comment="0原创，1转载，2书籍")
    is_enable = Column('is_enable', Integer, default=0, comment="0启用，1禁用")
    created = Column('created', DateTime, default=datetime.now)
    updated = Column('updated', DateTime, default=datetime.now, onupdate=datetime.now)









