import scrapy
import json

from tutorial.items import LaGou


class SfSpider(scrapy.Spider):
    name = "lagou"

    # allowed_domains = ["lagou.com"]

    def start_requests(self):
        url = "https://www.lagou.com/jobs/positionAjax.json?city=%E6%88%90%E9%83%BD&needAddtionalResult=false&isSchoolJob=0"
        for i in range(1, 31):
            istrue = 'true' if i == 1 else 'false'
            formdata = {'first': istrue, 'pn': str(i), 'kd': 'web前端'}
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
            item['financeStage'] = sel['financeStage']
            item['workYear'] = sel['workYear']
            item['industryField'] = sel['industryField'].split(",")
            yield item
