from flask_restful import Resource, Api, reqparse
from db.models import LotsModel

db = None

parser = reqparse.RequestParser()


class LotteryHandler(Resource):

    def get(self, lot_num):
        data = parser.parse_args()
        _type = data.get('_type')

        lot = db.query(LotsModel).filter(LotsModel.num == lot_num)\
                                 .filter(LotsModel.lot_type == _type)

        if not lot:
            return '签名不存在'

        return lot

    def _get_list(self):
        data = parser.parse_args()
        _type = data['_type']
        lots = db.query(LotsModel).filter(LotsModel.lot_type == _type)

        return lots

    def post(self):
        data = parser.parse_args()
        num = data['num']
        lot_type = data['lot_type']
        content = data['content']
        name = data['name']
        solution = data['solution']
        poetry = data['poetry']
        p_solution = data['p_solution']
        meaning = data['meaning']

        return '添加成功'

    def put(self, lid):
        data = parser.parse_args()
        lot = db.query(LotsModel).get(lid)
        if not lot:
            return '签名不存在'

        lot.content = data['content']
        lot.name = data['name']
        lot.solution = data['solution']
        lot.poetry = data['poetry']
        lot.p_solution = data['p_solution']
        lot.meaning = data['meaning']

        db.commit()
        return '修改成功'

    def delete(self, lid):
        lot = db.query(LotsModel).get(lid)
        if not lot:
            return '签名不存在'

        lot.delete()
        db.commit()
        return '删除成功'
