#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request

from monarch.utils import logger


def get_ip():
    real_ip = request.headers.get("X-Real-Ip", "")
    forward_ip = request.headers.get("X-Forwarded-For", "").split(",")[0]
    ori_forward_ip = request.headers.get("X-Original-Forwarded-For", "").split(",")[0]
    ip = ori_forward_ip or forward_ip or real_ip
    logger.info("真实ip --> {}".format(ip))
    return ip

