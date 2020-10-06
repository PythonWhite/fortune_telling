#!/usr/bin/env python
# -*- coding: utf-8 -*-
from monarch.models.lots import (
    PreDestination,
    Numerology,
    Lots
)
from monarch.forms.admin.lots import (
    NumerologySchema
)
from monarch.utils.api import Bizs
from monarch.utils import logger


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
    result = NumerologySchema().dump(instance)
    return Bizs.success(reuslt)


def update_numerology(_id, data):
    instance = Numerology.get(_id)
    if not instance:
        return Bizs.fail("不存在")
    day_gan, hour_gan = data["day_gan"], data["hour_gan"]
    numero = Numerology.get_by_day_hour_gan(day_gan, hour_gan)
    if numero and numero.id != _id:
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

