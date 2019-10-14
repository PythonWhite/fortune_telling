import uuid
from datetime import datetime
from db import db


def gen_uuid():
    return uuid.uuid4().hex


class UserModel(db.Model):
    '''用户表'''
    __tablename__ = "user"

    id = db.Column('id', db.Integer, primary_key=True)
    uid = db.Column('uid', db.String(64), default=gen_uuid,
                    nullable=False, index=True)
    account = db.Column('account', db.String(64), unique=True,
                        index=True, comment="账号")
    password = db.Column('password', db.String(64))
    avatar = db.Column('avatar', db.String(128), default="", comment="头像")
    nick_name = db.Column('nick_num', db.String(64), comment="昵称")
    real_name = db.Column('real_name', db.String(
        64), nullable=True, comment="真实姓名")
    sex = db.Column('sex', db.Integer, default=1, comment="1男，0女")
    email = db.Column('email', db.String(128), nullable=True)
    phone = db.Column('phone', db.String(32), nullable=True)
    integral = db.Column('integral', db.String(32), default=0, comment="积分")
    ip = db.Column('ip', db.String(32), nullable=True)
    last_login = db.Column('last_login', db.DateTime, default=datetime.now)
    created = db.Column('created', db.DateTime, default=datetime.now)
    updated = db.Column('updated', db.DateTime,
                        default=datetime.now, onupdate=datetime.now)


class AdminUserModel(db.Model):
    '''管理员表'''
    __tablename__ = "admin_user"

    id = db.Column('id', db.Integer, primary_key=True)
    nick_name = db.Column('nick_num', db.String(64), comment="昵称")
    real_name = db.Column('real_name', db.String(
        64), nullable=True, comment="真实姓名")
    avatar = db.Column('avatar', db.String(128), default="", comment="头像")
    password = db.Column('password', db.String(64))
    email = db.Column('email', db.String(128), nullable=True)
    phone = db.Column('phone', db.String(32), nullable=True)
    last_login = db.Column('last_login', db.DateTime, default=datetime.now)
    created = db.Column('created', db.DateTime, default=datetime.now)
    updated = db.Column('updated', db.DateTime,
                        default=datetime.now, onupdate=datetime.now)
    is_enable = db.Column('is_enable', db.Integer,
                          default=0, comment="0启用，1禁用")
    ip = db.Column('ip', db.String(32), nullable=True)


class PermissionModel(db.Model):
    '''用户权限'''
    __tablename__ = "permission"

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(64))
    user_id = db.Column('user_id', db.Integer, nullable=True)
    created = db.Column('created', db.DateTime, default=datetime.now)
    updated = db.Column('updated', db.DateTime,
                        default=datetime.now, onupdate=datetime.now)
    is_enable = db.Column('is_enable', db.Integer,
                          default=0, comment="0启用，1禁用")


class UserVipModel(db.Model):
    __tablename__ = "user_vip"

    id = db.Column('id', db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.ForeignKey('user.id'))
    start_time = db.Column('start_time', db.DateTime, nullable=True)
    end_time = db.Column('end_time', db.DateTime, nullable=True)
    vip_len = db.Column('vip_len', db.Integer, comment="会员时长")
    vip_grade = db.Column('vip_grdae', db.Integer, default=1, comment="会员等级")
    is_expired = db.Column('is_expired', db.Integer,
                           default=0, comment="0未过期，1过期")


class ServiceModel(db.Model):
    '''服务表'''
    __tablename__ = "service"

    id = db.Column('id', db.Integer, primary_key=True)
    sid = db.Column('sid', db.String(64), default=gen_uuid,
                    nullable=False, index=True)
    service = db.Column('service', db.String(64), comment="服务中文名称")
    name = db.Column('name', db.String(64))
    url = db.Column('url', db.String(128))
    created = db.Column('created', db.DateTime, default=datetime.now)
    updated = db.Column('updated', db.DateTime,
                        default=datetime.now, onupdate=datetime.now)
    is_enable = db.Column('is_enable', db.Integer,
                          default=0, comment="0启用，1禁用")


class ServiceLogModel(db.Model):
    __tablename__ = "service_log"

    id = db.Column('id', db.Integer, primary_key=True)
    sid = db.Column('sid', db.String(64))
    user_id = db.Column('user_id', db.ForeignKey('user.id'), index=True)
    created = db.Column('created', db.DateTime, default=datetime.now)
    content = db.Column('content', db.Text)


class OrderModel(db.Model):
    __tablename__ = "order"

    id = db.Column('id', db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.ForeignKey('user.id'))
    created = db.Column('created', db.DateTime, default=datetime.now)
    uid = db.Column('uid', db.String(64), default=gen_uuid,
                    nullable=False, index=True)
    flow_id = db.Column('flow_id', db.String(64), comment="第三方支付id")
    amount = db.Column('amount', db.String(32), nullable=False, comment="金额")
    pay_time = db.Column('pay_time', db.DateTime,
                         nullable=True, comment="支付时间")
    status = db.Column('status', db.Integer, default=1,
                       comment="支付状态1未支付，0支付成功，-1支付失败")


class LotsModel(db.Model):
    __tablename__ = "lots"

    id = db.Column('id', db.Integer, primary_key=True)
    num = db.Column('num', db.Integer, comment="签号")
    lot_type = db.Column('lot_type', db.String(32), comment="类型")
    content = db.Column('content', db.Text, comment="签文内容")
    created = db.Column('created', db.DateTime, default=datetime.now)
    name = db.Column('name', db.String(64), comment="签名")
    solution = db.Column('solution', db.Text, comment="解签内容", nullable=True)
    poetry = db.Column('poetry', db.Text, comment="诗文", nullable=True)
    p_solution = db.Column('p_solution', db.Text, comment="诗解", nullable=True)
    meaning = db.Column('meaning', db.Text, comment="签意", nullable=True)


class PreDestinationModel(db.Model):
    __tablename__ = "pre_destination"

    id = db.Column('id', db.Integer, primary_key=True)
    horoscope = db.Column('horoscope', db.String(64), comment="八字")
    name = db.Column('name', db.Text, comment="星名")
    content = db.Column('content', db.Text)
    created = db.Column('created', db.DateTime, default=datetime.now)


class ArticleModel(db.Model):
    __tablename__ = "article"

    id = db.Column('id', db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.ForeignKey('user.id'))
    title = db.Column('title', db.String(255))
    introduction = db.Column('introduction', db.Text, comment="简介")
    content = db.Column('content', db.Text)
    cover = db.Column('cover', db.String(255), comment="封面")
    author = db.Column('author', db.String(32), comment="作者")
    type = db.Column('type', db.Integer, default=0, comment="0原创，1转载，2书籍")
    is_enable = db.Column('is_enable', db.Integer,
                          default=0, comment="0启用，1禁用")
    created = db.Column('created', db.DateTime, default=datetime.now)
    updated = db.Column('updated', db.DateTime,
                        default=datetime.now, onupdate=datetime.now)
