#!/usr/bin/env python
# -*- coding: utf-8 -*-
from marshmallow import fields, Schema


class QueryNumerologySchema(Schema):
    datatype = fields.Str(required=True)
    year = fields.Int(required=True)
    month = fields.Int(required=True)
    day = fields.Int(required=True)
    hour = fields.Int(required=True)
    minute = fields.Int(required=True)
    second = fields.Int(required=True)
    is_leap = fields.Bool(required=True)
