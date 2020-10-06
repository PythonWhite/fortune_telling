#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shortuuid
from datetime import datetime

from flask import g, request

from monarch.models.user import User
from monarch.forms.api import (
    RetCurrentUserSchema,
)
from monarch.corelibs.mcredis import mc
from monarch.util.address import get_ip
from monarch.utils.api import Bizs
from monarch.exc.consts import (
    CACHE_USER_CAPTCHA_KEY,
    CACHE_USER_TOKEN,
    CACHE_TWELVE_HOUR,
)


def login(data):
    account = data["account"]
    password = data["password"]
    captcha_value = data["captcha_value"]
    captcha_id = data["captcha_id"]
    captcha_cache_key = CACHE_USER_CAPTCHA_KEY.format(captcha_id)
    captcha_code = mc.get(captcha_cache_key)
    if not captcha_code:
        return Bizs.fail(msg="验证码不存在")

    if captcha_code != captcha_value:
        return Bizs.fail(msg="验证码错误")

    user = User.get_by_account(account)
    if not user:
        return Bizs.fail(msg="账号密码错误")
    if not user.check_password(password):
        return Bizs.fail(msg="账号密码错误")

    user.update(
        last_login=datetime.now(),
        ip=get_ip()
    )

    token = shortuuid.uuid()
    mc.set(CACHE_USER_TOKEN.format(token), user.id, CACHE_TWELVE_HOUR)
    result = {
        "token": token,
        "expired_at": CACHE_TWELVE_HOUR,
        "account": user.account,
        "id": user.id
    }
    return Bizs.success(result)


def logout():
    token = request.headers.get("token")
    mc.delete(CACHE_USER_TOKEN.format(token))
    return Bizs.success()


def registered(data):
    account = data["account"]
    password = data["password"]
    if User.get_by_account(account):
        return Bizs.fail(msg="账号已存在")
    User.create(
        account=account,
        password=password
    )
    return Bizs.success()


def get_current_user_info():
    user = g.user
    data = RetCurrentUserSchema().dump(user).data
    return Bizs.success(data)


def reset_current_user_password(data):
    current_user = g.user
    password = data["password"]
    if not current_user.check_password(data["old_password"]):
        return Bizs.fail(msg="原密码错误")
    current_user.reset_password(password)
    return Bizs.success()


def update_current_user_info(data):
    current_user = g.user
    current_user.update(**data)
    return Bizs.success()
