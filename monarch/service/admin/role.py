# -*- coding: utf-8 -*-
from flask import g

from monarch.models.permission import Permission, PermissionGroup
from monarch.forms.admin.role import RetQueryRoleSchma
from monarch.utils.api import biz_success, parse_pagination, Bizs
from monarch.exc import codes


def get_company_menus():
    current_user = g.user
    company_menus = Permission.query.all()
    fields = ["id", "name", "parent_id"]
    menu_dict_list = [item.to_dict(fields) for item in company_menus]
    menu_tree = Permission.menu_list_to_tree(menu_dict_list)
    return biz_success(menu_tree)


def create_role(data):
    user = g.user
    name = data["name"]

    if PermissionGroup.get_by_name(name):
        return Bizs.fail(msg="已存在该角色: %s" % name)

    PermissionGroup.create(**data)
    return biz_success()


def update_role(role_id, data):
    user = g.user
    name = data["name"]

    role = PermissionGroup.get(role_id)
    if not role:
        return biz_success(code=codes.CODE_NOT_FOUND, http_code=codes.HTTP_NOT_FOUND)

    if Role.get_by_name(name, role.id):
        return Bizs.fail(msg="已存在该角色: %s" % name)

    role.update(**data)
    return biz_success()


def delete_role(role_id):
    current_user = g.user
    role = PermissionGroup.get(role_id)
    if not role:
        return biz_success(code=codes.CODE_NOT_FOUND, http_code=codes.HTTP_NOT_FOUND)
    if role.admin_users:
        names = [item.name for item in role.admin_users]
        msg = "以下用户拥有该角色权限, 请取消权限后删除 %s" % ", ".join(names)
        return biz_success(
            code=codes.BIZ_CODE_FAIL, http_code=codes.HTTP_OK, msg=msg
        )
    role.delete(_hard=True)
    return biz_success()


def get_role(role_id):
    current_user = g.user
    role = PermissionGroup.get(role_id)
    if not role:
        return biz_success(code=codes.CODE_NOT_FOUND, http_code=codes.HTTP_NOT_FOUND)
    menu_tree = role.get_menus_tree()
    return biz_success(menu_tree)


def query_role(data):
    current_user = g.user
    query = PermissionGroup.query.order_by(
        PermissionGroup.created_at.desc()
    )
    data = parse_pagination(query)
    result, pagination = data["result"], data["pagination"]
    ret_list = RetQueryRoleSchma().dump(result, many=True).data
    ret_data = {"list": ret_list, "pagination": pagination}
    return biz_success(data=ret_data)
