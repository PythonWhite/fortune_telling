#!/usr/bin/env python
# -*- coding: utf-8 -*-
from monarch.models.lots import LotsType, Lots
from monarch.forms.admin.lots import CurrentLotsTypeSchema


def create_lots_type(data):
    name = data["name"]
    LotsType.create(name=name)
    return Bizs.success()


def get_lots_type(data):
    lots_type = LotsType.query_lots_type()
    result = CurrentLotsTypeSchema().dump(lots_type, many=True).data
    return Bizs.success(data=result)


def delete_lots_type(data):
    id = data["id"]
    lots_type = LotsType.get(id)
    if not lots_type:
        return Bizs.not_found()
    lots.deleted()
    return Bizs.success()


def edit_lots_type(data):
    pass


def create_lots(lots_type_id, data):
    pass


def get_lots(lots_type_id, data):
    pass


def edit_lots(lots_type_id, lots_id, data):
    pass


def delete_lots(lots_type_id, lots_id):
    pass



