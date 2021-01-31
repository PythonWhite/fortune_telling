#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shortuuid

from sqlalchemy import Column, DateTime, String, Boolean
from sqlalchemy.orm import relationship

from werkzeug.security import generate_password_hash, check_password_hash

from monarch.models.base import Base, TimestampMixin


class AdminUser(Base, TimestampMixin):
    '''管理员表'''
    __tablename__ = "admin_user"

    id = Column(String(32), default=shortuuid.uuid, nullable=False, primary_key=True)
    account = Column(String(64), unique=True, comment="账号")
    name = Column(String(64), nullable=True, comment="真实姓名")
    avatar = Column(String(128), nullable=True, comment="头像")
    _password = Column("password", String(128), comment="密码")
    email = Column(String(128), nullable=True, comment="邮箱")
    phone = Column(String(11), nullable=True, comment="手机号码")
    last_login = Column(DateTime, nullable=True, comment="最后登录时间")
    ip = Column(String(32), nullable=True, comment="ip")
    is_admin = Column(Boolean, nullable=False, default=False, comment="是否为超管")

    '''permissions = relationship(
        "Permission",
        secondary="admin_user_permission",
        primaryjoin="AdminUser.id==AdminUserPermission.admin_user_id",
        secondaryjoin="PermissionGroup.id==AdminUserPermission.group_id"
    )'''

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
    def get_all(cls, delete=False):
        return cls.query.filter(cls.delete == delete).order_by(cls.created_at.desc())

    @classmethod
    def get_user_by_id(cls, _id, delete=False):
        return cls.query.filter(cls.id == _id, cls.delete == delete).first()

    @classmethod
    def exist_user(cls, q_field, q, exclude_user_id=None):
        query = cls.query.filter_by(**{q_field: q}).filter(cls.id != exclude_user_id)
        return bool(query.first())

    @classmethod
    # @model_cache(CACHE_USER_BY_ACCOUNT, CACHE_DAY)
    def get_by_account(cls, account, deleted=False):
        return cls.query.filter_by(
            account=account,
            deleted=deleted,
        ).first()

    @property
    def get_menu_ids(self):
        return [item.id for item in self.permissions]

    def get_menus_tree(self):
        menus = Permission.query.all()
        menu_id_set = set(self.get_menu_ids)
        menu_list = []
        for menu in menus:
            menu_data = menu.to_dict(["id", "name", "parent_id"])
            menu_data["permission"] = menu_data.get("id") in menu_id_set
            menu_list.append(menu_data)
        return Permission.menu_list_to_tree(menu_list)


from monarch.models.permission import Permission
