import scrapy

from tutorial.items import SegmentFault

class SfSpider(scrapy.Spider):
    name = "sf"
    allowed_domains = ["soso.gamersky.com"]
    start_urls = [
        "http://soso.gamersky.com/cse/search?q=lol&click=1&s=3068275339727451251&nsid=1"
    ]

    def parse(self, response):
        for sel in response.xpath('//section'):
            item = SegmentFault()
            item['title'] = sel.xpath('div[2]/h2[1]/a[1]/text()').extract()
            item['auth'] = sel.xpath('div[2]/ul[1]/li[1]/a[1]/text()').extract()
            yield item