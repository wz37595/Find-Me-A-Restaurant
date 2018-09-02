# api path
from api import app
from httpRequestHelper import TaskHelper
from httpRequestHelper.HttpResponseGenerator import HttpResponse
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

        status = DatabaseHelper.addTask(task_token, user_token)
        httpResponse = HttpResponse()
        if status:
            httpResponse.addData(key="taskToken", value=task_token)
            return httpResponse.getResponse()
        else:
            return abort(200, "DataBase Error")

    return abort(404)


@app.route("/checktask", methods=['POST'])
def checkTask():
    logger.info('Received Request: %s', request.get_data())
    if request.method == 'POST':
        taskToken = request.json.get('TaskToken')
        userToken = request.json.get('UserToken')
        try:
            status = DatabaseHelper.getTaskStatus(taskToken, userToken)
        except Exception as e:
            return abort(500, "Something wrong when get the task status")

        httpResponse = HttpResponse()
        httpResponse.addData(key='Task Status', value=status)
        return httpResponse.getResponse()
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
            httpResponse.addData("Status", 500)
            httpResponse.addData("Message", "Something wrong when get the task result")
            return httpResponse.getResponse()
        httpResponse.addData(dict=result)
    else:
        httpResponse.addData("Status", 404)
        return httpResponse.getResponse()


@app.route("/", methods=['GET', 'POST'])
def hh():
    logger.info("Hello World")
    return abort(404, "Hello World")
