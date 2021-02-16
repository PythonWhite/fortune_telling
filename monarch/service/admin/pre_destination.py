#!/usr/bin/env python
# -*- coding: utf-8 -*-
from monarch.models.lots import (
    PreDestination,
    Numerology,
)
from monarch.forms.admin.lots import (
    NumerologySchema,
    CurrentPreDistinationSchema,
)
from monarch.utils.api import parse_pagination
from monarch.utils.api import Bizs


def add_unmerology(data):
    day_gan = data["day_gan"]
    hour_gan = data["hour_gan"]
    if Numerology.get_by_day_hour_gan(day_gan, hour_gan):
        return Bizs.fail(msg="已存在")
    Numerology.create(**data)
    return Bizs.success()


def get_numerology(_id):
    instance = Numerology.get(_id)
    if not instance:
        return Bizs.fail("不存在")
    result = NumerologySchema().dump(instance).data
    return Bizs.success(result)


def query_numerology(data):
    query = Numerology.query_numerology(data.get("keyword"), data.get("query_field"))
    p_data = parse_pagination(query)
    result, pagination = p_data["result"], p_data["pagination"]
    result = NumerologySchema().dump(result, many=True).data
    return Bizs.success({
        "list": result,
        "pagination": pagination
    })


def update_numerology(_id, data):
    instance = Numerology.get(_id)
    if not instance:
        return Bizs.fail("不存在")
    day_gan, hour_gan = data["day_gan"], data["hour_gan"]
    numero = Numerology.get_by_day_hour_gan(day_gan, hour_gan, bans_id=instance.id)
    if numero:
        return Bizs.fail("已存在")
    instance.update(**data)
    return Bizs.success()


def delete_numerology(_id):
    instance = Numerology.get(_id)
    if not instance:
        return Bizs.fail(msg="不存在")
    if not instance.delete_numerology():
        return Bizs.fail(msg="删除失败")
    return Bizs.success()


def query_pre_destination(numerology_id):
    query = PreDestination.query_by_numerology_id(numerology_id)
    result = CurrentPreDistinationSchema().dump(query.all(), many=True).data
    return Bizs.success(result)


def create_pre_destination(numerology_id, data):
    instance = Numerology.get(numerology_id)
    if not instance:
        return Bizs.fail(msg="不存在")
    if PreDestination.get_by_numerology_id_and_hour_gz(numerology_id, data["hour_gz"]):
        return Bizs.fail(msg="已存在相同时干支的数据")
    data["numerology_id"] = numerology_id
    PreDestination.create(**data)
    return Bizs.success()


def delete_pre_destination(pre_destination):
    pre_destination = PreDestination.get(pre_destination)
    if not pre_destination:
        return Bizs.fail(msg="资源不存在")
    pre_destination.delete(_hard=True)
    return Bizs.success()


def edit_pre_destination(pre_destination_id, data):
    pre_destination = PreDestination.get(pre_destination_id)
    if not pre_destination:
        return Bizs.fail(msg="资源不存在")
    if PreDestination.get_by_numerology_id_and_hour_gz(
        pre_destination.numerology_id, data["hour_gz"], pre_destination.id
    ):
        return Bizs.fail(msg="已存在相同时干支的数据")
    pre_destination.update(**data)
    return Bizs.success()
