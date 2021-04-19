#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import g

from monarch.models.video import CourseModel, ChapterModel
from monarch.corelibs.store import db
from monarch.forms.admin.course import (
    CoursesSchema,
    RetCourseSchema,
)
from monarch.utils.api import Bizs, parse_pagination
from monarch.utils import logger


def create_course(data):
    data["user_id"] = g.admin_user.id
    CourseModel.create(**data)
    return Bizs.success()


def update_course(course_id, data):
    course = CourseModel.get(course_id)
    if not course:
        return Bizs.fail(msg="课程不存在")
    course.update(**data)
    return Bizs.success()


def course_publication(course_id, data):
    course = CourseModel.get(course_id)
    if not course:
        return Bizs.fail(msg="课程不存在")
    course.update(is_publication=data["is_publication"])
    return Bizs.success()


def get_course(course_id):
    course = CourseModel.get(course_id)
    if not course:
        return Bizs.fail(msg="课程不存在")

    result = RetCourseSchema().dump(course).data
    return Bizs.success(result)


def query_course(data):
    keyword = data.get("keyword")
    field = data.get("field")
    sort = data.get("sort")
    sort_field = data.get("sort_field")
    type = data.get("type")
    is_publication = data.get("is_publication")
    query = CourseModel.query_course(keyword, field, sort, sort_field, type, is_publication)
    p_data = parse_pagination(query)
    result, pagination = p_data["result"], p_data["pagination"]
    result = CoursesSchema().dump(result, many=True).data
    return Bizs.success({
        "list": result,
        "pagination": pagination
    })


def add_chapter(course_id, data):
    course = CourseModel.get(course_id)
    if not course:
        return Bizs.fail(msg="课程不存在")

    data["course_id"] = course_id
    ChapterModel.create(**data)
    return Bizs.success()


def update_chapter(chapter_id, data):
    chapter = ChapterModel.get(chapter_id)
    if not chapter:
        return Bizs.fail(msg="章节不存在")
    chapter.update(**data)
    return Bizs.success()


def chapter_sort(chapter_id, data):
    chapter = ChapterModel.get(chapter_id)
    if not chapter:
        return Bizs.fail(msg="章节不存在")
    try:
        if chapter.pid != "0":
            pchapter = ChapterModel.get(chapter.pid)
            pchapter.update(nid=chapter.nid, _commit=False)
        if chapter.nid != "0":
            nchapter = ChapterModel.get(chapter.nid)
            nchapter.update(pid=chapter.pid, _commit=False)
        db.session.flush()
        if data["pid"] != "0":
            new_pchapter = ChapterModel.get(data["pid"])
            new_pchapter.update(nid=chapter.id, _commit=False)
        if data["nid"] != "0":
            new_nchapter = ChapterModel.get(data["nid"])
            new_nchapter.update(pid=chapter.id, _commit=False)
        chapter.update(_commit=False, **data)
        db.session.commit()
    except Exception as e:
        logger.error(e, exc_info=True)
        db.session.rollback()
        return Bizs.fail(msg="修改失败")
    return Bizs.success()


def delete_chapter(chapter_id):
    chapter = ChapterModel.get(chapter_id)
    if not chapter:
        return Bizs.fail(msg="章节不存在")
    if chapter.pid != "0":
        pchapter = ChapterModel.get(chapter.pid)
        pchapter.update(nid=chapter.nid, _commit=False)
    if chapter.nid != "0":
        nchapter = ChapterModel.get(chapter.nid)
        nchapter.update(pid=chapter.pid, _commit=False)
    chapter.delete(_commit=False)
    try:
        db.session.commit()
    except Exception as e:
        logger.error(e, exc_info=True)
        db.session.rollback()
        return Bizs.fail(msg="删除失败")
    return Bizs.success()
