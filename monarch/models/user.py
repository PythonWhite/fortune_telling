import shortuuid

from datetime import datetime
from sqlalchemy import Index, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from werkzeug.security import generate_password_hash, check_password_hash

from monarch.models.base import Base, TimestampMixin


class User(Base, TimestampMixin):
    '''用户表'''
    __tablename__ = "user"

    __table_args__ = (
        Index("account", "account"),
    )

    id = Column(String(32), default=shortuuid.uuid, nullable=False, primary_key=True)
    account = Column(String(64), unique=True, comment="账号")
    _password = Column("password", String(128))
    avatar = Column(String(128), default="", comment="头像")
    nick_name = Column(String(64), comment="昵称")
    real_name = Column(String(64), nullable=True, comment="真实姓名")
    sex = Column(Integer, default=0, comment="1男，2女")
    email = Column(String(128), nullable=True, unique=True,)
    phone = Column(String(11), nullable=True, unique=True,)
    integral = Column(String(32), default=0, comment="积分")
    ip = Column(String(32), nullable=True)
    last_login = Column(DateTime, default=datetime.now)

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


class AdminUser(Base, TimestampMixin):
    '''管理员表'''
    __tablename__ = "admin_user"

    id = Column(String(32), default=shortuuid.uuid, nullable=False, primary_key=True)
    nick_name = Column(String(64), comment="昵称")
    real_name = Column(String(64), nullable=True, comment="真实姓名")
    avatar = Column(String(128), default="", comment="头像")
    _password = Column("password", String(128))
    email = Column(String(128), nullable=True)
    phone = Column(String(11), nullable=True)
    last_login = Column(DateTime, default=datetime.now)
    ip = Column(String(32), nullable=True)

    permissions = relationship(
        "Permission",
        secondary="admin_user_permission",
        primaryjoin="AdminUser.id==AdminUserPermission.admin_user_id",
        secondaryjoin="PermissionGroup.id==AdminUserPermission.group_id"
    )

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
