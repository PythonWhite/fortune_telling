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
    cover = fields.Str()
    introduction = fields.Str()
    lots_nums = fields.Int()
    create_at = fields.Method("get_created_at")

    def get_created_at(self, obj):
        return datetime_to_timestamp(obj.created_at)


class GetLotsTypeListSchema(SearchSchema, PaginationSchema):
    pass


class CreateLotsTypeSchema(Schema):
    name = fields.Str(required=True)
    cover = fields.Str()
    introduction = fields.Str()


class EditLotsTypeSchema(Schema):
    name = fields.Str(required=True)
    cover = fields.Str()
    introduction = fields.Str()


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


class NumerologySchema(Schema):
    id = fields.Int()
    day_gan = fields.Str()
    hour_gan = fields.Str()
    hexagram_name = fields.Str()
    fate_name = fields.Str()
    fate_desc = fields.Str()
    fate_poetry = fields.Str()
    detail = fields.Dict()
    star_desc = fields.Str()


class CreateNumerologySchema(Schema):
    day_gan = fields.Str(required=True)
    hour_gan = fields.Str(required=True)
    hexagram_name = fields.Str(required=True)
    fate_name = fields.Str(required=True)
    fate_desc = fields.Str(required=True)
    fate_poetry = fields.Str(required=True)
    detail = fields.Str(required=True)
    star_desc = fields.Str(required=True)


class UpdateNumerologySchema(Schema):
    day_gan = fields.Str(required=True)
    hour_gan = fields.Str(required=True)
    hexagram_name = fields.Str(required=True)
    fate_name = fields.Str(required=True)
    fate_desc = fields.Str(required=True)
    fate_poetry = fields.Str(required=True)
    detail = fields.Str(required=True)
    star_desc = fields.Str(required=True)


class QueryNumerologySchema(SearchSchema, PaginationSchema):
    pass


class CurrentPreDistinationSchema(Schema):
    id = fields.Int()
    hour_gz = fields.Str()
    numerology_id = fields.Int()
    name = fields.Str()


class CreatePreDestinationSchema(Schema):
    hour_gz = fields.Str(required=True)
    name = fields.Str(required=True)
