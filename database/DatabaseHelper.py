from log import Logger

logger = Logger.getLogger('databaseHelper')


def addTask(taskToken, userToken):
    logger.info("Adding task: {} for user: {} into database".format(taskToken, userToken))
    return True
