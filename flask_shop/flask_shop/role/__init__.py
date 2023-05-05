from flask import Blueprint
from flask_restful import Api

role = Blueprint('role', __name__)
role_api = Api(role)

from flask_shop.role import view