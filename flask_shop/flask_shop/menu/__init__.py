from flask import Blueprint
from flask_restful import Api

menu = Blueprint('menu', __name__)
menu_api = Api(menu)

from flask_shop.menu import view