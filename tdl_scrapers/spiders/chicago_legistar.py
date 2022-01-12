from scrapy import Request, Spider

from ..items import TdlItem


class ChicagoLegistarSpider(Spider):
    name = "chicago_legistar"
    base_url = "https://ocd.datamade.us"

    def start_requests(self):
        return [Request(f"{self.base_url}/bills/")]

    def parse(self, response):
        yield TdlItem()
