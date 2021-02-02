from flask import g
from flask_restplus import Resource, Namespace

from monarch.forms.admin.lots import (
    GetLotsTypeListSchema,
    CreateLotsTypeSchema,
    EditLotsTypeSchema,
    CreateLotsSchema,
    QueryLotsSchema,
    EditLotsSchema,
)
from monarch.service.admin.lots import (
    create_lots_type,
    get_lots_type,
    edit_lots_type,
    delete_lots_type,
    create_lots,
    query_lots,
    edit_lots,
    delete_lots,
    get_lots,
)
from monarch.utils.common import expect_schema


class LotsDto:
    ns = Namespace("lots", description="灵签")


ns = LotsDto.ns


@ns.route("/lotsType")
class LotsTypeListResource(Resource):
    @expect_schema(ns, GetLotsTypeListSchema())
    def get(self):
        return get_lots_type(g.data)

    @expect_schema(ns, CreateLotsTypeSchema())
    def post(self):
        return create_lots_type(g.data)


@ns.route("/lotsType/<int:lotsTypeID>")
class LotsTypeResource(Resource):
    @expect_schema(ns, EditLotsTypeSchema())
    def put(self, lotsTypeID):
        return edit_lots_type(lotsTypeID, g.data)

    def delete(self, lotsTypeID):
        return delete_lots_type(lotsTypeID)


@ns.route("/<int:lotsTypeID>")
class QueryLotsResource(Resource):
    @expect_schema(ns, QueryLotsSchema())
    def get(self, lotsTypeID):
        return query_lots(lotsTypeID, g.data)

    @expect_schema(ns, CreateLotsSchema())
    def post(self, lotsTypeID):
        return create_lots(lotsTypeID, g.data)


@ns.route("/lots/<int:lotsID>")
class LotsResource(Resource):
    def get(self, lotsID):
        return get_lots(lotsID)

    @expect_schema(ns, EditLotsSchema())
    def put(self, lotsID):
        return edit_lots(lotsID, g.data)

    def delete(self, lotsID):
        return delete_lots(lotsID)
