from apitax.ah.builders.Builder import Builder


class Catalog(Builder):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.built = {self.name: {}}

    def add(self, item):
        super().add({self.name: item})
