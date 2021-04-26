#!/usr/bin/env python
# -*- coding: utf-8 -*-
from monarch.models.video import CourseModel
from monarch.forms.admin.course import CoursesSchema, RetCourseSchema
from monarch.utils.api import Bizs, parse_pagination
from monarch.utils.common import user_browse_log


def get_courses_likes_top5():
    query = CourseModel.get_courses_likes_top5()
    data = CoursesSchema().dump(query, many=True).data
    return Bizs.success(data)


def get_courses(data):
    keyword = data.get("keyword")
    query_field = data.get("query_field")
    _type = data.get("type", 0)
    query = CourseModel.query_course(keyword, query_field, _type)
    p_data = parse_pagination(query)
    result, pagination = p_data["result"], p_data["pagination"]
    result = CoursesSchema().dump(result, many=True).data
    return Bizs.success({
        "list": result,
        "pagination": pagination
    })


@user_browse_log(CourseModel)
def get_course(course_id):
    course = CourseModel.get(course_id)
    if not course:
        return Bizs.fail(msg="课程不存在")
    data = RetCourseSchema().dump(course).data
    return Bizs.success(data)


def like_course(course_id):
    course = CourseModel.get(course_id)
    if not course:
        return Bizs.fail(msg="课程不存在")
    course.update(likes=course.likes + 1)
    return Bizs.success()
