# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 主播名称
    nickname = scrapy.Field()
    # 主播图片地址
    imageLink = scrapy.Field()
    # 图片保存的位置
    imagePath = scrapy.Field()
    # pass
