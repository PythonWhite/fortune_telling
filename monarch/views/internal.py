from __future__ import absolute_import

from flask import Blueprint
from monarch.tasks.form_id import print_sth

bp = Blueprint("api_internal", __name__, url_prefix="/_internal")


@bp.route("/ping")
def ping():
    """用来提供可达性检测的接口，无实际意义"""
    print_sth.delay()
    return "pong"
