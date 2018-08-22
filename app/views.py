# -*- coding:utf-8 -*-
from app import app
from flask import render_template,request
from models import Todo, TodoForm
# 初始路由
@app.route('/')
def index():
    form = TodoForm()
    todos = Todo.objects.all()
    return render_template('index.html', todos=todos, form=form)
# 添加按钮路由
@app.route('/add', methods=['POST', ])
def add():
    # request传入表单数据
    form = TodoForm(request.form)
    # 表单验证
    if form.validate():
        # 将表单内容传入
        content = form.content.data
        todo = Todo(content = content)
        # 保存todo表单
        todo.save()
    todos = Todo.objects.all()
    return render_template('index.html', todos=todos, form=form)