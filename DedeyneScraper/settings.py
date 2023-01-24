import os

BOT_NAME = 'DedeyneScraper'
SPIDER_MODULES = ['DedeyneScraper.spiders']
NEWSPIDER_MODULE = 'DedeyneScraper.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

FEEDS = {
    'data/%(name)s/%(name)s_%(time)s.csv': {
        'format': 'csv',
    }
}

FEED_EXPORT_FIELDS = ['product', 'price', 'cnk', 'manufacturer']

ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
IMAGES_STORE = os.path.join(os.getcwd(), 'images')

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
