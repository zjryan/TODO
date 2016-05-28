from . import main
from .forms import TaskForm
from ..models import Task
from .. import db
from flask import render_template, redirect, url_for, flash, abort, make_response, request
from flask.ext.login import current_user, login_required

@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
def index():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(content=form.content.data,
                    author=current_user._get_current_object())
        db.session.add(task)
        flash('Successfully added a task.')
        return redirect(url_for('.index'))
    tasks = None
    if current_user.is_authenticated:
        tasks = Task.query.filter_by(user_id=current_user.id).all()
    show_completed = False
    if current_user.is_authenticated:
        show_completed = bool(request.cookies.get('show_completed', ''))
    return render_template('index.html',
                           form=form,
                           tasks=tasks,
                           show_finished=show_completed)

@main.route('/delete_task/<int:id>')
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)
    if current_user != task.author:
        abort(403)
    if task is not None:
        db.session.delete(task)
    return redirect(url_for('.index'))

@main.route('/complete_task/<int:id>')
@login_required
def complete_task(id):
    task = Task.query.get_or_404(id)
    if current_user != task.author:
        abort(403)
    if task is not None:
        task.complete_task()
    return redirect(url_for('.index'))

@main.route('/show_unfinished')
@login_required
def show_unfinished():
    resp = make_response(redirect(url_for('.index')))
    resp.set_cookie('show_completed', '', max_age=60*60*24)
    return resp

@main.route('/show_finished')
@login_required
def show_finished():
    resp = make_response(redirect(url_for('.index')))
    resp.set_cookie('show_completed', '1', max_age=60*60*24)
    return resp
