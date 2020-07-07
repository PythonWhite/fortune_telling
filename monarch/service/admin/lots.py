#!/usr/bin/env python
# -*- coding: utf-8 -*-
from monarch.models.lots import LotsType, Lots


def create_lots_type(data):
    name = data["name"]
    LotsType.create(name=name)
    return Bizs.success()


def get_lots_type(data):
    pass


def delete_lots_type(data):
    pass


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



