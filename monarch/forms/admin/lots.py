#!/usr/bin/env python
# -*- coding: utf-8 -*-
from marshmallow import fields, Schema


class CurrentLotsTypeSchema(Schema):
    id = fields.Int()
    name = fields.Str()
