# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmmmiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 图片标题
    title = scrapy.Field()
    # 图片名
    picture_name = scrapy.Field()
    # 图片下载地址
    image_url = scrapy.Field()
    # 图片保存地址
    image_path = scrapy.Field()
    # pass
