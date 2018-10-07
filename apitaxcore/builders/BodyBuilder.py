from apitaxcore.builders.DictBuilder import DictBuilder


# Builder class for creating headers dynamically
class BodyBuilder(DictBuilder):
    def __init__(self):
        super().__init__()
