# import os

from .base import *  # noqa

USER_AGENT = "TDL Scrapers [production mode]"

# Configure item pipelines
ITEM_PIPELINES = {}

EXTENSIONS = {
    "scrapy_sentry.extensions.Errors": 10,
    "scrapy.extensions.closespider.CloseSpider": None,
}

FEED_EXPORTERS = {
    "json": "scrapy.exporters.JsonItemExporter",
    "jsonlines": "scrapy.exporters.JsonLinesItemExporter",
}

FEED_FORMAT = "jsonlines"

# TODO: Write output to S3 potentially

FEED_PREFIX = "%Y/%m/%d"
