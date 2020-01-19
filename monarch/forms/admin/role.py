# -*- coding: utf-8 -*-
from marshmallow import fields, Schema
from marshmallow.validate import Length
from monarch.forms import PaginationSchema


class QueryRoleSchema(PaginationSchema):
    pass


class CreateRoleSchema(Schema):
    name = fields.Str(required=True, allow_none=False, validate=[Length(min=1, max=64)])
    description = fields.Str(required=True, allow_none=False, validate=[Length(max=500)])
    permission = fields.List(fields.Int, required=True)


class UpdateRoleSchema(Schema):
    name = fields.Str(required=True, allow_none=False, validate=[Length(min=1, max=64)])
    description = fields.Str(required=True, allow_none=False, validate=[Length(max=500)])
    permission = fields.List(fields.Int, required=True)


class RetQueryRoleSchma(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    permission = fields.List(fields.Int)