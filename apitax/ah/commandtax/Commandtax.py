# System import
import shlex

# Application import
from apitax.ah.flow.LoadedDrivers import LoadedDrivers
from apitax.ah.flow.requests.ApitaxRequest import ApitaxRequest
from apitax.ah.flow.responses.ApitaxResponse import ApitaxResponse
from apitax.ah.models.Options import Options
from apitax.ah.models.State import State
from apitax.ah.models.Command import Command


# Command is used to distribute the workload amoung a heirarchy of possible handlers
# Command is the 'brain' of the application
class Commandtax:
    def __init__(self, request: ApitaxRequest = ApitaxRequest(), command='', options: Options = Options(),
                 parameters={}):

        self.config = State.config
        self.request = request
        self.command = command
        self.parameters = parameters
        self.options = options

        self.response: ApitaxResponse = None

        driverName = None
        isScript = False

        if (type(self.command) is not list):
            self.command = shlex.split(self.command.strip())

        if (len(self.command) < 1):
            return

        if ('--apitax-debug' in self.command):
            self.options.debug = True
            del self.command[self.command.index('--apitax-debug')]

        if ('--apitax-sensitive' in self.command):
            self.options.sensitive = True
            del self.command[self.command.index('--apitax-sensitive')]

        if ('--apitax-driver' in self.command):
            driverName = self.command[self.command.index('--apitax-driver') + 1]
            del self.command[self.command.index('--apitax-driver')]
            del self.command[self.command.index('--apitax-sensitive') + 1]

        if ('--apitax-script' in self.command):
            isScript = True
            del self.command[self.command.index('--apitax-script')]

        if (driverName):
            self.options.driver = LoadedDrivers.getDriver(driverName)
        elif (LoadedDrivers.getDriver(self.command[0])):
            self.options.driver = LoadedDrivers.getDriver(self.command[0])
            del self.command[0]
        else:
            self.options.driver = LoadedDrivers.getDefaultDriver()

        self.command = Command(command=self.command, request=self.request, parameters=self.parameters,
                               options=self.options)

        if (isScript and self.options.driver.isDriverScriptable()):
            self.response = self.options.driver.handleDriverScript(self.command)
        elif (self.options.driver.isDriverCommandable()):
            self.response = self.options.driver.handleDriverCommand(self.command)
        else:
            State.log.error(
                'Driver `' + self.options.driver.getDriverName() + '` does not support this operation when expecting script(' + str(
                    isScript) + '): ' + str(self.command))

