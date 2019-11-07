from db.models import LotsModel
from base import ControlBase
from lib.util import query_to_dict, dict_querys


class LotsControl(ControlBase):
    def __init__(self):
        super().__init__(LotsModel)

    def get_lot_by_type_and_num(self, type, num):
        return self.model.query.filter(
            self.model.lot_type == type
        ).filter(
            self.model.num == num
        ).first()

    def format_result(self, query):
        return query_to_dict(query)

    def format_results(self, query):
        return dict_querys(query)
