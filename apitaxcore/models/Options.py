# from apitax.drivers.Driver import Driver


class Options:
    def __init__(self, debug: bool = False, sensitive: bool = False, driver=None):
        self.debug = debug
        self.sensitive = sensitive
        self.driver = driver
