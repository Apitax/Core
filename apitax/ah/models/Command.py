from apitax.ah.models.Options import Options
from apitax.ah.flow.requests.ApitaxRequest import ApitaxRequest


class Command:
    def __init__(self, command: list = None, request: ApitaxRequest = ApitaxRequest(), parameters: dict = {}, options: Options = Options()):
        self.command = command
        self.options = options
        self.request = request
        self.parameters = parameters