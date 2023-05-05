from flask import Blueprint
from flask_restful import Api

order = Blueprint('order',__name__)
order_api = Api(order)

from flask_shop.order import view