class Options:
    def __init__(self, debug=False, sensitive=False, driver=None):# dataType = 'json'):
        self.debug = debug
        self.sensitive = sensitive
        self.driver = driver
        #self.dataType = dataType # json, xml, text
