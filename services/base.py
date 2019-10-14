from db import get_db, get_redis


class ControlBase():
    def __init__(self, model):
        self.db = get_db()
        self.r = get_redis()
        self.model = model

    def get_one(self, id):
        return self.db.query(self.model).get(id)

    def get_list(self):
        return self.db.query(self.model)
