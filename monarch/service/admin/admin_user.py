#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shortuuid
from datetime import datetime

from flask import g, request

from monarch.models.admin_user import AdminUser
from monarch.forms.admin import (
    RetCurrentAdminUserSchema,
)
from monarch.corelibs.mcredis import mc
from monarch.util.address import get_ip
from monarch.utils.api import Bizs
from monarch.exc.consts import (
    CACHE_ADMIN_USER_CAPTCHA_KEY,
    CACHE_ADMIN_USER_TOKEN,
    CACHE_TWELVE_HOUR,
)


def admin_login(data):
    account = data["account"]
    password = data["password"]
    captcha_value = data["captcha_value"]
    captcha_id = data["captcha_id"]
    captcha_cache_key = CACHE_ADMIN_USER_CAPTCHA_KEY.format(captcha_id)
    captcha_code = mc.get(captcha_cache_key)
    if not captcha_code:
        return Bizs.fail(msg="验证码不存在")

    if captcha_code != captcha_value:
        return Bizs.fail(msg="验证码错误")

    admin_user = AdminUser.get_by_account(account)
    if not admin_user:
        return Bizs.fail(msg="账号密码错误")
    if not admin_user.check_password(password):
        return Bizs.fail(msg="账号密码错误")

    admin_user.update(
        last_login=datetime.now(),
        ip=get_ip()
    )

    token = shortuuid.uuid()
    mc.set(CACHE_ADMIN_USER_TOKEN.format(token), admin_user.id, CACHE_TWELVE_HOUR)
    result = {
        "token": token,
        "expired_at": CACHE_TWELVE_HOUR,
        "account": admin_user.account,
        "id": admin_user.id
    }
    return Bizs.success(result)


def admin_logout():
    token = request.headers.get("token")
    mc.delete(CACHE_ADMIN_USER_TOKEN.format(token))
    return Bizs.success()


def create_admin_user(data):
    account = data["account"]
    password = data["password"]
    if AdminUser.get_by_account(account):
        return Bizs.fail(msg="账号已存在")
    AdminUser.create(
        account=account,
        password=password
    )
    return Bizs.success()


def get_current_admin_user_info():
    admin_user = g.admin_user
    data = RetCurrentAdminUserSchema().dump(admin_user).data
    return Bizs.success(data)


def reset_current_admin_user_password(data):
    current_admin_user = g.admin_user
    password = data["password"]
    if not current__admin_user.check_password(data["old_password"]):
        return Bizs.fail(msg="原密码错误")
    current_admin_user.reset_password(password)
    return Bizs.success()


def update_current_user_info(data):
    current_admin_user = g.admin_user
    current_admin_user.update(**data)
    return Bizs.success()
