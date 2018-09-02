from flask import Response
from log import Logger
import json

logger = Logger.getLogger("HttpResponse")


class HttpResponse:
    def __init__(self):
        self.data = {}
        self.status = 200
        self.data["Status"] = 200

    def add_data(self, key=None, value=None, dict=None):
        if key and value:
            self.data[key] = value

        if dict:
            self.data.update(dict)

    def set_status(self, status):
        self.status = status

    def get_response(self):
        data = json.dumps(self.data)
        response = Response(response=data, content_type='application/json', status=200)
        logger.info(response.data)
        return response
