#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_restplus import Resource, Namespace
from flask_restplus._http import HTTPStatus

from monarch.service.api.captcha import get_captcha


class CaptchaDto:
    ns = Namespace("captcha", description="验证码")


ns = CaptchaDto.ns


@ns.route("")
class CaptchaRescore(Resource):
    @ns.response(code=HTTPStatus.OK.value, description="成功")
    @ns.response(code=HTTPStatus.BAD_REQUEST.value, description="参数错误")
    @ns.doc("获取验证码")
    def get(self):
        """获取验证码"""
        return get_captcha()
