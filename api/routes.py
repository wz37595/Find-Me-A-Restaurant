# api path
from api import app
from httpRequestHelper import taskHelper
from database import databaseHelper
from flask import jsonify, abort, request
from log import Logger

logger = Logger.getLogger("routes")

@app.route("/task", methods=['POST'])
def generateTaskId():
    logger.info('Received Request: %s', request.get_data())
    if request.method == 'POST':
        location = request.json.get('Location')
        userToken = request.json.get('UserToken')
        radius = request.json.get('Radius')

        try:
            taskToken = taskHelper.setUpTask(location, userToken, radius)
        except Exception as e:
            logger.error(e)
            return abort(500, "Something wrong when set up the task")

        status = databaseHelper.addTask(taskToken, userToken)
        if status:
            return taskToken
        else:
            return abort(200, "DataBase Error")

    return abort(404)

@app.route("/", methods=['GET', 'POST'])
def hh():
    logger.info("Hello World")
    return abort(404, "Hello World")
