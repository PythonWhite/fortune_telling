from db import db, get_redis


class ControlBase():
    def __init__(self, model):
        self.db = db
        self.r = get_redis()
        self.model = model

    def get_one(self, id):
        return self.model.query.get(id)

    def get_list(self):
        return self.model.query
