# -*- coding:utf-8 -*-
from app import db
# 使用MongoEngine 和 WTForms
from flask_mongoengine.wtf import model_form
import datetime

# 创建todo类的内容
class Todo(db.Document):
    # 内容，添加约束属性，必填和长度
    content = db.StringField(required=True, max_length=20)
    # 时间
    time = db.DateTimeField(default = datetime.datetime.now())
    # 状态
    status = db.IntField(default = 0)
# 实例化表单
TodoForm = model_form(Todo)