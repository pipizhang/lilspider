# -*- coding: utf-8 -*-

# Scrapy settings for net39 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import os
import os.path as path

BOT_NAME = 'net39'

SPIDER_MODULES = ['net39.spiders']
NEWSPIDER_MODULE = 'net39.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'net39 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    #'net39.middlewares.Net39SpiderMiddleware': 543,
    'lilspider.middlewares.DisallowDomainMiddleware': 30,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'lilspider.middlewares.ProxyMiddleware': 10,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 20,
    'lilspider.middlewares.MongoDBDupeFilterMiddleware': 30,
    'lilspider.middlewares.UserAgentMiddleware': 50,
    'net39.middlewares.Net39DownloaderMiddleware': 200
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}
EXTENSIONS = {
    'scrapy.extensions.closespider.CloseSpider': 500
}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'lilspider.pipelines.ImagePipeline': 100,
    'scrapy.pipelines.images.ImagesPipeline': 110,
    'net39.pipelines.ArticlePipeline': 200,
    'lilspider.pipelines.ItemDebugPipeline': 300,
    'scrapy_mongodb.MongoDBPipeline': 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

CLOSESPIDER_PAGECOUNT = 100
LOG_LEVEL = 'INFO'

# Images
IMAGES_STORE = path.abspath(path.dirname(path.realpath(__file__))+'/../../data/images')

# MongoDBPipeline
# See https://github.com/sebdah/scrapy-mongodb
MONGODB_URI = os.environ.get('MONGODB_URI')
MONGODB_DATABASE = 'scrapy'
MONGODB_COLLECTION = 'jkArticle'
MONGODB_UNIQUE_KEY = 'url'

# Proxy
HTTPPROXY_ENABLED = False
HTTPPROXY_ADDRESS = os.environ.get('HTTPPROXY_ADDRESS')

# Retry
RETRY_ENABLED = True

