import scrapy

from tutorial.items import SegmentFault

class SfSpider(scrapy.Spider):
    name = "sf"
    allowed_domains = ["segmentfault.com"]
    start_urls = [
        "https://segmentfault.com/questions"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = SegmentFault()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item