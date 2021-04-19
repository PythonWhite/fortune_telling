#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shortuuid
from sqlalchemy import Column, Integer, String, Text, Index, DECIMAL, Boolean

from monarch.models.base import Base, TimestampMixin
from monarch.forms.admin.course import RetChapterSchema
from monarch.utils.model import escape_like


class CourseModel(Base, TimestampMixin):
    """课程"""

    __tablename__ = "course"

    __table_args__ = (
        Index("idx_title", "title"),
    )

    id = Column(String(32), primary_key=True, default=shortuuid.uuid, nullable=False)
    user_id = Column(String(32), nullable=False, comment="管理员ID")
    title = Column(String(255), nullable=False, comment="课程标题")
    introduction = Column(Text, nullable=False, comment="简介")
    cover = Column(String(255), nullable=False, comment="封面")
    author = Column(String(64), nullable=False, comment="作者")
    type = Column(Integer, nullable=False, default=1, comment="类型,1原创,2转载")
    likes = Column(Integer, nullable=False, default=0, comment="点赞数")
    is_publication = Column(Boolean, nullable=False, default=False, comment="是否发布")
    is_free = Column(Boolean, nullable=False, default=True, comment="是否免费")
    marked_price = Column(DECIMAL(6, 2), nullable=False, default=0, comment="标价")

    @classmethod
    def query_course(cls, keyword=None, field=None, sort=1, sort_field="likes", type=None, is_publication=None):
        query = cls.query
        if keyword and hasattr(cls, field):
            field = getattr(cls, field)
            query = query.filter(
                field.like("%" + escape_like(keyword) + "%")
            )
        if type:
            query = query.filter(
                cls.type == type
            )

        if is_publication is not None:
            query = query.filter(
                cls.is_publication == is_publication
            )
        if hasattr(cls, sort_field):
            sort_field = getattr(cls, sort_field)
            if sort == -1:
                sort = sort_field.desc()
            else:
                sort = sort_field
            query = query.order_by(sort)
        return query

    @property
    def chapters(self):
        result = ChapterModel.get_chapters_by_course_id(self.id)
        if result:
            result = ChapterModel.format_chapters_to_tree(result)
        return result or []


class ChapterModel(Base, TimestampMixin):
    """课程章节"""

    __tablename__ = "chapter"

    id = Column(String(32), primary_key=True, default=shortuuid.uuid, nullable=False)
    name = Column(String(64), nullable=False, comment="章节名称")
    course_id = Column(Integer, nullable=False, comment="课程ID")
    video_url = Column(String(255), nullable=True, comment="视频地址")
    pid = Column(String(32), nullable=False, default="0", comment="上一章节ID")
    nid = Column(String(32), nullable=False, default="0", comment="下一章节ID")
    parent = Column(String(32), nullable=False, default="0", comment="父章节ID")

    @classmethod
    def get_chapters_by_course_id(cls, course_id):
        query = cls.query.filter(
            cls.course_id == course_id
        ).all()
        return query

    @classmethod
    def sort(cls, data, datas):
        result = []
        temp = data.pop("0", None)
        while temp:
            temp["children"] = cls.sort(datas[temp["id"]["children"]], datas)
            result.append(temp)
            temp = data.pop(temp["id"], None)
        return result

    @classmethod
    def format_chapters_to_tree(cls, chapters):
        chapter_dicts = {}
        for chapter in chapters:
            schema_data = RetChapterSchema().dump(chapter).data
            data = chapter_dicts.setdefault(chapter.parent, {"children": {}})
            data["children"][chapter.pid] = schema_data
            chapter_dicts.get(chapter.id, {"children": {}}).update(**schema_data)

        return cls.sort(chapter_dicts.get("0", {}), chapter_dicts)
