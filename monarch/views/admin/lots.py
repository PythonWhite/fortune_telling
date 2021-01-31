from flask import g
from flask_restplus import Resource, Namespace
from flask_restplus._http import HTTPStatus

from monarch.forms.admin.lots import (
    GetLotsTypeListSchema,
    CreateLotsTypeSchema,
)
from monarch.service.admin.lots import (
    create_lots_type,
    get_lots_type,
)
from monarch.utils.common import expect_schema


class LotsDto:
    ns = Namespace("lots", description="灵签")


ns = LotsDto.ns


@ns.route("/lotsType")
class LotsTypeResource(Resource):
    @ns.doc("获取灵签类型")
    @expect_schema(ns, GetLotsTypeListSchema())
    def get(self):
        """获取灵签类型"""
        return get_lots_type(g.data)
