from db.models import LotsModel
from base import ControlBase


class LotsControl(ControlBase):
    def __init__(self):
        super().__init__(LotsModel)
