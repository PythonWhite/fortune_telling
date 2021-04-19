#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import g
from flask_restplus import Resource, Namespace

from monarch.service.admin.course import (
    create_course,
    update_course,
    course_publication,
    get_course,
    query_course,
    add_chapter,
    update_chapter,
    chapter_sort,
    delete_chapter,
)
from monarch.forms.admin.course import (
    CreateCourseSchema,
    UpdateCourseSchema,
    QueryCourseSchema,
    AddChapterSchema,
    UpdateChapterSchema,
    SortChapterSchema,
    PublicationCourseSchema,
)
from monarch.utils.common import expect_schema


class CourseDto:
    ns = Namespace("course", description="课程")


ns = CourseDto.ns


@ns.route("/list")
class QueryCourseResource(Resource):
    @expect_schema(ns, QueryCourseSchema())
    def get(self):
        return query_course(g.data)


@ns.route("/create")
class CreateCourseResource(Resource):
    @expect_schema(ns, CreateCourseSchema())
    def post(self):
        return create_course(g.data)


@ns.route("/<course_id>")
class CourseResource(Resource):
    def get(self, course_id):
        return get_course(course_id)

    @expect_schema(ns, UpdateCourseSchema())
    def put(self, course_id):
        return update_course(course_id, g.data)


@ns.route("/<course_id>/publication")
class Publication(Resource):
    @expect_schema(ns, PublicationCourseSchema())
    def post(self, course_id):
        return course_publication(course_id, g.data)


@ns.route("/<course_id>/chapter/add")
class AddChapterResource(Resource):
    @expect_schema(ns, AddChapterSchema())
    def post(self, course_id):
        return add_chapter(course_id, g.data)


@ns.route("/chapter/<chapter_id>")
class ChapterResource(Resource):
    @expect_schema(ns, UpdateChapterSchema())
    def put(self, chapter_id):
        return update_chapter(chapter_id, g.data)

    def delete(self, chapter_id):
        return delete_chapter(chapter_id)


@ns.route("/chapter/<chapter_id>/sort")
class SortChapterResource(Resource):
    @expect_schema(ns, SortChapterSchema())
    def post(self, chapter_id):
        return chapter_sort(chapter_id, g.data)
