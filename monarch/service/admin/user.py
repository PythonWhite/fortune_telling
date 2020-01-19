import base64
import datetime
import shortuuid

from flask import g, request
from monarch.utils.date import datetime_to_timestamp

from monarch.corelibs.captcha import gen_captcha, check_pass
from monarch.models.user import User, AdminUser
from monarch.models.permission import PermissionGroup
from monarch.utils.api import Bizs, parse_pagination
from monarch.forms.admin.user import (
    RetCurrentUserSchema,
    RetQueryUserSchema,
    RetCurrentUserInfoSchema
)
from monarch.exc.consts import (
    CACHE_ADMIN_USER_CAPTCHA,
    CACHE_TWELVE_HOUR,
    CACHE_FIVE_MINUTE,
    CACHE_ADMIN_USER_TOKEN,
)
from monarch.corelibs.mcredis import mc


def get_a_captcha(data):
    t = data.get("t")
    code, image_data = gen_captcha(num=4)
    mc.set(CACHE_ADMIN_USER_CAPTCHA.format(t), code, CACHE_FIVE_MINUTE)
    data = {
        "image": image_data,
    }
    return Bizs.success(data)


def user_login(data):
    account = data.get("account")
    password = data.get("password")
    t = data.get("t")
    code = data.get("code")

    cache_user_captcha_key = CACHE_USER_CAPTCHA.format(t)
    captcha_code = mc.get(cache_user_captcha_key)
    if not captcha_code:
        return Bizs.bad_query(msg="验证码不存在")

    if not check_pass(code, captcha_code):
        return Bizs.bad_query(msg="验证码错误")

    user = AdminUser.get_by_account(account)
    if not user:
        return Bizs.fail(msg="账号不存在或被禁用")

    if not user.check_password(password):
        return Bizs.fail(msg="账号密码错误")

    token = shortuuid.uuid()
    mc.set(CACHE_ADMIN_USER_TOKEN.format(token), user.id, CACHE_TWELVE_HOUR)
    result = {
        "token": token,
        "expired_at": CACHE_TWELVE_HOUR,
        "account": user.account,
        "id": user.id,
    }
    g.admin_user = user
    return Bizs.success(result)


def user_logout():
    token = request.headers.get("token")
    mc.delete(CACHE_ADMIN_USER_TOKEN.format(token))
    return Bizs.success()


def update_user(user_id, data):
    name = data["name"]
    user = AdminUser.get_user_by_id(user_id)
    if not user:
        return Bizs.not_found()
    if AdminUser.exist_user("name", name, user.id):
        return Bizs.bad_query(msg="名字已存在")

    data["permissions"] = PermissionGroup.get_permission_by_ids(data.get("roles"))
    user.update(**data)
    return Bizs.success()


def create_user(data):
    account = data["account"]
    nickname = data["name"]
    if AdminUser.get_by_account(account):
        return Bizs.bad_query(msg="账号已存在")
    if AdminUser.exist_user("name", name):
        return Bizs.bad_query(msg="名称已存在")
    data["permissions"] = PermissionGroup.get_permission_by_ids(data.get("roles"))
    AdminUser.create(**data)
    return Bizs.success()


def delete_user(uid):
    user = AdminUser.get_user_by_id(uid)
    if not user:
        return Bizs.not_found()

    user.delete()
    return Bizs.success()


def query_user(data):
    current_user = g.user
    role_id = data.get("role_id")
    enabled = data.get("enabled")
    is_online = data.get("is_online")
    data = parse_pagination(
        User.query_user(
            company_id=current_user.company_id,
            enabled=enabled,
            role_id=role_id,
            is_online=is_online,
        )
    )
    result, pagination = data["result"], data["pagination"]
    ret_list = RetQueryUserSchema().dump(result, many=True).data
    online_num = User.query_user(current_user.company_id, is_online=True).count()
    ret_data = {"list": ret_list, "pagination": pagination, "online_num": online_num}
    return Bizs.success(data=ret_data)


def get_user_menu_tree():
    current_user = g.admin_user
    menu_tree = current_user.get_menus_tree()
    return Bizs.success(menu_tree)


def get_current_user():
    current_user = g.admin_user
    data = RetCurrentUserSchema().dump(current_user).data
    return Bizs.success(data)


def get_current_user_info():
    current_user = g.admin_user
    data = RetCurrentUserInfoSchema().dump(current_user).data
    return Bizs.success(data)


def update_current_user_info(data):
    current_user = g.admin_user
    current_user.update(**data)
    return Bizs.success()


def reset_current_user_password(data):
    current_user = g.admin_user
    password = data['password']

    if not current_user.check_password(data['old_password']):
        return Bizs.bad_query(msg="原密码错误")

    current_user.reset_password(password)
    return Bizs.success()