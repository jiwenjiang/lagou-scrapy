# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class TutorialItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass


class LaGou(scrapy.Item):
    salary = scrapy.Field()  # 薪资
    company = scrapy.Field()  # 公司
    financeStage = scrapy.Field()  # 融资状况
    workYear = scrapy.Field()  # 工作年限
    industryField = scrapy.Field()  # 公司领域
