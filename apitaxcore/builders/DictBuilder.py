# Builder class for creating headers dynamically
class DictBuilder:
    def __init__(self):
        self.built = {}

    def add(self, item):
        self.built.update(item)
        return self

    def remove(self, item):
        return self.built.pop(item, None)

    def get(self):
        return self.built