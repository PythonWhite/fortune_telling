from control.admin_user import UserControl
from lib.util import write_rsponse


def login(data):
    username = data.get("username")
    password = data.get("password")
    uc = UserControl()
    is_ok, data = uc.check_login(username, password)

    return write_rsponse()
