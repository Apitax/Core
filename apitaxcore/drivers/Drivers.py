from apitax.logs.Log import Log


class Drivers:
    drivers = None

    @staticmethod
    def initialize():
        Drivers.drivers = {}

    @staticmethod
    def add(name, driver):
        name = name.lower()
        if (name == 'default' or name == 'defaultdriver'):
            Log().error("A driver cannot be named default for driver: " + name)
            return None
        Drivers.drivers[name + "driver"] = driver

    @staticmethod
    def get(name):
        name = name.lower()
        if (name not in Drivers.drivers):
            Log().error("Driver '" + name + "' does not exist or has not been imported/added.")
            return None
        return Drivers.drivers[name]
