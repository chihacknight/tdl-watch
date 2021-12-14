from os.path import dirname, join

import pytest
from scrapy.http import TextResponse

from tdl_scrapers.spiders.chicago_legistar import ChicagoLegistarSpider


@pytest.fixture
def response():
    with open(join(dirname(__file__), "files", "chicago_legistar.json"), "r") as f:
        test_content = f.read()
    return TextResponse(
        url=ChicagoLegistarSpider.base_url, body=test_content, encoding="utf-8"
    )


@pytest.fixture
def items(response):
    spider = ChicagoLegistarSpider()
    return [item for item in spider.parse(response)]


def test_len(items):
    assert len(items) == 1
