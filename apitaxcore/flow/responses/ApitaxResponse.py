from apitaxcore.flow.responses.Response import Response
from apitaxcore.models.State import State
from apitaxcore.utilities.Json import isJson

import json
import xmltodict


class ApitaxResponse(Response):
    def __init__(self, humanReadable=None, responseFormat=None):
        super().__init__()
        self.options = State.options
        self.log = State.log
        self.humanReadable = humanReadable
        self.responseFormat = responseFormat

    def getResponseBody(self) -> dict:
        body = super().getResponseBody()
        if (self.responseFormat == 'json' and isJson(body)):
            return json.loads(body)
        if (self.responseFormat == 'xml'):
            return xmltodict.parse(body)
        return {"response": body}

    def isStatusSuccess(self) -> bool:
        if (self.getResponseStatusCode() > 299):
            return False
        if (self.getResponseStatusCode() < 200):
            return False
        return True

    def getDebugResponse(self):
        line = ''
        line += 'Status: ' + str(self.getResponseStatusCode()) + '\n'
        line += 'Headers:' + '\n'
        if (self.options.sensitive):
            line += 'Headers are not shown as it contains sensitive data. ie. token' + '\n'
        else:
            line += str(self.getResponseHeaders()) + '\n'
        line += 'Body:' + '\n'
        line += str(self.getResponseBody()) + '\n'
        return line

    ###################
    # QUICK RESPONSES #
    ###################

    def res_success(self, body=None):
        self.status = 200
        if (body):
            self.body.add(body)
        return self

    def res_created(self, body=None):
        self.status = 201
        if (body):
            self.body.add(body)
        return self

    def res_no_content(self, body=None):
        self.status = 204
        if (body):
            self.body.add(body)
        return self

    def res_not_modified(self, body=None):
        self.status = 304
        if (body):
            self.body.add(body)
        return self

    def res_bad_request(self, body=None):
        self.status = 400
        if (body):
            self.body.add(body)
        return self

    def res_unauthorized(self, body=None):
        self.status = 401
        if (body):
            self.body.add(body)
        return self

    def res_forbidden(self, body=None):
        self.status = 403
        if (body):
            self.body.add(body)
        return self

    def res_not_found(self, body=None):
        self.status = 404
        if (body):
            self.body.add(body)
        return self

    def res_conflict(self, body=None):
        self.status = 409
        if (body):
            self.body.add(body)
        return self

    def res_server_error(self, body=None):
        self.status = 500
        if (body):
            self.body.add(body)
        return self