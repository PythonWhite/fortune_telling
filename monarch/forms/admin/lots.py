#!/usr/bin/env python
# -*- coding: utf-8 -*-
from marshmallow import fields, Schema
from monarch.forms.base import (
    SearchSchema,
    PaginationSchema,
)
from monarch.utils.date import datetime_to_timestamp

class CurrentLotsTypeSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    lots_nums = fields.Int()
    create_at = fields.Method("get_created_at")

    def get_create_at(self, obj):
        return datetime_to_timestamp(obj.created_at)


class GetLotsTypeListSchema(SearchSchema, PaginationSchema):
    pass


class CreateLotsTypeSchema(Schema):
    pass
