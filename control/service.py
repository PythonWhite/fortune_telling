from db.models import ServiceModel
from services.base import ControlBase
from lib.util import query_to_dict, dict_querys


class ServiceControl(ControlBase):
    def __init__(self):
        super().__init__(ServiceModel)

    def format_result(self, query):
        return query_to_dict(query)

    def format_results(self, query):
        return dict_querys(query)