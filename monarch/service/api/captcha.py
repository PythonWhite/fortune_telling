#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64

from monarch.exc.consts import CACHE_USER_CAPTCHA_KEY, CACHE_FIVE_MINUTE
from monarch.utils.tool import random_text, gen_id, CustomImageCaptcha
from monarch.corelibs.mcredis import mc
from monarch.utils.api import Bizs


def get_captcha():
    text = random_text()
    image_uuid = gen_id()
    image_data = CustomImageCaptcha().generate(text)
    image_data_bs64 = base64.b64encode(image_data.getvalues()).decode("utf-8")
    data = {
        "b64s": "data:iamge/png;base64,{}".format(image_data_bs64),
        "id": image_uuid
    }
    key = CACHE_USER_CAPTCHA_KEY.format(image_uuid)
    mc.set(key, text, CACHE_FIVE_MINUTE)
    return Bizs.sucess(data)
