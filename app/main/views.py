from . import main
from .forms import TaskForm
from ..models import Task, User
from .. import db
from flask import render_template, redirect, url_for, flash, abort, make_response, request, current_app
from flask.ext.login import current_user, login_required

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/todo/<username>', methods=['GET', 'POST'])
@login_required
def todo(username):
    form = TaskForm()
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    if current_user == user and form.validate_on_submit():
        task = Task(content=form.content.data,
                    author=user)
        db.session.add(task)
        db.session.commit()
        flash('Successfully added a task.')
        return redirect(url_for('.todo', username=user.username))
    show_completed = False
    if current_user.is_authenticated:
        show_completed = bool(request.cookies.get('show_completed', ''))
    page = request.args.get('page', 1, type=int)
    if show_completed:
        query = Task.query.filter_by(completed=True)
    else:
        query = Task.query.filter_by(completed=False)
    pagination = query.filter_by(author=user)\
                      .order_by(Task.timestamp.desc())\
                      .paginate(page,
                                per_page=current_app.config['TODO_TASKS_PER_PAGE'],
                                error_out=False)
    tasks = pagination.items
    return render_template('todo.html',
                           form=form,
                           user=user,
                           tasks=tasks,
                           show_finished=show_completed,
                           pagination=pagination)


@main.route('/delete_task/<int:id>')
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)
    if current_user != task.author:
        abort(403)
    if task is not None:
        db.session.delete(task)
    return redirect(url_for('.todo', username=task.author.username))

@main.route('/complete_task/<int:id>')
@login_required
def complete_task(id):
    task = Task.query.get_or_404(id)
    print task.author, current_user
    if current_user != task.author:
        abort(403)
    if task is not None:
        task.complete_task()
    return redirect(url_for('.todo', username=task.author.username))

@main.route('/show_unfinished')
@login_required
def show_unfinished():
    resp = make_response(redirect(url_for('.todo', username=current_user.username)))
    resp.set_cookie('show_completed', '', max_age=60*60*24)
    return resp

@main.route('/show_finished')
@login_required
def show_finished():
    resp = make_response(redirect(url_for('.todo', username=current_user.username)))
    resp.set_cookie('show_completed', '1', max_age=60*60*24)
    return resp
