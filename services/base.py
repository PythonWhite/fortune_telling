from db import db, get_redis
from abc import ABCMeta, abstractmethod


class ControlBase():
    __metaclass__ = ABCMeta

    def __init__(self, model):
        self.db = db
        self.r = get_redis()
        self.model = model

    def query_one(self, id):
        return self.model.query.get(id)

    def query_list(self, **kwargs):
        return self.model.query
    
    def add(self, **kwargs):
        pass

    def batch_add(self, model_list):
        pass

    def update(self, uniques, **kwargs):
        pass

    def batch_update(self, uniques, data):
        pass

    def delete(self, uniques):
        pass

    def batch_delete(self, uniques):
        pass

    @abstractmethod
    def format_result(self, data):
        pass

