from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_map


db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)
    obj = config_map.get(config_name)
    app.config.from_object(obj)
    db.init_app(app)

    from flask_shop.user import user
    app.register_blueprint(user)

    from flask_shop.menu import menu
    app.register_blueprint(menu)

    from flask_shop.role import role
    app.register_blueprint(role)

    from flask_shop.category import category
    app.register_blueprint(category)

    from flask_shop.category import attribute
    app.register_blueprint(attribute)

    from flask_shop.goods import goods
    app.register_blueprint(goods)

    from flask_shop.order import order
    app.register_blueprint(order)

    return app
