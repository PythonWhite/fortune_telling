from flask import Blueprint, request, g
from flask_restplus import Api

from monarch.utils.common import _check_user_login
from monarch.views.api.login import ns as captcha_ns
from monarch.views.api.user import ns as user_ns
from monarch.views.api.article import ns as article_ns
from monarch.views.api.lots import ns as lots_ns
from monarch.views.api.numerology import ns as numerology_ns
from monarch import config


NO_LOGIN_ROUTE = ["/", "/swagger.json", "/user/login", "/captcha", "/user/register"]
BLUEPRINT_URL_PREFIX = "/api/v1"


def login_before_request():
    if request.path.split(BLUEPRINT_URL_PREFIX)[-1] in NO_LOGIN_ROUTE:
        return

    token = request.headers.get("token")
    is_ok, resp = _check_user_login(token)
    if not is_ok:
        return resp

    g.user = resp


authorizations = {
    "apikey": {
        "type": "apikey",
        "in": "header",
        "name": "token"
    }
}


def register_api(app):
    blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
    api = Api(
        blueprint,
        title="New API",
        version="1.0",
        description="New API",
        doc=config.ENABLE_DOC,
        authorizations=authorizations,
        security="apikey"
    )

    api.add_namespace(captcha_ns, path="/captcha")
    api.add_namespace(user_ns, path="/user")
    api.add_namespace(article_ns, path="/article")
    api.add_namespace(lots_ns, path="/lots")
    api.add_namespace(numerology_ns, path="/numerology")

    blueprint.before_request(login_before_request)
    app.register_blueprint(blueprint)
