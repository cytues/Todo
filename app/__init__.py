# -*- coding:utf-8 -*-
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
# 实例化配置
app.config.from_object('config')
# 实例化mongodb数据库
db = MongoEngine(app)

from app import models, views