from apitax.ah.flow.responses.Response import Response
from apitax.ah.models.State import State
from apitax.utilities.Json import isJson

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
        if(self.responseFormat == 'json' and isJson(body)):
            return json.loads(body)
        if(self.responseFormat == 'xml'):
            return xmltodict.parse(body)
        return {"response": body}

    def isStatusSuccess(self) -> bool:
        if(self.getResponseStatusCode() > 299):
            return False
        if(self.getResponseStatusCode() < 200):
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