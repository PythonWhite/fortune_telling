from monarch import config
from flask import Blueprint, request, g
from flask_restplus import Api
from monarch.utils.common import _check_admin_user_login
from monarch.views.admin.user import ns as user_ns
from monarch.views.admin.lots import ns as lots_ns
from monarch.views.admin.pre_destination import ns as pre_destination_ns
from monarch.views.admin.upload import ns as upload_ns
from monarch.views.admin.article import ns as article_ns
from monarch.views.admin.course import ns as course_ns


NO_LOGIN_ROUTE = ["/user/login", "/user/captcha", "/", "/swagger.json"]
BLUEPRINT_URL_PREFIX = "/admin/v1"


def login_before_request():
    if request.path.split(BLUEPRINT_URL_PREFIX)[-1] in NO_LOGIN_ROUTE:
        return

    token = request.headers.get("token")
    is_ok, resp = _check_admin_user_login(token)
    if not is_ok:
        return resp

    g.admin_user = resp


authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'token'
    }
}


def register_admin_api(app):
    blueprint = Blueprint("admin", __name__, url_prefix=BLUEPRINT_URL_PREFIX)
    api = Api(
        blueprint,
        title="后台管理",
        version="1.0",
        description="后台管理",
        doc=config.ENABLE_DOC,
        authorizations=authorizations,
        security='apikey'
    )
    api.add_namespace(user_ns, path="/user")
    api.add_namespace(lots_ns, path="/lots")
    api.add_namespace(pre_destination_ns, path="/pre_destination")
    api.add_namespace(upload_ns, path="/upload")
    api.add_namespace(article_ns, path="/article")
    api.add_namespace(course_ns, path="/course")
    blueprint.before_request(login_before_request)
    app.register_blueprint(blueprint)
