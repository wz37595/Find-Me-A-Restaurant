from log import Logger
from exception import Exception
from api import model

logger = Logger.getLogger('databaseHelper')


def addTask(taskToken, userToken):
    logger.info("Adding task: {} for user: {} into database".format(taskToken, userToken))
    user = model.User()
    return True


def getTaskStatus(taskToken, userToken):
    if not taskToken:
        logger.error("taskToken is none... We need a taskToken to find the task")
        raise Exception.NoTaskTokenError
    # TODO: do some data base look up here....
    # Exception: Doesn't exist
    # returnValue: COMPLETE PENDING STARTED
