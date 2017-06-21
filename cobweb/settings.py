# -*- coding: utf-8 -*-

# Scrapy settings for cobweb project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
from cobweb.utilities import load_list_from_file

BOT_NAME = 'Googlebot'

SPIDER_MODULES = ['cobweb.spiders']
NEWSPIDER_MODULE = 'cobweb.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent

REFERER_LIST = load_list_from_file('/cobweb/resources/referers.txt')

USER_AGENT_LIST = load_list_from_file('/cobweb/resources/useragents.txt')

# Proxy list containing entries like
# http://host1:port1
#HTTP_PROXIES = load_lines('/cobweb/resources/prod_proxies.txt')
HTTP_PROXIES = load_list_from_file('/cobweb/resources/test_proxies.txt')

# Retry many times since proxies often fail
RETRY_TIMES = 20
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY=5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#    'Accept-Language': 'en',
#    'Referer': 'http://www.google.com',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'cobweb.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares or your custom middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'cobweb.middlewares.RandomUserAgentMiddleware': 400,
    #'cobweb.middlewares.ProxyMiddleware': 410,
    'cobweb.middlewares.RandomProxyMiddleware': 420,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'cobweb.pipelines.MongoDBPipeline',
}

# This is just for development. Don't do this on production. Put your credentials elsewhere.
MONGODB_CREDENTIALS = {
    "server": "localhost",
    "port": 27017,
    "database": "real_estate",
    "username": "your_username",
    "password": "your_password"
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
