from log import Logger
from tokenGenerator import TokenGenerator
from exception import Exception
from database import DatabaseHelper

logger = Logger.getLogger("taskHelper")


def setUpTask(location, userToken, radius):
    logger.info("Location: {}, UserToken: {}, Radius: {} ".format(location, userToken, radius))
    if not location:
        raise Exception.NoLocationError
    radius = 50 if not radius else radius
    task_token = TokenGenerator.generateTaskToken(location, radius)
    if DatabaseHelper.is_task_exist(task_token):
        # TODO: Check whether the task still valid : expired? what's the status
        return
    else:
        # TODO: 1. push it to Google pub sub 2. create a new task to Database
        return
    return task_token
