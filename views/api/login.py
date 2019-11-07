from flask_restful import Resource, reqparse

from db.models import UserModel

db = None

parser = reqparse.RequestParser()


class UserLoginHandler(Resource):
    def post(self):
        data = parser.parse_args()
        if 'username' not in data or 'password' not in data:
            return '请输入用户名或密码'

        if 'code' not in data:
            return '请输入验证码'

        return '登录成功'

    def get(self):
        data = parser.parse_args()
        if 'user_id' not in data:
            return '参数错误'

        return '退出登录成功'


class AdminLoginHandler(Resource):
    def post(self):
        data = parser.parse_args()
        if 'username' not in data or 'password' not in data:
            return '请输入用户名或密码'

        if 'code' not in data:
            return '请输入验证码'

        return '登录成功'

    def get(self):
        data = parser.parse_args()
        if 'user_id' not in data:
            return '参数错误'

        return '退出登录成功'


class UserHandler(Resource):
    def get(self, uid=None):
        if uid is None:
            resp = self._get_user_list()
        else:
            resp = self._get_user_one(uid)

        return resp

    def _get_user_one(self, uid):
        user = db.query(UserModel).get(uid)
        if not user:
            return '用户不存在'

        return user

    def _get_user_list(self):
        data = parser.parse_args()
        users = db.query(UserHandler).all()

        return users

    def post(self):
        data = parser.parse_args()

        username = data.get('username')
        password = data.get('password')

        return '添加成功'

    def put(self, uid):
        data = parser.parse_args()
        user = db.query(UserModel).get(uid)
        user.username = data['username']

        return '修改成功'

    def delete(self, uid):
        user = db.query(UserModel).filter(UserModel.id == uid)
        if not user:
            return '用户不存在'

        user.delete()

        return '删除成功'


class AdminUserHandler(Resource):
    def get(self, uid=None):
        if uid is None:
            resp = self._get_user_list()
        else:
            resp = self._get_user_one(uid)

        return resp

    def _get_user_one(self, uid):
        user = db.query(UserModel).get(uid)
        if not user:
            return '用户不存在'

        return user

    def _get_user_list(self):
        data = parser.parse_args()
        users = db.query(UserHandler).all()

        return users

    def post(self):
        data = parser.parse_args()

        username = data.get('username')
        password = data.get('password')

        return '添加成功'

    def put(self, uid):
        data = parser.parse_args()
        user = db.query(UserModel).get(uid)
        user.username = data['username']

        return '修改成功'

    def delete(self, uid):
        user = db.query(UserModel).filter(UserModel.id == uid)
        if not user:
            return '用户不存在'

        user.delete()

        return '删除成功'
