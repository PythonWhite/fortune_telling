from flask import g

from flask_restplus import Resource, Namespace
from monarch.service.api.course import (
    get_courses_likes_top5,
    get_courses,
    get_course,
)
from monarch.forms.admin.course import (
    QueryCourseSchema,
)
from monarch.utils.common import expect_schema


class CourseDto:
    ns = Namespace("course", description="课程")


ns = CourseDto.ns


@ns.route("/top5")
class CourseTop5(Resource):
    def get(self):
        return get_courses_likes_top5()


@ns.route("/list")
class CoursesResource(Resource):
    @expect_schema(ns, QueryCourseSchema())
    def get(self):
        return get_courses(g.data)


@ns.route("/<course_id>")
class CourseResource(Resource):
    def get(self, course_id):
        return get_course(course_id)
