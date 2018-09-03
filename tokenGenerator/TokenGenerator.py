import hashlib
from log import Logger

logger = Logger.getLogger('TokenGenerator')


def generate_task_token(long, lat, radius, search_string):
    logger.info('Generating Token for long: {}, lat: {}, radius: {}, search_string: {}'
                .format(long, lat, radius, search_string))
    taskString = str(long) + ',' + str(lat) + ',' + str(radius) + ',' + search_string
    logger.debug(taskString.encode())
    taskToken = hashlib.md5(taskString.encode()).hexdigest()
    logger.info("Token for {} is {}".format(taskString, taskToken))
    return taskToken
