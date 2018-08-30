from log import Logger
from tokenGenerator import TokenGenerator
from exception import Exception
logger = Logger.getLogger("taskHelper")


def setUpTask(location, userToken, radius):
    logger.info("Location: {}, UserToken: {}, Radius: {} ".format(location, userToken, radius))
    if not location:
        raise Exception.NoLocationError
    radius = 50 if not radius else radius
    token = TokenGenerator.generateTaskToken(location, radius)
    return token
