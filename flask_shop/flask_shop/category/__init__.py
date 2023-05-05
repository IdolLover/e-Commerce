from flask import Blueprint
from flask_restful import Api

category = Blueprint('category', __name__)
category_api = Api(category)

attribute = Blueprint('attribute', __name__, url_prefix='/category')
attribute_api = Api(attribute)

from flask_shop.category import view