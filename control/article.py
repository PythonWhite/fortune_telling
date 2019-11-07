from db.models import ArticleModel
from services.base import ControlBase
from lib.util import query_to_dict, dict_querys


class ArticleControl(ControlBase):
    def __init__(self):
        super().__init__(ArticleModel)

    def format_result(self, query):
        return query_to_dict(query)

    def format_results(self, query):
        return dict_querys(query)
