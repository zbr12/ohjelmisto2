import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key-goes-here'
    MYSQL_HOST = os.environ.get('MYSQL_HOST') or 'mysql.metropolia.fi'
    MYSQL_PORT = os.environ.get('MYSQL_PORT') or 3306
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE') or 'user'
    MYSQL_USER = os.environ.get('MYSQL_USER') or 'user'
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or 'password'