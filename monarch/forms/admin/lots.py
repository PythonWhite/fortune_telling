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

    def get_created_at(self, obj):
        return datetime_to_timestamp(obj.created_at)


class GetLotsTypeListSchema(SearchSchema, PaginationSchema):
    pass


class CreateLotsTypeSchema(Schema):
    name = fields.Str(required=True)


class EditLotsTypeSchema(Schema):
    name = fields.Str(required=True)


class CreateLotsSchema(Schema):
    num = fields.Int(required=True, allow_none=False)
    name = fields.Str(required=True, allow_none=False)
    content = fields.Str(required=True, allow_none=False)
    solution = fields.Str(required=False)
    poetry = fields.Str(required=False)
    p_solution = fields.Str(required=False)
    meaning = fields.Str(required=False)


class CurrentLotsSchema(Schema):
    id = fields.Int()
    lots_type = fields.Int()
    num = fields.Int(required=True, allow_none=False)
    name = fields.Str(required=True, allow_none=False)
    content = fields.Str(required=True, allow_none=False)
    solution = fields.Str(required=False)
    poetry = fields.Str(required=False)
    p_solution = fields.Str(required=False)
    meaning = fields.Str(required=False)
    create_at = fields.Method("get_created_at")
    updated_at = fields.Method("get_updated_at")

    def get_created_at(self, obj):
        return datetime_to_timestamp(obj.created_at)

    def get_updated_at(self, obj):
        return datetime_to_timestamp(obj.updated_at)


class QueryLotsSchema(SearchSchema, PaginationSchema):
    pass


class EditLotsSchema(Schema):
    name = fields.Str(required=True, allow_none=False)
    content = fields.Str(required=True, allow_none=False)
    solution = fields.Str(required=False)
    poetry = fields.Str(required=False)
    p_solution = fields.Str(required=False)
    meaning = fields.Str(required=False)
