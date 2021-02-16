#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import uuid
from monarch.utils.api import Bizs
from monarch.config import UPLOAD_FOLDER, STATIC_URL_PATH, DOMAIN


def upload(fileHandler):
    suffix = fileHandler.filename.split(".")[-1]
    fileName = uuid.uuid4().hex + "." + suffix
    file_path = DOMAIN + STATIC_URL_PATH + "/" + fileName
    fileHandler.save(os.path.join(UPLOAD_FOLDER, fileName))
    return Bizs.success({
        "url": file_path
    })

