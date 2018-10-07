from apitaxcore.builders.ListBuilder import ListBuilder


class Catalog(ListBuilder):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def get(self):
        return {self.name: super().get()}
