from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import relationship

from monarch.models.base import Base, TimestampMixin


class Permission(Base, TimestampMixin):
    '''用户权限'''
    __tablename__ = "permission"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(64), nullable=False, comment="菜单名称")
    parent_id = Column(Integer, nullable=False, default=0, comment="父级菜单ID")

    @staticmethod
    def menu_list_to_tree(menu_list):
        tree = {0: {"id": 0, "parent_id": 0, "name": "总后台", "children": []}}

        for menu in menu_list:
            tree.setdefault(menu["parent_id"], {"children": []})
            tree.setdefault(menu["id"], {"children": []})
            tree[menu["id"]].update(menu)
            tree[menu["parent_id"]]["children"].append(tree[menu["id"]])

        return tree[0]

    @classmethod
    def get_menus_by_ids(cls, menu_ids):
        menus = []
        if menu_ids:
            menus = cls.query.filter(cls.id.in_(menu_ids)).all()
        return menus

    @classmethod
    def get_by_name_and_parent_id(cls, name, parent_id):
        return cls.query.filter(cls.name == name, cls.parent_id == parent_id).first()


class PermissionGroup(Base, TimestampMixin):
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(64), nullable=False, comment="权限名称")
    description = Column(String(500), nullable=True, comment="权限组描述")
    permissions = Column(JSON, nullable=False, comment="权限ID集合")

    admin_users = relationship(
        "AdminUser",
        secondary="admin_user_permission",
        secondaryjoin="AdminUser.id==AdminUserPermission.admin_user_id",
        primaryjoin="PermissionGroup.id==AdminUserPermission.group_id"
    )

    @classmethod
    def get_permission_by_ids(cls, role_ids):
        roles = []
        if role_ids:
            roles = cls.query.filter(cls.id.in_(role_ids)).all()
        return roles

    def get_menus_tree(self):
        company_menus = Permission.get_menus_by_company_id()
        menu_id_set = set(self.permission)
        menu_list = []
        for menu in company_menus:
            menu_data = menu.to_dict(["id", "name", "parent_id"])
            menu_data["permission"] = menu_data.get("id") in menu_id_set
            menu_list.append(menu_data)
        return Permission.menu_list_to_tree(menu_list)

    @classmethod
    def get_by_name(cls, name, exclude_id=None):
        query = cls.query.filter_by(name=name)
        if exclude_id:
            query = query.filter(cls.id != exclude_id)
        return query.first()


class AdminUserPermission(Base, TimestampMixin):
    id = Column(Integer, primary_key=True)
    admin_user_id = Column(String(32), nullable=False, comment="管理员ID")
    group_id = Column(Integer(), nullable=False, comment="权限组ID")
