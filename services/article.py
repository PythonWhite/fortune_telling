from sqlalchemy import or_
from db.models import ArticleModel
from services.base import ControlBase
from lib.util import query_to_dict


class ArticleControl(ControlBase):
    def __init__(self):
        super().__init__(ArticleModel)
    
    