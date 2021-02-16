#!/usr/bin/env python
# -*- coding: utf-8 -*-
from monarch.models.lots import LotsType, Lots
from monarch.forms.admin.lots import (
    CurrentLotsTypeSchema,
    CurrentLotsSchema,
)
from monarch.utils.api import Bizs, parse_pagination



def get_lots_type():
    lots_type = LotsType.query_lots_type()
    lots_type = [item for item in lots_type if item.lots_nums != 0]
    result = CurrentLotsTypeSchema().dump(lots_type, many=True).data
    return Bizs.success(data=result)


def drawLots(typeID):
    lots = Lots.random_gen_lot(typeID)
    data = CurrentLotsSchema().dump(lots).data
    return Bizs.success(data)


def get_lots(lotsID):
    lot = Lots.get(lotsID)
    if not lot:
        return Bizs.not_found()
    result = CurrentLotsSchema().dump(lot, many=False).data
    return Bizs.success(result)
