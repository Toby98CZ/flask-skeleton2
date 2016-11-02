"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template, redirect, url_for
from .forms import LogUserForm, AddTaskForm
from ..data.database import db
from ..data.models import LogUser, Task
blueprint = Blueprint('public', __name__)


@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')


@blueprint.route('/loguserinput', methods=['GET', 'POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)


@blueprint.route('/loguserlist', methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)


@blueprint.route('/addtask', methods=['GET', 'POST'])
def AddTaskLog():
    form = AddTaskForm()
    if form.validate_on_submit():
        Task.create(**form.data)
    return render_template("public/AddTask.tmpl", form=form)


@blueprint.route('/tasks', methods=['GET', 'POST'])
def WriteTaskLog():
    pole = db.session.query(Task).all()
    return render_template("public/tasklog.tmpl", data=pole)


@blueprint.route('/removeTask/<int:idpassed>', methods=['GET', 'POST'])
def RemoveTask(idpassed):
    policko = db.session.query(Task).filter_by(id=idpassed).first()
    try:
        db.session.delete(policko)
    except:
        status = ["Chyba", "ERROR"]
        return redirect(url_for('public.WriteTaskLog'))
        #return redirect(url_for('public.WriteTaskLog'))
    db.session.commit()
    return redirect(url_for('public.WriteTaskLog'))
