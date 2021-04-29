#!/usr/bin/env python
# -*- coding: utf-8 -*-
from monarch.exc.consts import ARABIC_TO_CN_NUM_MAP


def num_cn(num: int):
    return "".join([ARABIC_TO_CN_NUM_MAP[i] for i in str(num)])
