
import os

import memcache

from zuman import constants

conf = {}
if os.getenv('FLASK_APP') == constants.FLASK_APP_DEV:
    conf['SESSION_MEMCACHED'] = constants.LOCALHOST + ":11211"
    conf["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI').replace("DB_HOST", constants.LOCALHOST)
else:
    conf['SESSION_MEMCACHED'] = os.getenv('SESSION_MEMCACHED')
    conf["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI').replace("DB_HOST", "db")
conf["SQLALCHEMY_DATABASE_URI"] = conf["SQLALCHEMY_DATABASE_URI"].replace("DB_PASS", os.getenv('POSTGRES_PASSWORD'))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SALT = os.getenv("SALT")
    LOG_LEVEL = os.getenv("LOG_LEVEL")

    SQLALCHEMY_DATABASE_URI = conf["SQLALCHEMY_DATABASE_URI"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_TYPE = os.getenv('SESSION_TYPE')
    SESSION_MEMCACHED = memcache.Client([conf['SESSION_MEMCACHED']])
    SESSION_COOKIE_NAME = os.getenv('SESSION_COOKIE_NAME')
    SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE') == 'True'
    PERMANENT_SESSION_LIFETIME = int(os.getenv('PERMANENT_SESSION_LIFETIME'))

    REMEMBER_COOKIE_DURATION = int(os.getenv('REMEMBER_COOKIE_DURATION'))
    REMEMBER_COOKIE_HTTPONLY = os.getenv('REMEMBER_COOKIE_HTTPONLY') == 'True'
    REMEMBER_COOKIE_SECURE = os.getenv('REMEMBER_COOKIE_SECURE') == 'True'

    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
