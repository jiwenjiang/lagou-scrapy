import scrapy
import json

from tutorial.items import LaGou


class SfSpider(scrapy.Spider):
    name = "lagou"

    # allowed_domains = ["lagou.com"]

    def start_requests(self):
        url = "https://www.lagou.com/jobs/positionAjax.json?gj=3%E5%B9%B4%E5%8F%8A%E4%BB%A5%E4%B8%8B%2C3-5%E5%B9%B4&xl=%E6%9C%AC%E7%A7%91&px=default&city=%E6%88%90%E9%83%BD&needAddtionalResult=false&isSchoolJob=0"
        for i in range(1, 14):
            formdata = {'first': 'true', 'pn': str(i), 'kd': 'web前端'}
            print(i)
            yield scrapy.FormRequest(str(url), callback=self.parseJson, formdata=formdata)


    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)

    def parseJson(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        for sel in jsonresponse['content']['positionResult']['result']:
            item = LaGou()
            item['salary'] = sel['salary']
            item['company'] = sel['companyFullName']
            yield item
