
import json
import os

import memcache

from zuman import constants

conf = {}
if os.getenv('FLASK_APP') == constants.FLASK_APP_DEV:
    conf['CONFIG_FILE'] = os.getcwd() + "/web/config/conf.json"
else:
    conf['CONFIG_FILE'] = "/var/zuman.one/conf.json"

with open(conf['CONFIG_FILE']) as config_file:
    conf = json.load(config_file)

    if os.getenv('FLASK_APP') == constants.FLASK_APP_DEV:
        conf['SESSION_MEMCACHED'] = "localhost:11211"
    conf["SQLALCHEMY_DATABASE_URI"] = conf["SQLALCHEMY_DATABASE_URI"].replace("DB_PASS", os.getenv('DB_PASS'))


class Config:
    SECRET_KEY = conf["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = conf["SQLALCHEMY_DATABASE_URI"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = conf['MAIL_USERNAME']
    MAIL_PASSWORD = conf['MAIL_PASSWORD']
    LOG_LEVEL = conf['LOG_LEVEL']
    SESSION_TYPE = conf['SESSION_TYPE']
    SESSION_MEMCACHED = memcache.Client([conf['SESSION_MEMCACHED']])
    SESSION_COOKIE_NAME = conf['SESSION_COOKIE_NAME']
    SESSION_COOKIE_SECURE = conf['SESSION_COOKIE_SECURE']
    PERMANENT_SESSION_LIFETIME = conf['PERMANENT_SESSION_LIFETIME']
    REMEMBER_COOKIE_DURATION = conf['REMEMBER_COOKIE_DURATION']
    REMEMBER_COOKIE_HTTPONLY = conf['REMEMBER_COOKIE_HTTPONLY']
    REMEMBER_COOKIE_SECURE = conf['REMEMBER_COOKIE_SECURE']
