#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_restplus import Resource, Namespace

from monarch.service.api.lots import (
    get_lots_type,
    drawLots,
    get_lots,
)


class LotsDto:
    ns = Namespace("lots", description="灵签")


ns = LotsDto.ns


@ns.route("/types")
class LotsTypeListResource(Resource):
    def get(self):
        return get_lots_type()


@ns.route("/draw/<int:typeID>")
class DrawLots(Resource):
    def get(self, typeID):
        return drawLots(typeID)


@ns.route("/<int:lotsID>")
class LotsResource(Resource):
    def get(self, lotsID):
        return get_lots(lotsID)
