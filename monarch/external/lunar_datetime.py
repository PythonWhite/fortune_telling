#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sxtwl
import datetime

from monarch.exc.consts import (
    GAN,
    ZHI,
    ZODIAC,
    MONTH_CN,
    DAY_CN,
    LUNAR_DAY_STR,
    STARTING_YEAR,
    DAY_GZ_STR,
)
from monarch.utils.cn import num_cn


Lunar = sxtwl.Lunar()


class DayException(Exception):
    pass


class LunarDatetime(object):
    def __init__(self, datetime):
        self.solarDatetime = datetime
        self.lunarDay = Lunar.getDayBySolar(datetime.year, datetime.month, datetime.day)
        self.hourGZ = Lunar.getShiGz(self.lunarDay.Lday2.tg, datetime.hour)

    @property
    def yearGan(self):
        return GAN[self.lunarDay.Lyear2.tg]

    @property
    def zodiac(self):
        return ZODIAC[self.lunarDay.Lyear2.dz]

    @property
    def yearZhi(self):
        return ZHI[self.lunarDay.Lyear2.dz]

    @property
    def monthGan(self):
        return GAN[self.lunarDay.Lmonth2.tg]

    @property
    def monthZhi(self):
        return ZHI[self.lunarDay.Lmonth2.dz]

    @property
    def dayGan(self):
        return GAN[self.lunarDay.Lday2.tg]

    @property
    def dayZhi(self):
        return ZHI(self.lunarDay.Lday2.dz)

    @property
    def hourGan(self):
        return GAN[self.hourGZ.tg]

    @property
    def hourZhi(self):
        return ZHI[self.hourGZ.dz]

    @property
    def lunarYear(self):
        return DAY_GZ_STR.format(self.yearGan, self.yearZhi, self.monthGan, self.monthZhi, self.dayGan, self.dayZhi)

    @property
    def lunar_str(self):
        return LUNAR_DAY_STR.format(
            num_cn(self.lunarDay.Lyear + STARTING_YEAR), "闰" if self.lunarDay.Lleap else "",
            MONTH_CN[self.lunarDay.Lmc], DAY_CN[self.lunarDay.Ldi]
        )

    @classmethod
    def create_by_lunar_day(
            cls, lunarYear: int, lunarMonth: int, lunarDay: int, hour: int,
            minute: int, second: int, is_leapMonth: bool = False
    ):
        try:
            day = Lunar.getDayByLunar(lunarYear, lunarMonth, lunarDay)
        except sxtwl.LunarException:
            raise DayException("农历日期错误")

        dt = datetime.datetime(day.y, day.m, day.d, hour, minute, second)
        return cls(dt)

    @classmethod
    def create_by_solar_day(
            cls, solarYear: int, solarMonth: int, solarDay: int, hour: int,
            minute: int, second: int
    ):
        try:
            dt = datetime.datetime(solarYear, solarMonth, solarDay, hour, minute, second)
        except Exception:
            raise DayException("阳历日期错误")

        return cls(dt)
