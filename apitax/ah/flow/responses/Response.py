from apitax.ah.builders.HeaderBuilder import HeaderBuilder
from apitax.ah.builders.BodyBuilder import BodyBuilder
from apitax.ah.flow.responses.LowLevelResponse import LowLevelResponse


class Response(LowLevelResponse):
    def __init__(self, status=None, headers=HeaderBuilder(), body=BodyBuilder()):
        super().__init__()
        self.status = status
        self.headers = headers
        self.body = body

    def getResponseHeaders(self):
        if (len(self.headers.get()) > 0):
            return self.headers.get()
        return super().getResponseHeaders()

    def getResponseBody(self):
        if (len(self.body.get()) > 0):
            return self.body.get()
        return super().getResponseBody()

    def getResponseStatusCode(self):
        if (self.status):
            return self.status
        return super().getResponseStatusCode()
