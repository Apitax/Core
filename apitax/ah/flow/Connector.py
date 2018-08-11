from apitax.ah.commandtax.Commandtax import Commandtax
from apitax.ah.flow.LoadedDrivers import LoadedDrivers
from apitax.ah.models.State import State
from apitax.ah.models.Options import Options
from apitax.ah.flow.requests.ApitaxRequest import ApitaxRequest

from time import time


# The 'heart' of the application
# Connector facilitates the initialization of the connection to an API
# Connector handles setting up the driver, authetnication, headers, and then
# using all of that to execute a command
#
# Additional interfaces to this utility should directly communicate with connector
# and likely nothing else. Connector handles the rest.
class Connector:

    def __init__(self, options=Options(), credentials=None, command='', parameters={}):

        self.options = options
        self.parameters = parameters

        self.credentials = credentials

        self.command = command
        self.command = self.command.replace('\\"', '"')
        self.command = self.command.replace('\\\'', '\'')

        self.executionTime = None
        self.commandtax = None
        self.logBuffer = []

        if (not self.options.driver):
            self.options.driver = LoadedDrivers.getDefaultDriver()

        self.request = ApitaxRequest()

        self.request.headerBuilder = self.options.driver.addApiHeaders(self.request.headerBuilder)
        self.request.bodyBuilder = self.options.driver.addApiBody(self.request.bodyBuilder)

        if (self.options.driver.isApiAuthenticated()):
            if (self.options.driver.isApiAuthenticationSeparateRequest()):
                if (self.options.driver.isApiTokenable()):
                    self.credentials.token = self.options.driver.getApiToken(
                        self.options.driver.authenticateApi(self.credentials)).token
            else:
                self.request.headerBuilder = self.options.driver.addApiAuthHeader(self.request.headerBuilder)
                self.request.bodyBuilder = self.options.driver.addApiAuthBody(self.request.bodyBuilder)

    def execute(self, command=''):
        if (command != ''):
            self.command = command

        t0 = time()

        self.commandtax = Commandtax(request=self.request, command=self.command, options=self.options,
                                     parameters=self.parameters)

        self.executionTime = time() - t0

        self.logBuffer = State.log.getLoggerDriver().buffer
        State.log.getLoggerDriver().outputLog()

        return self.commandtax
