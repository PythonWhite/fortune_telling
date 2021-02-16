#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import g

from flask_restplus import Resource, Namespace
from monarch.service.api.article import (
    get_articles_likes_top5,
    get_articles,
    get_article,
)
from monarch.forms.admin.article import (
    QueryArticleSchema,
)
from monarch.utils.common import expect_schema


class ArticleDto:
    ns = Namespace("article", description="文章")


ns = ArticleDto.ns


@ns.route("/top5")
class ArticleTOP5(Resource):
    def get(self):
        return get_articles_likes_top5()


@ns.route("/list")
class ArticlesResource(Resource):
    @expect_schema(ns, QueryArticleSchema())
    def get(self):
        return get_articles(g.data)


@ns.route("/<int:article_id>")
class ArticleResource(Resource):
    def get(self, article_id):
        return get_article(article_id)
