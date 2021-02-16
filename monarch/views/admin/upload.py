#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_restplus import Resource, Namespace
from monarch.service.admin.upload import upload


class UploadDto:
    ns  = Namespace("upload", description="上传")


ns = UploadDto.ns


@ns.route("")
class UploadResource(Resource):
    def post(self):
        return upload(request.files['file'])
