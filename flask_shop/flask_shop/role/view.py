from flask_shop.role import role,role_api
from flask_shop import models,db
from flask import request
from flask_restful import Resource
from flask_shop.utils.message import to_dict_msg

class Role(Resource):
    def get(self):
        try:
            role_list = []
            roles = models.Role.query.all()
            role_list = [r.to_dict() for r in roles]
            return to_dict_msg(200,data=role_list,msg='获取角色列表成功')
        except Exception:
            return to_dict_msg(20000)
        
    def post(self):
        name = request.form.get('name')
        desc = request.form.get('desc')
        try:
            if name:
                role = models.Role(name=name,desc=desc)
                db.session.add(role)
                db.session.commit()
                return to_dict_msg(200,msg='添加角色成功')
            else:
                return to_dict_msg(10000)
        except Exception:
            return to_dict_msg(20000)

    def delete(self):
        try:
            id = int(request.form.get('id'))
            r = models.Role.query.get(id)
            if r:
                db.session.delete(r)
                db.session.commit()
                return to_dict_msg(200,msg='删除角色成功')
            else:
                return to_dict_msg(10000)
        except Exception:
            return to_dict_msg(10000)
        
    def put(self):
        try:
            id = int(request.form.get('id'))
            name = request.form.get('name').strip() if request.form.get('name') else ''
            desc = request.form.get('desc').strip() if request.form.get('desc') else ''
            if name:
                r = models.Role.query.get(id)
                if r:
                    r.name = name
                    r.desc = desc
                    db.session.commit()
                    return to_dict_msg(200,msg='修改角色成功')
                return to_dict_msg(10020)
            return to_dict_msg(10000)

        except Exception:
            return to_dict_msg(20000)

role_api.add_resource(Role, '/role')

@role.route('/del_menu/<int:rid>/<int:mid>')
def del_menu(rid,mid):
    try:
        r = models.Role.query.get(rid)
        m = models.Menu.query.get(mid)
        if all([r,m]):
            if m in r.menus:
                r.menus.remove(m)
                if m.level==1:
                    for s in m.children:
                        if s in r.menus:
                            r.menus.remove(s)
                db.session.commit()
                return to_dict_msg(200,data=r.get_menu_dict(),msg='删除菜单成功')
            return to_dict_msg(10021)
        return to_dict_msg(10000)
    except Exception:
        return to_dict_msg(20000)
    
@role.route('/set_menu/<int:rid>',methods=['post'])
def set_menu(rid):
    try:
        role = models.Role.query.get(rid)
        mids = request.form.get('mids')
        if role:
            role.menu = []
            for m in mids.split(','):
                if m:
                    tm = models.Menu.query.get(int(m))
                    if tm:
                        role.menus.append(tm)
            db.session.commit()
            return to_dict_msg(200,msg='分配权限成功')
        return to_dict_msg(10020)
    except Exception:
        return to_dict_msg(20000)


