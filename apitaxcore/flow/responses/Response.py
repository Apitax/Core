from apitaxcore.builders.HeaderBuilder import HeaderBuilder
from apitaxcore.builders.BodyBuilder import BodyBuilder
from apitaxcore.flow.responses.LowLevelResponse import LowLevelResponse


class Response(LowLevelResponse):
    def __init__(self, status=None, headers=None, body=None):
        super().__init__()
        self.status = status
        self.headers: HeaderBuilder = headers if headers is not None else HeaderBuilder()
        self.body: BodyBuilder = body if body is not None else BodyBuilder()

    def getResponseHeaders(self):
        if len(self.headers.get()) > 0:
            return self.headers.get()
        return super().getResponseHeaders()

    def getResponseBody(self):
        if len(self.body.get()) > 0:
            return self.body.get()
        return super().getResponseBody()

    def getResponseStatusCode(self):
        if self.status:
            return self.status
        return super().getResponseStatusCode()
