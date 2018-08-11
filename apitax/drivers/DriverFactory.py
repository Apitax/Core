# Import Drivers below here

from apitax.drivers.Drivers import Drivers


# End Driver Imports


# Factory class for creating HttpPlug Drivers
class DriverFactory:

    @staticmethod
    def make(name):
        return Drivers.get(name)

    @staticmethod
    def makeInstance(basedUpon):
        clazz = basedUpon.__class__
        return clazz()
