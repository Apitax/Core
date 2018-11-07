from apitaxcore.builders.HeaderBuilder import HeaderBuilder
from apitaxcore.builders.BodyBuilder import BodyBuilder
from apitaxcore.builders.QueryBuilder import QueryBuilder
from apitaxcore.builders.CookieBuilder import CookieBuilder
from apitaxcore.flow.requests.LowLevelRequest import LowLevelRequest


class Request(LowLevelRequest):
    def __init__(self, endpoint=None, headerBuilder=None, bodyBuilder=None,
                 queryBuilder=None, cookieBuilder=None):
        super().__init__()
        self.headerBuilder = headerBuilder
        self.bodyBuilder = bodyBuilder
        self.queryBuilder = queryBuilder
        self.cookieBuilder = cookieBuilder
        
        if not self.headerBuilder:
            self.headerBuilder = HeaderBuilder()
            
        if not self.bodyBuilder:
            self.bodyBuilder = BodyBuilder()
            
        if not self.queryBuilder:
            self.queryBuilder = QueryBuilder()
            
        if not self.cookieBuilder:
            self.cookieBuilder = CookieBuilder()
        
        self.endpoint = endpoint

    def preRequest(self):
        self.url = self.endpoint
        if len(self.headerBuilder.built) > 0:
            self.headers = self.headerBuilder.built

        if len(self.bodyBuilder.built) > 0:
            self.body = self.bodyBuilder.built

        if len(self.queryBuilder.built) > 0:
            self.params = self.queryBuilder.built
            
        if len(self.cookieBuilder.built) > 0:
            self.cookies = self.cookieBuilder.built

        super().preRequest()

    def postRequest(self):
        super().postRequest()
