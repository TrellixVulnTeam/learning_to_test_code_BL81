from flask import (
    Blueprint, current_app, flash, make_response, redirect, render_template, request, send_file, send_from_directory, url_for, g
)
import flask_excel
from app import db
from app.models import Todo
from app.main import bp

@bp.before_request
def before_request():
    total_items = Todo.query.count()
    complete_items = Todo.query.filter(Todo.complete == 1).count()
    remaining_items = total_items - complete_items
    g.count = str(remaining_items)

@bp.route('/', methods=['GET','POST']) #GET
def index():
    if request.method == 'POST':
        todo_text = request.form['todo_text']
        if not todo_text:
            flash('Task name is required.')
        else:
            db.session.add(Todo(todo_text=todo_text))
            db.session.commit()
            return redirect(url_for('main.index'))

    todo_list = Todo.query.all()
    return render_template('index.html', todo_list=todo_list)

@bp.route("/delete/<string:todo_id>", methods=['GET','POST'])
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("main.index"))

@bp.route("/complete/<string:todo_id>", methods=['GET','POST'])
def complete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("main.index"))

@bp.route("/custom_export", methods=["GET"])
def docustomexport():
    query_sets = Todo.query.all()
    column_names = ["id", "todo_text", "complete"]
    return flask_excel.make_response_from_query_sets(
        query_sets, column_names, "csv", file_name="custom_sheet")