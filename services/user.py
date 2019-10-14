from db.models import UserModel
from services.base import ControlBase


class UserControl(ControlBase):
    def __init__(self):
        super().__init__(UserModel)
