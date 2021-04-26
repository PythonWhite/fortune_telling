#!/usr/bin/env python
# -*- coding: utf-8 -*-
from monarch.models.article import ArticleModel
from monarch.forms.admin.article import (
    CurrentArticleSchema,
)
from monarch.utils.api import Bizs, parse_pagination


def get_articles_likes_top5():
    query = ArticleModel.get_articles_likes_top5(is_books=False)
    data = CurrentArticleSchema().dump(query, many=True).data
    return Bizs.success(data)


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


def get_article(article_id):
    article = ArticleModel.get(article_id)
    if not article:
        return Bizs.fail("文章不存在")
    data = CurrentArticleSchema().dump(article).data
    return Bizs.success(data)


def like_article(article_id):
    article = ArticleModel.get(article_id)
    if not article:
        return Bizs.fail("文章不存在")
    article.update(likes=article.likes + 1)
    return Bizs.success()
