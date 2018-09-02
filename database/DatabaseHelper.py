from log import Logger
from exception import Exception
from api import model

logger = Logger.getLogger('databaseHelper')


def add_task(task_token, userToken):
    logger.info("Adding task: {} for user: {} into database".format(task_token, userToken))
    user = model.User()
    return True


def get_task_status(task_token, user_token):
    if not task_token:
        logger.error("taskToken is none... We need a taskToken to find the task")
        raise Exception.NoTaskTokenError
    # TODO: do some data base look up here....
    # Exception: Doesn't exist
    # returnValue: COMPLETE PENDING STARTED


def is_task_exist(task_token):
    return
