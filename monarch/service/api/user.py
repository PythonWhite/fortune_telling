#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shortuuid
from datetime import datetime

from flask import g, request

from monarch.models.user import User, UserBrowseLog, ActionLog
from monarch.models.article import ArticleModel
from monarch.forms.admin.article import (
    CurrentArticleSchema
)
from monarch.models.video import CourseModel
from monarch.forms.admin.course import CoursesSchema
from monarch.forms.api.user import (
    RetCurrentUserSchema,
)
from monarch.models.service import Service, ServiceLog
from monarch.corelibs.mcredis import mc
from monarch.utils.address import get_ip
from monarch.utils.api import Bizs, parse_pagination
from monarch.exc.consts import (
    # CACHE_USER_CAPTCHA_KEY,
    CACHE_USER_TOKEN,
    CACHE_TWELVE_HOUR,
)


def login(data):
    account = data["account"]
    password = data["password"]
    # captcha_value = data["captcha_value"]
    # captcha_id = data["captcha_id"]
    # captcha_cache_key = CACHE_USER_CAPTCHA_KEY.format(captcha_id)
    # captcha_code = mc.get(captcha_cache_key)
    # if not captcha_code:
    #    return Bizs.fail(msg="验证码不存在")

    # if captcha_code != captcha_value:
    #    return Bizs.fail(msg="验证码错误")

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
    if not ActionLog.get_by_user_id_and_day(user.id, "登录", datetime.now().date()):
        ActionLog.create(
            user_id=user.id,
            action="登录",
            day=datetime.now().date()
        )
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


def get_current_user_browse_articles():
    logs = UserBrowseLog.get_user_browse_log(g.user.id, ArticleModel.__tablename__)
    p_data = parse_pagination(logs)
    article_ids = [log.model_id for log in p_data["result"]]
    articles = ArticleModel.get_by_ids(article_ids)
    result = CurrentArticleSchema().dump(articles, many=True).data
    return Bizs.success({
        "list": result,
        "pagination": p_data["pagination"]
    })


def get_current_user_browse_course():
    logs = UserBrowseLog.get_user_browse_log(g.user.id, CourseModel.__tablename__)
    p_data = parse_pagination(logs)
    course_ids = [log.model_id for log in p_data["result"]]
    courses = CourseModel.get_by_ids(course_ids)
    result = CoursesSchema().dump(courses, many=True).data
    return Bizs.success({
        "list": result,
        "pagination": p_data["pagination"]
    })


def get_current_user_service_logs(service_type):
    service = Service.get_by_name(service_type)
    if not service:
        return Bizs.fail(msg="服务不存在")
    logs = ServiceLog.get_logs_by_user_id(g.user.id, service.id)
    result = [log.content for log in logs]
    return Bizs.success(result)


def get_hot_top5():
    query = CourseModel.get_courses_likes_top5()
    courses = CoursesSchema().dump(query, many=True).data
    for item in courses:
        item["type"] = "course"

    query = ArticleModel.get_articles_likes_top5(is_books=False)
    articles = CurrentArticleSchema().dump(query, many=True).data
    for item in articles:
        item["type"] = "article"
    return Bizs.success(courses + articles)
