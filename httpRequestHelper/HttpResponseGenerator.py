from flask import Response
from log import Logger
import json

logger = Logger.getLogger("HttpResponse")
class HttpResponse:
    def __init__(self):
        self.data = {}
        self.status = 200

    def addData(self, key, value):
        self.data[key] = value

    def setStatus(self, status):
        self.status = status

    def getResponse(self):
        data = json.dumps(self.data)
        response = Response(response=data, content_type='application/json', status=200)
        logger.info(response.data)
        return response
