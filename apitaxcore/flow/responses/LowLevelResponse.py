from requests import Request


class LowLevelResponse:
    def __init__(self, request: Request = None):
        self.request = request

    def getResponseHeaders(self):
        return self.request.headers

    def getResponseBody(self):
        return self.request.text.replace('\n', '')

    def getResponseStatusCode(self):
        return self.request.status_code
