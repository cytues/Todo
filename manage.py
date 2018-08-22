# -*- coding:utf-8 -*-
from app import app
from app.models import Todo
# Flask-Script。为Flask应用提供编写脚本的功能。
# 可以用来运行一个开发服务器，也可以与数据库交互，方便开发
from flask_script import Manager
# 实例化Manager
manager = Manager(app)

# 利用@manager.command注解实现（不带参数）
# 使save函数继承Command父类
@manager.command
def save():
    todo = Todo(content = 'loli')
    todo.save()

if __name__ == '__main__':
    manager.run()