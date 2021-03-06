# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Spider51JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 职位
    job_name = scrapy.Field()

    # 公司名称
    company_name = scrapy.Field()

    # 公司名称
    companysize = scrapy.Field()

    # 城市
    city = scrapy.Field()

    # 薪酬
    salary = scrapy.Field()

    # 公司所属行业
    category = scrapy.Field()

    # 属性
    attribute_text = scrapy.Field()

    # 职位福利
    job_welfare = scrapy.Field()

    # 总页码数
    total_page = scrapy.Field()

    # pass
