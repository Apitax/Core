from apitax.ah.builders.HeaderBuilder import HeaderBuilder
from apitax.drivers.builtin.Api import Api


class ApiXml(Api):
    def getDriverName(self) -> str:
        return 'xmlapi'

    def getDriverTips(self) -> str:
        return 'I recommend this website for viewing and beautifying XML: https://codebeautify.org/xmlviewer'

    def getApiFormat(self) -> str:
        return 'xml'

    def addApiHeaders(self, headerBuilder: HeaderBuilder) -> HeaderBuilder:
        return headerBuilder.add({'Content-type': 'application/xml'})
