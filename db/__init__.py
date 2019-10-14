from flask_sqlalchemy import SQLAlchemy
from redis import Redis
from setting import redis_str

db = SQLAlchemy()


def get_redis():
    return Redis.from_url(redis_str)
