from apitaxcore.builders.HeaderBuilder import HeaderBuilder
from apitaxcore.builders.BodyBuilder import BodyBuilder
from apitaxcore.builders.QueryBuilder import QueryBuilder
from apitaxcore.flow.requests.LowLevelRequest import LowLevelRequest


class Request(LowLevelRequest):
    def __init__(self, endpoint=None, headerBuilder=HeaderBuilder(), bodyBuilder=BodyBuilder(),
                 queryBuilder=QueryBuilder()):
        super().__init__()
        self.headerBuilder = headerBuilder
        self.bodyBuilder = bodyBuilder
        self.queryBuilder = queryBuilder
        self.endpoint = endpoint

    def preRequest(self):
        self.url = self.endpoint
        if (len(self.headerBuilder.built) > 0):
            self.headers = self.headerBuilder.built

        if (len(self.bodyBuilder.built) > 0):
            self.body = self.bodyBuilder.built

        if (len(self.queryBuilder.built) > 0):
            self.params = self.queryBuilder.built

        super().preRequest()

    def postRequest(self):
        super().postRequest()
