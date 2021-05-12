#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import g
from monarch.models.lots import LotsType, Lots
from monarch.models.service import ServiceLog
from monarch.forms.admin.lots import (
    CurrentLotsTypeSchema,
    CurrentLotsSchema,
)
from monarch.utils.api import Bizs


def get_lots_type():
    lots_type = LotsType.query_lots_type()
    lots_type = [item for item in lots_type if item.lots_nums != 0]
    result = CurrentLotsTypeSchema().dump(lots_type, many=True).data
    return Bizs.success(data=result)


def drawLots(typeID):
    lots = Lots.random_gen_lot(typeID)
    data = CurrentLotsSchema().dump(lots).data
    ServiceLog.create_by_lots(g.user.id, data)
    return Bizs.success(data)


def get_lots(lotsID):
    lot = Lots.get(lotsID)
    if not lot:
        return Bizs.not_found()
    result = CurrentLotsSchema().dump(lot, many=False).data
    return Bizs.success(result)
