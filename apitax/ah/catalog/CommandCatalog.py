from apitax.ah.catalog.Catalog import Catalog


class CommandCatalog(Catalog):

    def __init__(self):
        super().__init__("commands")

    def add(self, name, summary='', help='', driver='', examples=[]):
        item = {name: {'summary': summary, 'help': help, 'driver': driver, 'examples': examples}}
        super().add(item)
