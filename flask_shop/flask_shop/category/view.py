from flask_shop.category import category, category_api, attribute, attribute_api
from flask_shop import models, db
from flask import request
from flask_restful import Resource
from flask_shop.utils.message import to_dict_msg


class Category(Resource):
    def get(self):
        try:
            cid = request.args.get('cid')
            c = models.Category.query.get(cid)
            if c:
                return to_dict_msg(200, c.to_dict())
            else:
                return to_dict_msg(10022)
        except Exception:
            return to_dict_msg(20000)

    def post(self):
        try:
            name = request.form.get('name') if request.form.get('name') else ''
            level = int(request.form.get('level')
                        ) if request.form.get('level') else None
            pid = int(request.form.get('pid')
                      ) if request.form.get('pid') else 0
            if all([name, level]):
                if pid:
                    c = models.Category(name=name, level=level, pid=pid)
                else:
                    c = models.Category(name=name, level=level)
                db.session.add(c)
                db.session.commit()
                return to_dict_msg(200, msg='增加商品分类成功')
            return to_dict_msg(10000)
        except Exception as e:
            return to_dict_msg(20000)

    def put(self):
        try:
            cid = request.form.get('cid')
            name = request.form.get('name')
            c = models.Category.query.get(cid)
            if c:
                c.name = name
                db.session.commit()
                return to_dict_msg(200, msg='更新商品分类成功')
            return to_dict_msg(10022)
        except Exception as e:
            return to_dict_msg(20000)

    def delete(self):
        cid = request.form.get('cid')
        c = models.Category.query.get(cid)
        if c:
            db.session.delete(c)
            db.session.commit()
            return to_dict_msg(200, msg='删除商品分类成功！')
        return to_dict_msg(10022)


category_api.add_resource(Category, '/category')


@category.route('/category_list')
def get_categroy_list():
    level = int(request.args.get('level')) if request.args.get(
        'level') and int(request.args.get('level')) <= 3 else 0
    pnum = int(request.args.get('pnum')) if request.args.get('pnum') else 0
    psize = int(request.args.get('psize')) if request.args.get('psize') else 0

    cate_list = []
    base_query = models.Category.query.filter(models.Category.level == 1)

    if all([pnum, psize]):
        categories = base_query.paginate(pnum, psize)
        if level:
            cate_list = get_tree(categories.items, level, True)
        else:
            cate_list = get_tree(categories.items, level, False)
        data = {
            'pnum': pnum,
            'psize': psize,
            'total': categories.total,
            'data': cate_list
        }
        return to_dict_msg(200, data, '获取商品分类列表成功')
    else:
        categories = base_query.all()
        if level:
            cate_list = get_tree(categories, level, True)
        else:
            cate_list = get_tree(categories, level, False)
        return to_dict_msg(200, {'data': cate_list}, '获取商品分类列表成功')


def get_tree(info_list, level, flag):
    info_dict = []
    if info_list:
        for i in info_list:
            i_dict = i.to_dict()
            if flag:
                if i.level < level:
                    i_dict['children'] = get_tree(i.children, level, flag)
            else:
                if i.level != 3:
                    i_dict['children'] = get_tree(i.children, level, flag)
            info_dict.append(i_dict)
    return info_dict


class Attribute(Resource):
    def post(self):
        try:
            name = request.form.get('name')
            cid = request.form.get('cid')
            _type = request.form.get('_type')
            val = request.form.get('val')

            if all([name, cid, _type]):
                if val:
                    attr = models.Attribute(
                        name=name, cid=int(cid), _type=_type, val=val)
                else:
                    attr = models.Attribute(
                        name=name, cid=int(cid), _type=_type)
                db.session.add(attr)
                db.session.commit()
                return to_dict_msg(200, msg="增加分类参数成功")
            else:
                return to_dict_msg(10000)
        except Exception:
            return to_dict_msg(20000)

    def get(self):
        id = request.args.get('id')
        attr = models.Attribute.query.get(id)
        if attr:
            return to_dict_msg(200, attr.to_dict(), msg="获取分类参数成功")
        else:
            return to_dict_msg(10022)

    def put(self):
        try:
            id = request.form.get('id')
            name = request.form.get('name')
            val = request.form.get('val')
            cid = int(request.form.get('cid')
                      ) if request.form.get('cid') else 0
            if all([id, cid, name]):
                attr = models.Attribute.query.get(id)
                if attr:
                    attr.name = name
                    attr.val = val
                    attr.cid = cid
                    db.session.commit()
                    return to_dict_msg(200, msg='更新数据成功')
                else:
                    return to_dict_msg(10022)
            else:
                return to_dict_msg(10000)
        except Exception as e:
            return to_dict_msg(20000)

    def delete(self):
        id = request.form.get('id')
        attr = models.Attribute.query.get(id)
        if attr:
            db.session.delete(attr)
            db.session.commit()
            return to_dict_msg(200, attr.to_dict(), msg='删除分类参数成功')
        else:
            return to_dict_msg(10022)


attribute_api.add_resource(Attribute, '/attribute')


@attribute.route('/attr_list')
def get_attr_list():
    cid = request.args.get('cid')
    _type = request.args.get('_type')
    if all([cid, _type]):
        cate = models.Category.query.get(cid)
        attr_list = []
        if cate:
            if 'static' == _type:
                attr_list = [a.to_dict()
                             for a in cate.attrs if a._type == 'static']
            else:
                attr_list = [a.to_dict()
                             for a in cate.attrs if a._type == 'dynamic']
            return to_dict_msg(200, attr_list, msg="获取分类属性列表成功！！")
        else:
            return to_dict_msg(10022)
    else:
        return to_dict_msg(10000)

from sqlalchemy import func

@category.route('/cate_group_level')
def get_cate_group_by_level():
    # group_data  =models.Category.query.group_by(models.Category.level).having(models.Category.level > 0).all()
    group_data  = db.session.query(models.Category.level,func.count(1).label('count')).group_by(models.Category.level).having(models.Category.level >0).all()
    data={
        'name':'数量',
        'xAxis':[f'{g[0]}级分类' for g in group_data],
        'series_data':[g[1] for g in group_data]
    }
    return to_dict_msg(200,data,'获取统计数据成功')
