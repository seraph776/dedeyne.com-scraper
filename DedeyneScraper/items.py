import scrapy
from scrapy.loader import Item, ItemLoader
from itemloaders.processors import TakeFirst, MapCompose


def clean_price(price):
    return price.rstrip('€')


def clean_cnk(param):
    return param.lstrip('CNK')


class DedeyneItem(Item):
    product = scrapy.Field()
    price = scrapy.Field()
    cnk = scrapy.Field()
    manufacturer = scrapy.Field()
    image_urls = scrapy.Field()


class DedeyneItemLoader(ItemLoader):
    price_in = MapCompose(clean_price, str.strip)
    price_out = TakeFirst()

    cnk_in = MapCompose(clean_cnk, str.strip)
    image_urls_in = TakeFirst()

