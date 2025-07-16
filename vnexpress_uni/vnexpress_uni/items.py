# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VnexpressUniItem(scrapy.Item):
    # define the fields for your item here like:
    urls = scrapy.Field()
    header = scrapy.Field()
    program_group = scrapy.Field()
    program_code = scrapy.Field()
    program_name = scrapy.Field()
    entry_score = scrapy.Field()
    tuition_fee = scrapy.Field()
