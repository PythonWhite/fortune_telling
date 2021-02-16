#!/usr/bin/env python
# -*- coding: utf-8 -*-
from marshmallow import fields, Schema
from monarch.forms.base import (
    SearchSchema,
    PaginationSchema,
)
from monarch.utils.date import datetime_to_timestamp


class CreateArticleSchema(Schema):
    title = fields.Str(required=True)
    introduction = fields.Str(required=True)
    content = fields.Str(required=True)
    cover = fields.Str(required=True)
    author = fields.Str(required=True)


class QueryArticleSchema(SearchSchema, PaginationSchema):
    type = fields.Int()


class CurrentArticleSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    introduction = fields.Str()
    content = fields.Str()
    cover = fields.Str()
    author = fields.Str()
    type = fields.Int()
    created_at = fields.Method("get_created_at")
    updated_at = fields.Method("get_updated_at")

    def get_created_at(self, obj):
        return datetime_to_timestamp(obj.created_at)

    def get_updated_at(self, obj):
        return datetime_to_timestamp(obj.updated_at)


class UpdateArticleSchema(Schema):
    title = fields.Str(required=True)
    introduction = fields.Str(required=True)
    content = fields.Str(required=True)
    cover = fields.Str(required=True)
    author = fields.Str(required=True)
