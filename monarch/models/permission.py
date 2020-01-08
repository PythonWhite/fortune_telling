from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import relationship

from monarch.models.base import Base, TimestampMixin


class Permission(Base, TimestampMixin):
    '''用户权限'''
    __tablename__ = "permission"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))


class PermissionGroup(Base, TimestampMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    description = Column(String(500), comment="权限组描述")
    permissions = Column(JSON)

    admin_users = relationship(
        "AdminUser",
        secondary="admin_user_permission",
        secondaryjoin="AdminUser.id==AdminUserPermission.admin_user_id",
        primaryjoin="PermissionGroup.id==AdminUserPermission.group_id"
    )


class AdminUserPermission(Base, TimestampMixin):
    id = Column(Integer, primary_key=True)
    admin_user_id = Column(String(32), nullable=False, comment="管理员ID")
    group_id = Column(Integer(), nullable=False, comment="权限组ID")
