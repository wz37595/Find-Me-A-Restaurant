# api path
from api import app
from httpRequestHelper import TaskHelper
from httpRequestHelper.HttpResponseGenerator import HttpResponse
from exception import Exception
from database import DatabaseHelper
from flask import abort, request
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

        httpResponse = HttpResponse()
        httpResponse.add_data(key="taskToken", value=task_token)
        return httpResponse.get_response()

    return abort(404)


@app.route("/checktask", methods=['POST'])
def checkTask():
    logger.info('Received Request: %s', request.get_data())
    if request.method == 'POST':
        taskToken = request.json.get('TaskToken')
        userToken = request.json.get('UserToken')
        try:
            status = DatabaseHelper.get_task_status(taskToken, userToken)
        except Exception as e:
            return abort(500, "Something wrong when get the task status")

        httpResponse = HttpResponse()
        httpResponse.add_data(key='Task Status', value=status)
        return httpResponse.get_response()
    else:

        return abort(404)


@app.route("/getresult", methods=['POST'])
def getResult():
    logger.info('Received Request: %s', request.get_data())
    httpResponse = HttpResponse()
    if request.method == 'POST':
        taskToken = request.json.get('TaskToken')
        try:
            result = DatabaseHelper.getTaskResult(taskToken)
        except Exception as e:
            httpResponse.add_data("Status", 500)
            httpResponse.add_data("Message", "Something wrong when get the task result")
            return httpResponse.get_response()
        httpResponse.add_data(dict=result)
    else:
        httpResponse.add_data("Status", 404)
        return httpResponse.get_response()


@app.route("/", methods=['GET', 'POST'])
def hh():
    logger.info("Hello World")
    return abort(404, "Hello World")
