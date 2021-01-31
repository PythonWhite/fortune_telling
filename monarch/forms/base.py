#!/usr/bin/env python
# -*- coding: utf-8 -*-
from marshmallow import fields, Schema


class SearchSchema(Schema):
    keyword = fields.Str()
    queryField = fields.Str()


class PaginationSchema(Schema):
    page = fields.Int(allow_none=True)
    per_page = fields.Int(allow_none=True)
