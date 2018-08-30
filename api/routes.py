# api path
from api import app
from httpRequestHelper import TaskHelper
from httpRequestHelper.HttpResponseGenerator import HttpResponse
from database import DatabaseHelper
from flask import jsonify, abort, request
from log import Logger

logger = Logger.getLogger("routes")


@app.route("/task", methods=['POST'])
def generateTaskId():
    logger.info('Received Request: %s', request.get_data())
    if request.method == 'POST':
        location = request.json.get('Location')
        user_token = request.json.get('UserToken')
        radius = request.json.get('Radius')

        try:
            task_token = TaskHelper.setUpTask(location, user_token, radius)
        except Exception as e:
            logger.error(e)
            return abort(500, "Something wrong when set up the task")

        status = DatabaseHelper.addTask(task_token, user_token)
        httpResponse = HttpResponse()
        if status:
            httpResponse.addData("taskToken", task_token)
            return httpResponse.getResponse()
        else:
            return abort(200, "DataBase Error")

    return abort(404)


@app.route("/", methods=['GET', 'POST'])
def hh():
    logger.info("Hello World")
    return abort(404, "Hello World")
