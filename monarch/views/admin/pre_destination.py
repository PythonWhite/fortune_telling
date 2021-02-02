#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import g
from flask_restplus import Resource, Namespace

from monarch.forms.admin.lots import (
    QueryNumerologySchema,
    CreateNumerologySchema,
    UpdateNumerologySchema,
)
from monarch.service.admin.pre_destination import (
    add_unmerology,
    get_numerology,
    query_numerology,
    update_numerology,
    delete_numerology,
)
from monarch.utils.common import expect_schema


class PreDestinationDto:
    ns = Namespace("pre_destination", description="")


ns = PreDestinationDto.ns


@ns.route("/numerology")
class NumerologysResource(Resource):
    @expect_schema(ns, QueryNumerologySchema())
    def get(self):
        return query_numerology(g.data)

    @expect_schema(ns, CreateNumerologySchema())
    def post(self):
        return add_unmerology(g.data)


@ns.route("/numerology/<int:numerology_id>")
class NumerologyResource(Resource):
    def get(self, numerology_id):
        return get_numerology(numerology_id)

    @expect_schema(ns, UpdateNumerologySchema())
    def put(self, numerology_id):
        return update_numerology(numerology_id, g.data)

    def delete(self, numerology_id):
        return delete_numerology(numerology_id)
