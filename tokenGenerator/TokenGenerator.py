import hashlib
from log import Logger

logger = Logger.getLogger('TokenGenerator')


def generateTaskToken(location, radius):
    logger.info('Generating Token for {}, {}'.format(location, radius))
    lat = location['latitude']
    long = location['longitude']
    taskString = str(long) + ',' + str(lat) + ',' + str(radius)
    logger.debug(taskString.encode())
    taskToken = hashlib.md5(taskString.encode()).hexdigest()
    logger.info("Token for {} is {}".format(taskString, taskToken))
    return taskToken
