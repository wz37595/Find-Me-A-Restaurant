import logging


def getLogger(name):
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(funcName)s %(levelname)s: %(message)s")
    return logging.getLogger(name)
