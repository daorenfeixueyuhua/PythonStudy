# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DushuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 章节名称
    chapterName = scrapy.Field()
    # 内容
    text = scrapy.Field()
    pass
