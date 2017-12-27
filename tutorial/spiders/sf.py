import scrapy

from tutorial.items import SegmentFault

class SfSpider(scrapy.Spider):
    name = "sf"
    allowed_domains = ["segmentfault.com"]
    start_urls = [
        "https://segmentfault.com/questions"
    ]

    def parse(self, response):
        for sel in response.xpath('//section'):
            item = SegmentFault()
            item['title'] = sel.xpath('div[2]/h2[1]/a[1]/text()').extract()
            item['auth'] = sel.xpath('div[2]/ul[1]/li[1]/a[1]/text()').extract()
            yield item