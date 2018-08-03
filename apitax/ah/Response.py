class Response:

    def __init__(self, status=None, body=None):
        self.status = status
        self.body = body
	
    def getResponseBody(self):
        return self.body
        
    def getResponseStatusCode(self):
        return self.status