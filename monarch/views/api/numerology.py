#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import g
from flask_restplus import Resource, Namespace

from monarch.service.api.numerology import numerology
from monarch.forms.api.numerology import QueryNumerologySchema
from monarch.utils.common import expect_schema


class NumerologyDto:
    ns = Namespace("numerology", description="")


ns = NumerologyDto.ns


@ns.route("")
class NumerologyResource(Resource):
    @ns.doc("查询命理前定数")
    @expect_schema(ns, QueryNumerologySchema())
    def post(self):
        return numerology(g.data)
