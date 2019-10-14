import sqlalchemy
from sqlalchemy import create_engine
from redis import Redis
from setting import sql_str, redis_str


engine = create_engine(sql_str, pool_size=100, pool_recycle=1800, pool_timeout=60,
                       max_overflow=10)

def get_db():
    return engine.connect()

def get_redis():
    return Redis.from_url(redis_str)