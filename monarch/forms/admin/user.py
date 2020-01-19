from flask import g
from marshmallow import fields, Schema
from marshmallow.validate import Length
from marshmallow.exceptions import ValidationError

from monarch.forms import PaginationSchema, SearchSchema
from marshmallow.decorators import post_load
from monarch.utils.date import datetime_to_timestamp


class CaptchaSchema(Schema):
    t = fields.Str(required=True, allow_none=False)


class UserLoginSchema(Schema):
    account = fields.Str(required=True, allow_none=False, validate=[Length(min=1, max=64)])
    password = fields.Str(required=True, allow_none=False, validate=[Length(min=1, max=64)])
    t = fields.Str(required=True, allow_none=False)
    code = fields.Str(required=True, allow_none=False)


class CreateUserSchema(Schema):
    account = fields.Str(required=True, allow_none=False, validate=[Length(min=1, max=64)])
    name = fields.Str(required=True, allow_none=False, validate=[Length(min=1, max=64)])
    password = fields.Str(required=True, allow_none=False, validate=[Length(min=8, max=64)])
    deleted = fields.Boolean(required=True, allow_none=False)
    permissions = fields.List(fields.Int, required=True)


class UpdateUserSchema(Schema):
    name = fields.Str(required=True, allow_none=False, validate=[Length(min=1, max=64)])
    password = fields.Str(validate=[Length(min=8, max=64)])
    deleted = fields.Boolean(required=True, allow_none=False)
    permissions = fields.List(fields.Int, required=True)


class QueryAdminUserSchema(PaginationSchema):
    role_id = fields.Int()
    deleted = fields.Boolean()


class RetCurrentUserSchema(Schema):
    id = fields.Str()
    account = fields.Str()
    name = fields.Str()
    avatar = fields.Str()
    deleted = fields.Boolean()
    phone = fields.Str()
    email = fields.Str()


class UpdateCurrentUserInfoSchema(Schema):
    name = fields.Str(required=True, allow_none=False)
    avatar = fields.Str(required=True, allow_none=True)
    phone = fields.Str(required=True, allow_none=True)
    email = fields.Str(required=True, allow_none=True)


class ResetCurrentUserPasswordSchema(Schema):
    old_password = fields.Str(required=True, allow_none=False, validate=[Length(min=8, max=64)])
    password = fields.Str(required=True, allow_none=False, validate=[Length(min=8, max=64)])


class QueryUserSchema(PaginationSchema, SearchSchema):
    pass