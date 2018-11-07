import requests


class LowLevelRequest:
    def __init__(self, endpoint=None, headerData=None, bodyData=None, queryData=None, cookieData=None):
        self.request = None
        self.url = endpoint
        self.body = bodyData
        self.headers = headerData
        self.params = queryData
        self.cookies = cookieData

    def preRequest(self):
        pass

    def postRequest(self):
        pass

    def post(self):
        self.request = requests.post(self.url, data=self.body, headers=self.headers,
                                     params=self.params, cookies=self.cookies)

    def get(self):
        self.request = requests.get(self.url, data=self.body, headers=self.headers,
                                    params=self.params, cookies=self.cookies)

    def put(self):
        self.request = requests.put(self.url, data=self.body, headers=self.headers,
                                    params=self.params, cookies=self.cookies)

    def patch(self):
        self.request = requests.patch(self.url, data=self.body, headers=self.headers,
                                      params=self.params, cookies=self.cookies)

    def delete(self):
        self.request = requests.delete(self.url, data=self.body, headers=self.headers,
                                       params=self.params, cookies=self.cookies)
