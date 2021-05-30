#!/usr/bin/env python
# -*- coding: utf-8 -*-
from monarch.external.lunar_datetime import LunarDatetime, DayException
from monarch.models.lots import Numerology, PreDestination
from monarch.forms.admin.lots import NumerologySchema
from monarch.utils import logger
from monarch.utils.api import Bizs


def numerology(data):
    lunardatetime = None
    try:
        if data["datatype"] == "lunar":
            lunardatetime = LunarDatetime.create_by_lunar_day(
                lunarYear=data["year"],
                lunarMonth=data["month"],
                lunarDay=data["day"],
                hour=data["hour"],
                minute=data["minute"],
                second=data["second"],
                is_leapMonth=data["is_leap"]
            )
        else:
            lunardatetime = LunarDatetime.create_by_solar_day(
                solarYear=data["year"],
                solarMonth=data["month"],
                solarDay=data["day"],
                hour=data["hour"],
                minute=data["minute"],
                second=data["second"],
            )
    except DayException:
        return Bizs.fail(msg="时间错误")
    logger.info("八字:日干{},时干{},时之{}".format(lunardatetime.dayGan, lunardatetime.hourGan, lunardatetime.hourZhi))
    numerology = Numerology.get_by_day_hour_gan(lunardatetime.dayGan, lunardatetime.hourGan)
    if not numerology:
        return Bizs.fail(msg="没有找到相关命理前定数")
    pre_destination = PreDestination.get_by_numerology_id_and_hour_gz(numerology.id, lunardatetime.hourZhi)
    if not pre_destination:
        return Bizs.fail(msg="没有找到相关命理前定数")
    result = NumerologySchema().dump(numerology)
    result["pre_destination_id"] = pre_destination.id
    result["star_name"] = pre_destination.name
    result["hour_zhi"] = pre_destination.hour_gz
    result["star_poetry"] = pre_destination.star_poetry
    return Bizs.success(result)
