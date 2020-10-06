import shortuuid
import random

from sqlalchemy import Index, Column, DateTime, Integer, String

from werkzeug.security import generate_password_hash, check_password_hash

from monarch.models.base import Base, TimestampMixin


def gen_user_name():
    """生成客户名称"""
    name = "游客"
    num = list(range(ord("0"), ord("9") + 1))
    lower_char = list(range(ord("a"), ord("z") + 1))
    upper_char = list(range(ord("A"), ord("Z") + 1))
    chars = num + lower_char + upper_char
    for i in range(6):
        c = random.choice(chars)
        name += str(chr(c))
    return name


class User(Base, TimestampMixin):
    '''用户表'''
    __tablename__ = "user"

    __table_args__ = (
        Index("account", "account"),
    )

    id = Column(String(32), default=shortuuid.uuid, nullable=False, primary_key=True)
    account = Column(String(64), unique=True, comment="账号")
    _password = Column("password", String(128), comment="密码")
    avatar = Column(String(128), nullable=True, comment="头像")
    nickname = Column(String(64), default=gen_user_name, comment="昵称")
    sex = Column(Integer, default=0, comment="1男，2女")
    email = Column(String(128), nullable=True, comment="邮箱")
    phone = Column(String(11), nullable=True, comment="手机号码")
    integral = Column(Integer, default=0, comment="积分")
    ip = Column(String(32), nullable=True, comment="登录IP地址")
    last_login = Column(DateTime, nullable=True, comment="最后登录时间")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

    def reset_password(self, new_password):
        self._password = generate_password_hash(new_password)
        self.save()
        return True

    @classmethod
    def get_by_account(cls, account, deleted=False):
        return cls.query.filter_by(
            account=account, deleted=deleted
        ).first()

    def _clean_cache(self):
        pass
