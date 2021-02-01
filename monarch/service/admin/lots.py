#!/usr/bin/env python
# -*- coding: utf-8 -*-
from monarch.models.lots import LotsType, Lots
from monarch.forms.admin.lots import (
    CurrentLotsTypeSchema,
    CurrentLotsSchema,
)
from monarch.utils.api import Bizs, parse_pagination


def create_lots_type(data):
    name = data["name"]
    LotsType.create(name=name)
    return Bizs.success()


def get_lots_type(data):
    lots_type = LotsType.query_lots_type()
    result = CurrentLotsTypeSchema().dump(lots_type, many=True).data
    return Bizs.success(data=result)


def delete_lots_type(lotsTypeID):
    lots_type = LotsType.get(lotsTypeID)
    if not lots_type:
        return Bizs.not_found()
    lots.deleted()
    return Bizs.success()


def edit_lots_type(lotsTypeID, data):
    lots_type = LotsType.get(lotsTypeID)
    if not lots_type:
        return Bizs.not_found()
    lots_type.update(name=data["name"])
    return Bizs.success()


def create_lots(lots_type_id, data):
    lots_type = LotsType.get(lots_type_id)
    if not lots_type:
        return Bizs.not_found()
    if Lots.exist_num(data["num"], lots_type.id):
        return Bizs.fail(msg="已存在相同的数据")
    data["lot_type"] = lots_type.id
    Lots.create(**data)
    return Bizs.success()


def query_lots(lots_type_id, data):
    lots_type = LotsType.get(lots_type_id)
    if not lots_type:
        return Bizs.not_found()
    query = Lots.query_lots_by_type(
        lots_type.id, data.get("keyword"), data.get("query_field"), data.get("sort"), data.get("sort_field")
    )
    p_data = parse_pagination(query)
    result, pagination = p_data["result"], p_data["pagination"]
    result = CurrentLotsSchema().dump(result, many=True).data
    return Bizs.success({
        "list": result,
        "pagination": pagination
    })


def edit_lots(lots_id, data):
    lot = Lots.get(lots_id)
    if not lot:
        return Bizs.not_found()
    lot.update(**data)
    return Bizs.success()


def delete_lots(lots_id):
    lot = Lots.get(lots_id)
    if not lot:
        return Bizs.not_found()
    lot.delete(_hard=True)
    return Bizs.success()


def get_lots(self, lotsID):
    lot = Lots.get(lotsID)
    if not lot:
        return Bizs.not_found()
    result = CurrentLotsSchema().dump(lot, many=False).data
    return Bizs.success(result)
