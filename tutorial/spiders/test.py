import scrapy
import json

from tutorial.items import LaGou


class SfSpider(scrapy.Spider):
    name = "test"
    pagesize = 12

    # allowed_domains = ["lagou.com"]

    start_urls = [
        "https://www.lagou.com/jobs/list_web%E5%89%8D%E7%AB%AF?labelWords=sug&fromSearch=true&suginput=web"
    ]

    def get_jobs(self):
        pass

    def parse(self, response):
        # self.logger.info('A response from %s just arrived!', response.url)
        print(response)

    def parseJson(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        for sel in jsonresponse['content']['positionResult']['result']:
            item = LaGou()
            item['salary'] = sel['salary']
            item['company'] = sel['companyFullName']
            item['financeStage'] = sel['financeStage']
            item['workYear'] = sel['workYear']
            item['industryField'] = sel['industryField'].split(",")
            yield item
