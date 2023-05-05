from flask_shop.user import user,user_api
from flask_shop import models,db
from flask import request
from flask_restful import Resource,reqparse
import re
from flask_shop.utils.message import to_dict_msg
from flask_shop.utils.tokens import generate_auth_token,verify_auth_token,login_required

@user.route('/')
def index():
    return 'user hello!!'

@user.route('/login', methods=['POST'])
# @login_required
def login():
    name = request.form.get('name')
    pwd = request.form.get('pwd')

    if not all([name, pwd]):
        return to_dict_msg(10000)
    if len(name)>1:
        usr = models.User.query.filter_by(name=name).first()
        if usr:
            if usr.check_password(pwd):
                token = generate_auth_token(usr.id, 1000)
                verify_auth_token(token)
                return to_dict_msg(200, data={'token': token})
    
    return to_dict_msg(10001)


class User(Resource):
    def get(self):
        try:
            id = int(request.args.get('id').strip())
            usr = models.User.query.filter_by(id=id).first()
            if usr:
                return to_dict_msg(200,usr.to_dict())
            else:
                return to_dict_msg(200,[],'没有该用户')
        except Exception:
            return to_dict_msg(10000)

    def post(self):
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        real_pwd = request.form.get('real_pwd')
        nick_name = request.form.get('nick_name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        
        # 验证数据的正确性
        if not all([name,pwd,real_pwd]):
            return to_dict_msg(10000)

        if len(name)<2:
            return to_dict_msg(10011)
        
        if pwd != real_pwd:
            return to_dict_msg(10012)
        
        if len(pwd)<2:
            return to_dict_msg(10013)
        
        if phone:
            if not re.match(r'^1[34578]\d{9}$', phone):
                return to_dict_msg(10014)
        
        if email:
            if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
                return to_dict_msg(10015)
        
        try:
            rid = int(request.form.get('role_name')) if request.form.get('role_name') else ''
            usr = models.User(name=name, password=pwd, nick_name=nick_name, phone=phone,
                              email=email, rid=rid)
            db.session.add(usr)
            db.session.commit()
            return to_dict_msg(200)
        except Exception:
            return to_dict_msg(2000)
        
    def put(self):
        try:
            id = int(request.form.get('id').strip())
            email = request.form.get('email').strip() if request.form.get('email') else ''
            phone = request.form.get('phone').strip() if request.form.get('phone') else ''
            rid = int(request.form.get('role_name')) if request.form.get('role_name') else ''
            
            usr = models.User.query.get(id)
            if usr:
                usr.email = email
                usr.phone = phone
                usr.rid = rid
                db.session.commit()
                return to_dict_msg(200,msg='修改数据成功！')
            else:
                return to_dict_msg(10018)
        except Exception:
            return to_dict_msg(10000)
        
    def delete(self):
        try:
            # id = int(request.form.get('id').strip())
            id = request.json.get('id')
            usr = models.User.query.get(id)
            if usr:
                db.session.delete(usr)
                db.session.commit()
                return to_dict_msg(200,msg='删除数据成功！')
            else:
                return to_dict_msg(10019)
        except Exception:
            return to_dict_msg(20000)
        
    
user_api.add_resource(User, '/user')

@user.route('/reset',methods=['GET'])
def reset():
    try:
        id = request.args.get('id')
        usr = models.User.query.get(id)
        usr.password = '123'
        db.session.commit()
        return to_dict_msg(200, msg='重置密码成功')
    except Exception as e:
        return to_dict_msg(20000)


@user.route('/test')
@login_required
def test():
    return to_dict_msg(200)

class UserList(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name',type=str)
        parser.add_argument('pnum',type=int)
        parser.add_argument('psize',type=int)
        try:
            args = parser.parse_args()
            name = args.get('name')
            pnum = args.get('pnum') if args.get('pnum') else 1
            psize = args.get('psize') if args.get('psize') else 2   
            if name:
                user_p = models.User.query.filter(models.User.name.like(f'%{name}%')).paginate(pnum,psize)
            else:
                user_p = models.User.query.paginate(pnum,psize)
            data = {
                'pnum':pnum,
                'totalPage':user_p.total,
                'users':[user.to_dict() for user in user_p.items]
            }
            return to_dict_msg(200,data)
        
        except Exception:
            return to_dict_msg(10000)
        
user_api.add_resource(UserList, '/userlist')
