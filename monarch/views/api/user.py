#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import g
from flask_restplus import Resource, Namespace
from flask_restplus._http import HTTPStatus

from monarch.service.api.user import (
    login,
    logout,
    registered,
    get_current_user_info,
    update_current_user_info,
    reset_current_user_password,
    get_current_user_browse_articles,
    get_current_user_browse_course,
    get_current_user_service_logs,
)
from monarch.forms.api.user import (
    UpdateCurrentUserInfoSchema,
    UserLoginSchema,
    CreateUserSchema,
    ResetCurrentUserPasswordSchema,
)
from monarch.utils.common import expect_schema


class UserDto:
    ns = Namespace("user", description="客户")


ns = UserDto.ns


@ns.route("")
class UserRescore(Resource):
    @ns.response(code=HTTPStatus.OK.value, description="成功")
    @ns.response(code=HTTPStatus.BAD_REQUEST.value, description="参数错误")
    @ns.doc("获取用户信息")
    def get(self):
        """获取用户信息"""
        return get_current_user_info()

    @ns.response(code=HTTPStatus.OK.value, description="成功")
    @ns.response(code=HTTPStatus.BAD_REQUEST.value, description="参数错误")
    @ns.doc("修改用户信息")
    @expect_schema(ns, UpdateCurrentUserInfoSchema())
    def put(self):
        """修改用户信息"""
        return update_current_user_info(g.data)


@ns.route("/login")
class UserLoginRescore(Resource):
    @ns.response(code=HTTPStatus.OK.value, description="成功")
    @ns.response(code=HTTPStatus.BAD_REQUEST.value, description="参数错误")
    @ns.doc("用户登录")
    @expect_schema(ns, UserLoginSchema())
    def post(self):
        """用户登录"""
        return login(g.data)


@ns.route("/register")
class UserRegisterRescore(Resource):
    @ns.response(code=HTTPStatus.OK.value, description="成功")
    @ns.response(code=HTTPStatus.BAD_REQUEST.value, description="参数错误")
    @ns.doc("用户注册")
    @expect_schema(ns, CreateUserSchema())
    def post(self):
        """用户注册"""
        return registered(g.data)


@ns.route("/logout")
class UserLogoutRescore(Resource):
    @ns.doc("用户退出登录")
    def post(self):
        """用户退出登录"""
        return logout()


@ns.route("/reset_password")
class ResetCurrentUserPasswordResource(Resource):
    @ns.response(code=HTTPStatus.OK.value, description="成功")
    @ns.response(code=HTTPStatus.BAD_REQUEST.value, description="参数错误")
    @ns.doc("用户重置密码")
    @expect_schema(ns, ResetCurrentUserPasswordSchema())
    def post(self):
        """用户重置密码"""
        return reset_current_user_password(g.data)


@ns.route("/logs/articles")
class GetArticlesLogsResource(Resource):
    @ns.doc("文章浏览记录")
    def get(self):
        return get_current_user_articles()


@ns.route("/logs/courses")
class GetCourseLogsResource(Resource):
    def get(self):
        return get_current_user_course()


@ns.route("/logs/<service_type>")
class GetUserServiceLogsResource(Resource):
    def get(self, service_type):
        return get_current_user_service_logs(service_type)
