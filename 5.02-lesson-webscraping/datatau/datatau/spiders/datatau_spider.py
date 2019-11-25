import scrapy
from datatau.items import DatatauItem
from scrapy.selector import Selector

class DatatauSpider(scrapy.Spider):
    name = "datatau"
    allowed_domains = ['datatau.com']
    start_urls = [
        'https://www.datatau.com',
        'https://www.google.com'
    ]

    def parse(self, response):
        items = []
        hxs = Selector(response)
        for sel in hxs.xpath("//td[@class='title']/a"):
            item = DatatauItem()
            item['title'] = sel.xpath("./text()").extract()
            item['link'] = sel.xpath("./@href").extract()
            item['url'] = sel.xpath("../span/text()").extract()
            items.append(item)

        return items
