class Credentials:
    def __init__(self, username=None, password=None, token=None, extra={}):
        self.username = username
        self.password = password
        self.token = token
        self.extra = extra

    def getAuthObj(self):
        return {'username': self.username, 'password': self.password, 'token': self.token}

    def serialize(self):
        return str(self.username)
