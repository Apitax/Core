from apitaxcore.models.State import State
from apitaxcore.flow.requests.Request import Request
from apitaxcore.flow.responses.ApitaxResponse import ApitaxResponse
import re
import xmltodict


class ApitaxRequest(Request):
    def __init__(self, humanReadable=None, endpoint=None, pathData=None, requestFormat=None):
        super().__init__()
        self.options = State.options
        self.log = State.log
        self.preEndpoint = endpoint
        self.formedEndpoint = endpoint
        self.humanReadable = humanReadable
        self.path = pathData
        self.requestFormat = requestFormat

    def preRequest(self):
        self.endpoint = self.preEndpoint
        if self.path:
            self.injectPathData()
        super().preRequest()
        if self.requestFormat == 'xml':
            self.body = xmltodict.unparse(self.body)

    def postRequest(self):
        self.formedEndpoint = self.request.url
        super().postRequest()

    def post(self):
        self.preRequest()
        super().post()
        self.postRequest()

    def get(self):
        self.preRequest()
        super().get()
        self.postRequest()

    def put(self):
        self.preRequest()
        super().put()
        self.postRequest()

    def patch(self):
        self.preRequest()
        super().patch()
        self.postRequest()

    def delete(self):
        self.preRequest()
        super().delete()
        self.postRequest()

    def getResponse(self, format=None) -> ApitaxResponse:
        if format:
            response = ApitaxResponse(responseFormat=format)
        else:
            response = ApitaxResponse(responseFormat=self.requestFormat)
        response.request = self.request
        return response

    def injectPathData(self):
        matches = re.findall('{[A-z0-9]{1,}}', self.preEndpoint)
        for match in matches:
            matchStr = match[1:-1]
            if matchStr in self.path:
                self.endpoint = self.endpoint.replace(match, self.path.get(matchStr))
            else:
                self.log.log('Path data did not contain key for `' + matchStr + '`')

    def getDebugRequest(self):
        line = ''
        line += 'Endpoint:        ' + self.preEndpoint + '\n'
        line += 'Formed Endpoint: ' + self.formedEndpoint() + '\n'
        line += 'Headers:' + '\n'
        if (self.options.sensitive):
            line += 'Headers are not shown as it contains sensitive data. ie. password' + '\n'
        else:
            line += str(self.headers) + '\n'
        line += 'Post Data:' + '\n'
        if (self.options.sensitive):
            line += 'Post Data is not shown as it contains sensitive data. ie. password' + '\n'
        elif (not self.body):
            line += '{}' + '\n'
        else:
            line += str(self.body) + '\n'
        return line
