from db import db, get_redis
from abc import ABCMeta, abstractmethod
from lib.constant import ERROR_DATA_FORMAT, ERROR_UNIQUE_DATA, ERROR_DATA_NOT_EXIST


class ControlBase():
    __metaclass__ = ABCMeta

    def __init__(self, model):
        self.db = db
        self.r = get_redis()
        self.model = model

    def query_one(self, id):
        return self.model.query.get(id)

    def query_list(self, filters):
        is_ok = self.check_data(filters)
        if not is_ok:
            return False, ERROR_DATA_FORMAT
        return True, self.model.query.filter_by(**filters)

    def add(self, parameter):
        is_ok = self.check_data(parameter)
        if not is_ok:
            return False, ERROR_DATA_FORMAT
        instance = self.model(**parameter)
        self.db.session.add(instance)
        self.db.session.commit()
        return True, instance

    def batch_add(self, model_list, is_check=True):
        if is_check:
            for i in model_list:
                if not self.check_data(i):
                    return False, ERROR_DATA_FORMAT

        self.db.session.execute(
            self.model.__table__.insert(),
            model_list
        )
        self.db.session.commit()
        return True, ''

    def update(self, uniques, data):
        if not self.check_data(uniques):
            return False, ERROR_UNIQUE_DATA

        if not self.check_data(data):
            return False, ERROR_DATA_FORMAT

        instance = self.model.query.filter_by(**uniques).first()
        if not instance:
            return False, ERROR_DATA_NOT_EXIST
        for i in data:
            setattr(instance, i, data[i])
        self.db.session.commit()
        return True, instance

    def batch_update(self, data):
        for i in data:
            if not self.check_data(i):
                return False, ERROR_DATA_FORMAT
            elif "id" not in i:
                return False, ERROR_UNIQUE_DATA

        self.db.session.bulk_update_mappings(self.model, data)
        self.db.session.commit()

        return True, ""

    def delete(self, uniques):
        if not self.check_data(uniques):
            return False, ERROR_DATA_FORMAT

        self.db.query(self.model).filter_by(
            **uniques
        ).delete(
            synchronize_session=False
        )
        self.db.session.commit()

        return True, ""

    #  def batch_delete(self, uniques):
    #      pass

    def check_data(self, data):
        if isinstance(data, str) and hasattr(self.model, data):
            return True
        elif isinstance(data, dict):
            for i in data:
                if not hasattr(self.model, i):
                    return False

            return True
        else:
            return False

    def before_save(self, data):
        return data

    @abstractmethod
    def format_result(self, data):
        pass

    @abstractmethod
    def format_results(self, data):
        pass
