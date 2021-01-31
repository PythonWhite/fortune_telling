from flask import g
from flask_restplus import Resource, Namespace
from flask_restplus._http import HTTPStatus

from monarch.forms.admin.user import (
    CreateUserSchema,
    UpdateUserSchema,
    UserLoginSchema,
    QueryUserSchema,
    UpdateCurrentUserInfoSchema,
    ResetCurrentUserPasswordSchema,
)
from monarch.service.admin.user import (
    get_a_captcha,
    user_login,
    user_logout,
    create_user,
    update_user,
    delete_user,
    get_user_menu_tree,
    get_current_user,
    get_current_user_info,
    update_current_user_info,
    reset_current_user_password,
)
from monarch.utils.common import expect_schema


class UserDto:
    ns = Namespace("user", description="用户接口")


ns = UserDto.ns


@ns.route("/captcha")
class Captcha(Resource):
    @ns.response(code=HTTPStatus.OK.value, description="成功")
    @ns.response(code=HTTPStatus.BAD_REQUEST.value, description="参数错误")
    @ns.doc("获取验证码")
    def get(self):
        """获取验证码"""
        return get_a_captcha()


@ns.route("/login")
class UserLogin(Resource):
    @ns.doc("用户登录")
    @expect_schema(ns, UserLoginSchema())
    def post(self):
        """用户登录"""
        return user_login(g.data)


@ns.route("/logout")
class UserLogout(Resource):
    @ns.doc("用户注销")
    def post(self):
        """用户注销"""
        return user_logout()


@ns.route("")
class UserList(Resource):
    @ns.response(code=HTTPStatus.OK.value, description="成功创建用户")
    @ns.response(code=HTTPStatus.NOT_FOUND.value, description="暂无用户")
    @ns.response(code=HTTPStatus.BAD_REQUEST.value, description="参数错误")
    @ns.doc("创建用户信息")
    @expect_schema(ns, CreateUserSchema())
    def post(self):
        """创建用户信息"""
        return create_user(g.data)


@ns.route("/<uid>")
@ns.param("uid", "用户唯一标识")
class User(Resource):
    @ns.response(code=HTTPStatus.OK.value, description="成功更新用户")
    @ns.response(code=HTTPStatus.NOT_FOUND.value, description="暂无用户")
    @ns.response(code=HTTPStatus.BAD_REQUEST.value, description="参数错误")
    @ns.doc("更新用户信息")
    @expect_schema(ns, UpdateUserSchema())
    def put(self, uid):
        """更新用户信息"""
        return update_user(uid, g.data)

    @ns.doc("删除用户")
    @ns.response(code=HTTPStatus.OK.value, description="成功删除用户")
    @ns.response(code=HTTPStatus.NOT_FOUND.value, description="暂无用户")
    def delete(self, uid):
        """删除用户"""
        return delete_user(uid)


@ns.route("/current")
class CurrentUser(Resource):
    @ns.doc("获取用户信息")
    def get(self):
        """获取用户信息"""
        return get_current_user()


@ns.route("/permissions")
class UserMenuTree(Resource):
    @ns.doc("获取用户菜单树")
    def get(self):
        """获取用户菜单树"""
        return get_user_menu_tree()


@ns.route("/current")
class CurrentUser(Resource):
    @ns.doc("获取用户信息")
    def get(self):
        """获取用户信息"""
        return get_current_user()


@ns.route("/current/info")
class CurrentUserInfo(Resource):
    @ns.doc("获取当前用户信息")
    def get(self):
        """获取当前用户信息"""
        return get_current_user_info()

    @ns.doc("修改当前用户信息")
    @expect_schema(ns, UpdateCurrentUserInfoSchema())
    def put(self):
        """修改当前用户信息"""
        return update_current_user_info(g.data)


@ns.route("/current/reset_password")
class ResetCurrentUserPassword(Resource):
    @ns.doc("重设当前用户密码")
    @expect_schema(ns, ResetCurrentUserPasswordSchema())
    def put(self):
        """重设当前用户密码"""
        return reset_current_user_password(g.data)
