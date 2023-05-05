import os

class Config():
    # 配置MySQL参数
    MYSQL_DIALECT = 'mysql'
    MYSQL_DIRVER = 'pymysql'
    MYSQL_NAME = 'your-name'
    MYSQL_PWD = 'your-pasword'
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_DB = 'your-db'
    MYSQL_CHARSET ='utf8mb4'

    SQLALCHEMY_DATABASE_URI = f'{MYSQL_DIALECT}+{MYSQL_DIRVER}://{MYSQL_NAME}:{MYSQL_PWD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset={MYSQL_CHARSET}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.urandom(16)
    DEBUG=True

    ALLOWED_IMGS = set(['bmp','png','jpg','jpeg','gif'])
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SERVER_IMG_UPLOADS = os.path.join(BASE_DIR,'flask_shop','static','img')

class DevelopConfig(Config):
    DEBUG = True

class ProductConfig(Config):
    DEBUG = False

config_map = {
    'develop':DevelopConfig,
    'product':ProductConfig
}