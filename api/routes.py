# api path
from api import app
from httpRequestHelper import taskHelper
from database import databaseHelper
from flask import jsonify, Request, abort, Response

@app.route("/task", methods=['POST'])
def generateTaskId():
    if Request.methods == 'POST':
        location = Request.form.get('location')
        userToken = Request.form.get('userToken')
        radius = Request.form.get('radius')

        try:
            taskToken = taskHelper.setUpTask(location, userToken, radius)
        except:
            return abort(500, "Something wrong when set up the task")

        status = databaseHelper.addTask(taskToken, userToken)
        if status:
            return taskToken
        else:
            return abort(200, "DataBase Error")

    return abort(404)

@app.route("/", methods=['GET', 'POST'])
def hh():
    abort(404, "Hello World")
    return
