from marshmallow import fields, Schema, validate
from marshmallow.validate import Length
from marshmallow.exceptions import ValidationError

from monarch.forms import PaginationSchema
from marshmallow.decorators import post_load
from monarch.utils.date import datetime_to_timestamp
from monarch.exc.consts import VERIFICATION_WAY


class UserLoginSchema(Schema):
    account = fields.Str(required=True, allow_none=False, validate=[Length(min=1, max=64)])
    password = fields.Str(required=True, allow_none=False, validate=[Length(min=1, max=64)])
    # captcha_value = fields.Str(required=True, allow_none=False)
    # captcha_id = fields.Str(required=True, allow_none=False)


class CreateUserSchema(Schema):
    account = fields.Str(required=True, allow_none=False, validate=[Length(min=1, max=64)])
    password = fields.Str(required=True, allow_none=False, validate=[Length(min=8, max=64)])


class RetCurrentUserSchema(Schema):
    id = fields.Str()
    account = fields.Str()
    nickname = fields.Str()
    avatar = fields.Str()
    phone = fields.Str()
    email = fields.Str()
    sex = fields.Int()


class UpdateCurrentUserInfoSchema(Schema):
    nickname = fields.Str(required=True, allow_none=False)
    avatar = fields.Str(required=True, allow_none=True)
    phone = fields.Str(required=True, allow_none=True)
    email = fields.Str(required=True, allow_none=True)
    sex = fields.Int(required=True, allow_none=False, validate=validate.Range(0, 2))


class ResetCurrentUserPasswordSchema(Schema):
    old_password = fields.Str(required=True, allow_none=False, validate=[Length(min=8, max=64)])
    password = fields.Str(required=True, allow_none=False, validate=[Length(min=8, max=64)])

class VerificationSchema(Schema):
    type = fields.Str(required=True, allow_none=False, validate=validate.OneOf(VERIFICATION_WAY))
    value = fields.Str(required=True, allow_none=False)


class ForgetPasswordSchema(Schema):
    code = fields.Str(required=True, allow_none=False)
    type = fields.Str(required=True, allow_none=False, validate=validate.OneOf(VERIFICATION_WAY))
    value = fields.Str(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False, validate=[Length(min=8, max=64)])
