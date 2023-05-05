from flask_shop.goods import goods, goods_api
from flask_shop import models, db
from flask import request, current_app
from flask_restful import Resource
from flask_shop.utils.message import to_dict_msg
import hashlib
from time import time


@goods.route('/goods_list')
def get_goods_list():
    name = request.args.get('name')
    if name:
        goods = models.Goods.query.filter(
            models.Goods.name.like(f'%{name}%')).all()
    else:
        goods = models.Goods.query.all()
    goods_list = [gds.to_dict() for gds in goods]
    return to_dict_msg(200, goods_list, '获取商品列表成功')


class Goods(Resource):
    
    def post(self):
        try:
            attr_dynamic = request.form.get('attr_dynamic')
            attr_static = request.form.get('attr_static')
            pics = request.form.get('pics')

            cid_one = request.form.get('cid_one')
            cid_three = request.form.get('cid_three')
            cid_two = request.form.get('cid_two')
            introduce = request.form.get('introduce')
            name = request.form.get('name')
            number = request.form.get('number')
            price = request.form.get('price')
            weight = request.form.get('weight')

            goods = models.Goods(name=name, number=number, price=price,
                          weight=weight, introduce=introduce,
                          cid_one=int(cid_one), cid_two=int(cid_two), cid_three=int(cid_three))
            db.session.add(goods)
            db.session.commit()

            for p in eval(pics):
                tp = models.Picture(gid=goods.id, path=p)
                db.session.add(tp)
            for s in eval(attr_static):
                temp_s = models.GoodsAttr(gid=goods.id, aid=s.get(
                    'id'), val=s.get('val'), _type='static')
                db.session.add(temp_s)
            for d in eval(attr_dynamic):
                temp_d = models.GoodsAttr(gid=goods.id, aid=d.get(
                    'id'), val=d.get('val'), _type="dynamic")
                db.session.add(temp_d)
            db.session.commit()
            return to_dict_msg(200, msg="增加商品成功")
        except Exception:
            return to_dict_msg(20000)
    
    def delete(self):
        id = request.json.get('id')
        goods = models.Goods.query.get(id)
        if goods:
            db.session.delete(goods)
            db.session.commit()
            return to_dict_msg(200, msg='删除商品成功')
        else:
            return to_dict_msg(10022)


goods_api.add_resource(Goods, '/goods')


@goods.route('/upload_img', methods=['POST'])
def upload_img():
    img_file = request.files.get('file')
    if not img_file:
        return to_dict_msg(10023)
    if allowed_img(img_file.filename):
        folder = current_app.config.get('SERVER_IMG_UPLOADS')
        end_prefix = img_file.filename.rsplit('.', 1)[1]
        file_name = md5_file()

        img_file.save(f'{folder}/{file_name}.{end_prefix}')
        data = {
            'path': f'/static/img/{file_name}.{end_prefix}',
            'url': f'http://127.0.0.1:5000/static/img/{file_name}.{end_prefix}'
        }
        return to_dict_msg(200, data, '上传图片成功')
    else:
        return to_dict_msg(10024)


def allowed_img(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in current_app.config['ALLOWED_IMGS']


def md5_file():
    md5_obj = hashlib.md5()
    md5_obj.update(str(time()).encode())
    file_name = md5_obj.hexdigest()
    return file_name
