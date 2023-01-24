from ..items import DedeyneItem, DedeyneItemLoader
import scrapy
import os


def get_links():
    d = os.getcwd()
    with open(os.path.join(d, 'links', 'links.csv')) as file:
        links = [i.strip() for i in file.readlines()]
    return links


class DedeyneSpider(scrapy.Spider):
    name = 'dedeyne'
    allowed_domains = ['apotheekdedeyne.be']

    def start_requests(self):
        links = get_links()
        for link in links:
            yield scrapy.Request(
                url=link,
                callback=self.parse,
            )

    def parse(self, response):
        dedeyne_product = DedeyneItemLoader(item=DedeyneItem(), selector=response)
        dedeyne_product.add_xpath('product', '//h2[@id="prod_title"]/text()')
        dedeyne_product.add_css('price', '.price-new::text')
        dedeyne_product.add_value('cnk', response.xpath('//div').re_first(r'CNK\s\d*'))
        dedeyne_product.add_xpath('image_urls', '//img[@class="product-dtl-thumb"]/@src')

        if response.xpath('//div[@class="model"]'):
            manufacturer = response.xpath('//div[@class="model"]/a/text()').get()
        else:
            manufacturer = 'None'
        dedeyne_product.add_value('manufacturer', manufacturer)
        yield dedeyne_product.load_item()
