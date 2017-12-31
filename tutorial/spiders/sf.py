import scrapy
import json


# from tutorial.items import SegmentFault


class SfSpider(scrapy.Spider):
    name = "sf"

    # allowed_domains = ["lagou.com"]

    def start_requests(self):
        return [scrapy.FormRequest("https://www.lagou.com/jobs/positionAjax.json?gj=3%E5%B9%B4%E5%8F%8A%E4%BB%A5%E4%B8%8B%2C3-5%E5%B9%B4&xl=%E6%9C%AC%E7%A7%91&px=default&city=%E6%88%90%E9%83%BD&needAddtionalResult=false&isSchoolJob=0",
                                   formdata={'first': 'true', 'pn': '1', 'kd': 'web前端'},
                                   callback=self.logged_in
                                   )]

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        print('234444')

    def logged_in(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        print('34444')
        print(jsonresponse)
        pass
