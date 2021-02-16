#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import g

from monarch.models.article import ArticleModel
from monarch.forms.admin.article import (
    CurrentArticleSchema,
)
from monarch.utils.api import Bizs, parse_pagination


def create_article(data):
    title = data["title"]
    if ArticleModel.get_article(title, is_books=False):
        return Bizs.fail(msg="标题已存在")
    data["user_id"] = g.admin_user.id
    ArticleModel.create(**data)
    return Bizs.success()


def get_articles(data):
    keyword = data.get("keyword")
    query_field = data.get("query_field")
    _type = data.get("type", 0)
    query = ArticleModel.query_article(keyword, query_field, _type)
    p_data = parse_pagination(query)
    result, pagination = p_data["result"], p_data["pagination"]
    result = CurrentArticleSchema().dump(result, many=True).data
    return Bizs.success({
        "list": result,
        "pagination": pagination
    })


def update_article(article_id, data):
    article = ArticleModel.get(article_id)
    if not article:
        return Bizs.fail("文章不存在")
    title = data["title"]
    if ArticleModel.get_article(title, is_books=False, bans_id=article.id):
        return Bizs.fail(msg="标题已存在")
    article.update(**data)
    return Bizs.success()


def get_article(article_id):
    article = ArticleModel.get(article_id)
    if not article:
        return Bizs.fail("文章不存在")
    data = CurrentArticleSchema().dump(article).data
    return Bizs.success(data)


def delete_article(article_id):
    article = ArticleModel.get(article_id)
    if not article:
        return Bizs.fail("文章不存在")
    article.delete(_hard=True)
    return Bizs.success()
