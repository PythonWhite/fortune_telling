#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import g
from flask_restplus import Resource, Namespace

from monarch.service.admin.article import (
    create_article,
    get_articles,
    update_article,
    get_article,
    delete_article,
)
from monarch.forms.admin.article import (
    CreateArticleSchema,
    QueryArticleSchema,
    UpdateArticleSchema,
)
from monarch.utils.common import expect_schema


class ArticleDto:
    ns = Namespace("article", description="文章")


ns = ArticleDto.ns


@ns.route("")
class ArticlesResource(Resource):
    @expect_schema(ns, QueryArticleSchema())
    def get(self):
        return get_articles(g.data)

    @expect_schema(ns, CreateArticleSchema())
    def post(self):
        return create_article(g.data)


@ns.route("/<int:article_id>")
class ArticleResource(Resource):
    def get(self, article_id):
        return get_article(article_id)

    @expect_schema(ns, UpdateArticleSchema())
    def put(self, article_id):
        return update_article(article_id, g.data)

    def delete(self, article_id):
        return delete_article(article_id)
