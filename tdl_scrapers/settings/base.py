import os

# Scrapy settings for tdl_scrapers project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = "tdl_scrapers"

SPIDER_MODULES = ["tdl_scrapers.spiders"]
NEWSPIDER_MODULE = "tdl_scrapers.spiders"
COMMANDS_MODULE = "tdl_scrapers.commands"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "TDL Scrapers [development mode]"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Throttle results by default
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = float(os.getenv("AUTOTHROTTLE_START_DELAY", 1.0))
AUTOTHROTTLE_MAX_DELAY = float(os.getenv("AUTOTHROTTLE_MAX_DELAY", 30.0))
AUTOTHROTTLE_TARGET_CONCURRENCY = float(
    os.getenv("AUTOTHROTTLE_TARGET_CONCURRENCY", 1.0)
)

# Configure item pipelines
ITEM_PIPELINES = {}

SPIDER_MIDDLEWARES = {}

DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware": 543,
}

EXTENSIONS = {
    "scrapy.extensions.closespider.CloseSpider": None,
}

CLOSESPIDER_ERRORCOUNT = 5
