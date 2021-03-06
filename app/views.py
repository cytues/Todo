# -*- coding:utf-8 -*-
from app import app
from flask import render_template,request
from models import Todo, TodoForm
from datetime import datetime
# 初始路由
@app.route('/')
def index():
    form = TodoForm()
    todos = Todo.objects.order_by('-time')
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
        todo = Todo(content = content, time = datetime.now())
        # 保存todo表单
        todo.save()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos=todos, form=form)

@app.route('/done/<string:todo_id>')
def done(todo_id):
    form = TodoForm()
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 1
    todo.save()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos = todos, form = form)

@app.route('/undone/<string:todo_id>')
def undone(todo_id):
    form = TodoForm()
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 0
    todo.save()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos = todos, form = form)

@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    form = TodoForm()
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.delete()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos = todos, form = form)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')