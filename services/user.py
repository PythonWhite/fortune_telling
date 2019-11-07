from hashlib import sha1 as _sha
from sqlalchemy import or_
from db.models import UserModel
from services.base import ControlBase
from lib.util import query_to_dict


class UserControl(ControlBase):
    def __init__(self):
        super().__init__(UserModel)

    def gen_password(self, pwd):
        return _sha(pwd.encode("utf-8")).hexdigest()

    def check_password(self, user, pwd):
        pwd = self.gen_password(pwd)
        if user and user.password == pwd:
            return True

        return False

    def get_user_by_name(self, name):
        return self.model.query.filter(
            or_(
                self.model.account == name,
                self.model.email == name,
                self.model.phone == name
            )).first()

    def check_login(self, name, pwd):
        return self.check_password(self.get_user_by_name(name), pwd)

    def before_save(self, data):
        if not isinstance(data, dict):
            return data

        if "password" not in data:
            return data

        if len(data["password"]) >= 40:
            return data

        data["password"] = self.gen_password(data["password"])

        return data

    def add(self, data):
        data = self.before_save(data)
        return super().before_save(data)

    def update(self, uniques, data):
        data = self.before_save(data)
        return super().update(uniques, data)

    def format_result(self, query):
        data = query_to_dict(query)
        if "password" in data:
            del data["password"]

        return data

    def format_results(self, data):
        return [self.format_result(d) for d in data]
