import datetime

DEBUG = (False,)
ENABLE_DOC = "/"
SECRET_KEY = ""

UPLOAD_FOLDER = "monarch/static"
STATIC_URL_PATH = "/static"
DOMAIN = "http://127.0.0.1:5000"

# SQLALCHEMY 配置
SQLALCHEMY_DATABASE_URI = (
    "mysql+pymysql://root:root@127.0.0.1:3306/monarch?charset=utf8mb4"
)
SQLALCHEMY_POOL_SIZE = 100
SQLALCHEMY_MAX_OVERFLOW = 500
SQLALCHEMY_POOL_TIMEOUT = 10
SQLALCHEMY_POOL_RECYCLE = 7200
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Redis 配置
REDIS_URL = "redis://127.0.0.1:6379/0"
REDIS_MAX_CONNECTIONS = 20


# Celery 配置
CELERY_FORCE_ROOT = True
CELERY_TIMEZONE = "Asia/Shanghai"
BROKER_URL = "redis://127.0.0.1:6379/10"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/12"
CELERY_ACCEPT_CONTENT = ["pickle"]
CELERY_TASK_SERIALIZER = "pickle"
CELERY_RESULT_SERIALIZER = "pickle"
CELERY_ROUTES = {}
# CELERYBEAT_SCHEDULE = {
#    "auto_check_deploy_status": {
#        "task": "monarch.tasks.ai.auto_check_deploy_status",
#        "schedule": datetime.timedelta(seconds=AUTO_CHECK_DEPLOY_STATUS)
#    }
# }


# SMS请求域名
SMS_BASE_URL = ""

try:
    from local_settings import *  # noqa
except Exception as err:  # noqa
    pass
