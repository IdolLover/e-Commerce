from flask import Blueprint
from flask_restful import Api

goods = Blueprint('goods',__name__)
goods_api = Api(goods)

from flask_shop.goods import view