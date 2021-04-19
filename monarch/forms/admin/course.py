#!/usr/bin/env python
# -*- coding: utf-8 -*-
from marshmallow import fields, Schema
from monarch.forms.base import (
    SearchSchema,
    PaginationSchema,
)
from monarch.utils.date import datetime_to_timestamp


class CreateCourseSchema(Schema):
    title = fields.Str(required=True)
    introduction = fields.Str(required=True)
    cover = fields.Str(required=True)
    author = fields.Str(required=True)
    type = fields.Int(required=True)
    is_free = fields.Boolean(required=True)
    marked_price = fields.Float(required=True)


class UpdateCourseSchema(Schema):
    title = fields.Str(required=True)
    introduction = fields.Str(required=True)
    cover = fields.Str(required=True)
    author = fields.Str(required=True)
    type = fields.Int(required=True)
    is_free = fields.Boolean(required=True)
    marked_price = fields.Float(required=True)


class RetCourseSchema(Schema):
    id = fields.Str(required=True)
    title = fields.Str(required=True)
    introduction = fields.Str(required=True)
    cover = fields.Str(required=True)
    author = fields.Str(required=True)
    type = fields.Int(required=True)
    is_free = fields.Boolean(required=True)
    marked_price = fields.Float(required=True)
    chapters = fields.List(fields.Dict())


class CoursesSchema(Schema):
    id = fields.Str(required=True)
    title = fields.Str(required=True)
    introduction = fields.Str(required=True)
    cover = fields.Str(required=True)
    author = fields.Str(required=True)
    type = fields.Int(required=True)
    is_free = fields.Boolean(required=True)
    marked_price = fields.Float(required=True)
    updated_at = fields.Method("get_updated_at")

    def get_updated_at(self, obj):
        return datetime_to_timestamp(obj.updated_at)


class PublicationCourseSchema(Schema):
    is_publication = fields.Bool(required=True)


class QueryCourseSchema(PaginationSchema, SearchSchema):
    type = fields.Int()
    is_publication = fields.Int()


class AddChapterSchema(Schema):
    name = fields.Str(required=True)
    video_url = fields.Str(required=True)
    pid = fields.Str(required=True)
    nid = fields.Str(required=True)
    parent = fields.Str(required=True)


class UpdateChapterSchema(Schema):
    name = fields.Str(required=True)
    video_url = fields.Str(required=True)


class SortChapterSchema(Schema):
    pid = fields.Str(required=True)
    nid = fields.Str(required=True)
    parent = fields.Str(required=True)


class RetChapterSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)
    video_url = fields.Str(required=True)
    pid = fields.Str(required=True)
    nid = fields.Str(required=True)
    parent = fields.Str(required=True)
