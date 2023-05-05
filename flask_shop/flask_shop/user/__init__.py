from flask import Blueprint
from flask_restful import Api

user = Blueprint('user', __name__, url_prefix='/user')
user_api = Api(user)

from flask_shop.user import view